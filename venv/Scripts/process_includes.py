#!C:\Users\Muhammet\IzibizTestEntegration\venv\Scripts\python.exe
"""
    python %prog [options] <in_schema.xsd>  [<out_schema.xsd>]
Synopsis:
    Prepare schema document.  Replace include and import elements.
    Read from in_schema or stdin.  Write to out_schema or stdout.
Examples:
    python %prog myschema.xsd
    python %prog myschema.xsd newschema.xsd
    python %prog -f myschema.xsd newschema.xsd
    cat infile.xsd | python %prog > outfile.xsd
"""

#
# Imports

from __future__ import print_function
import logging
import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
import os
import copy
from optparse import OptionParser, Values
import itertools
from copy import deepcopy
from lxml import etree
import requests

try:
    from gds_inner_name_map import Inner_name_map
except ModulenotfoundExp_:
    Inner_name_map = None

_log = logging.getLogger(__name__)

#
# Globals and constants

#
# Do not modify the following VERSION comments.
# Used by updateversion.py.
##VERSION##
VERSION = '2.43.2'
##VERSION##

CatalogDict = {}
# the base url to use for all relative paths in the catalog
CatalogBaseUrl = None
XSDNameSpace = 'http://www.w3.org/2001/XMLSchema'

BuiltinSimpleTypeNames = [
    'string',
    'boolean',
    'float',
    'double',
    'decimal',
    'duration',
    'dateTime',
    'time',
    'date',
    'gYearMonth',
    'gYear',
    'gMonthDay',
    'gDay',
    'gMonth',
    'hexBinary',
    'base64Binary',
    'anyURI',
    'QName',
    'NOTATION',
    'normalizedString',
    'token',
    'language',
    'IDREFS',
    'ENTITIES',
    'NMTOKEN',
    'NMTOKENS',
    'Name',
    'NCName',
    'ID',
    'IDREF',
    'ENTITY',
    'integer',
    'nonPositiveInteger',
    'negativeInteger',
    'long',
    'int',
    'short',
    'byte',
    'nonNegativeInteger',
    'unsignedLong',
    'unsignedInt',
    'unsignedShort',
    'unsignedByte',
    'positiveInteger',
    'yearMonthDuration',
    'dayTimeDuration',
    'dateTimeStamp',
]


#
# Exceptions

class SchemaIOError(IOError):
    """Exception definition"""
    pass


class InnerNameMapError(Exception):
    """Exception definition"""
    pass


class RenameData(object):
    """A structure used to carry parameters."""
    __slots__ = ('global_names', 'global_count',
                 'modified_elements', 'name_mappings',
                 )

    def __init__(self, global_names=None, global_count=0,
                 modified_elements=None, name_mappings=None):
        # global_names is a set containing all the global names,
        #     both original names and new names for each complexType and
        #     simpleType.
        # name_mappings is a dictionary with:
        #     key -- a string -- the unqualified-name (orig-name)
        #     value -- list of names: [orig-name, new-name1, new-name2, ...]
        if global_names is None:
            self.global_names = set()
        else:
            self.global_names = global_names
        self.global_count = global_count
        if modified_elements is None:
            self.modified_elements = set()
        else:
            self.modified_elements = modified_elements
        if name_mappings is None:
            self.name_mappings = {}
        else:
            self.name_mappings = name_mappings

    def __str__(self):
        s1 = ("<RenameData at {}\n    global_names: {}\n"
              "    global_count: {}\n"
              "    modified_elements: {}\n"
              "    name_mappings: {}\n"
              ">".format(
                  id(self),
                  self.global_names, self.global_count,
                  self.modified_elements, self.name_mappings))
        return s1


def load_catalog(catalogpath):
    """Load the catalog base URL and save in global variable."""
    global CatalogBaseUrl
    if catalogpath:
        CatalogBaseUrl = os.path.split(catalogpath)[0]
        catalog = etree.parse(open(catalogpath, "rb"))
        for elements in catalog.getroot().findall(
                "{urn:oasis:names:tc:entity:xmlns:xml:catalog}public"):
            CatalogDict[elements.get("publicId")] = elements.get("uri")

#
# Functions for external use


def process_include_files(
        infile, outfile, inpath='',
        catalogpath=None,
        fixtypenames=None,
        no_collect_includes=False,
        no_redefine_groups=False):
    """The root/main function"""
    load_catalog(catalogpath)
    options = Values({
        'force': False,
        'fixtypenames': fixtypenames,
        'no_collect_includes': no_collect_includes,
        'no_redefine_groups': no_redefine_groups,
    })
    doc, ns_dict, schema_ns_dict, rename_data = prep_schema_doc(
        infile, outfile, inpath, options)
    return doc, ns_dict, schema_ns_dict, rename_data


def get_all_root_file_paths(
        infile,
        inpath='',
        catalogpath=None,
        shallow=False):
    """Get the file path for all imported and included schema files."""
    if inpath.startswith('/'):
        inpath = os.path.relpath(inpath)
    load_catalog(catalogpath)
    # Note: infile has been opened in binary mode.
    doc1 = etree.parse(infile)
    root1 = doc1.getroot()
    rootPaths = []
    params = Params()
    params.parent_url = infile
    params.base_url = os.path.split(inpath)[0]
    get_root_file_paths(root1, params, rootPaths, shallow)
    rootPaths.append(inpath)
    return rootPaths


#
# Classes

class Params(object):
    """A structure used to carry parameters."""
    members = ('base_url', 'already_processed', 'parent_url', )

    def __init__(self):
        self.base_url = None
        self.already_processed = set()
        self.parent_url = None

    def __setattr__(self, name, value):
        if name not in self.members:
            raise AttributeError('Class %s has no set-able attribute "%s"' % (
                self.__class__.__name__, name, ))
        self.__dict__[name] = value


#
# Functions for internal use and testing


def clear_includes_and_imports(node):
    namespace = node.nsmap[node.prefix]
    child_iter1 = node.iterfind('{%s}include' % (namespace, ))
    child_iter2 = node.iterfind('{%s}import' % (namespace, ))
    for child in itertools.chain(child_iter1, child_iter2):
        repl = etree.Comment(etree.tostring(child))
        repl.tail = '\n'
        node.replace(child, repl)


def get_ref_info(node, params):
    # first look for the schema location in the catalog, if not
    # there, then see if it's specified in the node
    namespace = node.get('namespace')
    url = None
    baseUrl = None
    if namespace in CatalogDict:
        url = CatalogDict[namespace]
        # setup the base url in case the path
        # in the catalog was a relative path
        baseUrl = CatalogBaseUrl
    if not url:
        url = node.get('schemaLocation')
    if not url:
        msg = '*** Warning: missing "schemaLocation" attribute in %s\n' % (
            params.parent_url, )
        sys.stderr.write(msg)
        return (None, None)
    # Uncomment the next lines to help track down missing schemaLocation etc.
    # print '(resolve_ref) url: %s\n    parent-url: %s' % (
    #     url, params.parent_url, )
    if not baseUrl:
        baseUrl = params.base_url
    if baseUrl and not (
            url.startswith('/') or
            url.startswith('http:') or
            url.startswith('https:') or
            url.startswith('ftp:')):
        locn = '%s/%s' % (baseUrl, url, )
        schema_name = locn
    else:
        locn = url
        schema_name = url
    return locn, schema_name


def resolve_ref(node, params, options):
    locn, schema_name = get_ref_info(node, params)
    if locn is not None and not (
            locn.startswith('/') or
            locn.startswith('http:') or
            locn.startswith('https:') or
            locn.startswith('ftp:')):
        schema_name = os.path.abspath(locn)

    if locn is None or schema_name in params.already_processed:
        return None

    if locn.startswith('file://'):
        schema_name = os.path.abspath(locn[7:])

    params.already_processed.add(schema_name)
##     print 'trace --'
##     print '    url:        : %s' % (url, )
##     print '    base        : %s' % (params.base_url, )
##     print '    parent      : %s' % (params.parent_url, )
##     print '    locn        : %s' % (locn, )
##     print '    schema_name : %s\n' % (schema_name, )
    if (locn.startswith('https:') or
            locn.startswith('http:') or
            locn.startswith('ftp:')):
        try:
            headers = {
                'User-Agent':
                    "Mozilla/5.0 (X11; 'Linux x86_64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) ",
            }
            content = requests.get(locn, headers=headers).content
            params.parent_url = locn
            params.base_url = os.path.split(locn)[0]
        except requests.exceptions.HTTPError:
            msg = "Can't find file %s referenced in %s." % (
                locn, params.parent_url, )
            raise SchemaIOError(msg)
    else:
        content = None
        if locn.startswith('file://'):
            locn = locn[7:]
        if os.path.exists(locn):
            if sys.version_info.major == 2:
                infile = open(locn)
                unencoded_content = infile.read()
                content = unencoded_content
            else:
                infile = open(locn, 'rb')
                content = infile.read()
            infile.close()
            params.parent_url = locn
            params.base_url = os.path.split(locn)[0]
        if content is None:
            msg = "Can't find file %s referenced in %s." % (
                locn, params.parent_url, )
            raise SchemaIOError(msg)
##     if content is None:
##         msg = "Can't find file %s referenced in %s." % (
##             locn, params.parent_url, )
##         raise SchemaIOError(msg)
    return content


def get_fixed_schema_nsmap(node, prefix='xs'):
    nsmap = {}
    if 'xs' in node.nsmap:
        nsmap[prefix] = node.nsmap.get('xs')
    elif 'xsd' in node.nsmap:
        nsmap[prefix] = node.nsmap.get('xsd')
    elif None in nsmap:
        nsmap[prefix] = node.nsmap.get(None)
    else:
        nsmap[prefix] = 'http://www.w3.org/2001/XMLSchema'
    return nsmap


_SCHEMA_DEFAULTS = {
    "targetNamespace": "None",
    #   "version": "None",
    #   "finalDefault": "",
    #   "blockDefault": "",
    "attributeFormDefault": "unqualified",
    "elementFormDefault": "unqualified",
    #   "defaultAttributes": "None",
    #   "xpathDefaultNamespace":  "##local",
    #   "id": "None",
    #   "{http://www.w3.org/XML/1998/namespace}lang": "None", # xml namespace
}


def _set_schema_defaults(schemaNode):
    '''Update attributes to contain all options explicitly.'''
    for k, v in _SCHEMA_DEFAULTS.items():
        if k not in schemaNode.attrib.keys():
            schemaNode.attrib.update({k: str(v)})
    return schemaNode


_PUSH_ATTRIBUTES = [
    'elementFormDefault',
    'attributeFormDefault',
    'targetNamespace',
]

_IGNORE_TAGS = [
    '{http://www.w3.org/2001/XMLSchema}import',
    '{http://www.w3.org/2001/XMLSchema}include',
]


def collect_inserts(node, params, inserts, ns_dict, schema_ns_dict,
                    rename_data, options):
    """Collect all the schemas (imported and included).
    If there are duplicate unqualified names, rename all but one, and
    collect a dictionary of the renamed names."""
    nsmap = get_fixed_schema_nsmap(node)
    roots = []
    # TODO this is probably not the right place
    node = _set_schema_defaults(node)
    for child in node.iterchildren():
        if child.tag in _IGNORE_TAGS or isinstance(child, etree._Comment):
            continue
        for p in _PUSH_ATTRIBUTES:
            child.attrib[p] = node.attrib[p]

    child_iter1 = node.iterfind('xs:include', namespaces=nsmap)
    child_iter2 = node.iterfind('xs:import', namespaces=nsmap)
    for child in itertools.chain(child_iter1, child_iter2):
        aux_roots = collect_inserts_aux(
            node,
            child, params, inserts, ns_dict, schema_ns_dict,
            rename_data, options)
        roots.extend(aux_roots)
    return roots
# end collect_inserts


def collect_inserts_aux(
        master_schema_root,
        child, params, inserts, ns_dict, schema_ns_dict,
        rename_data, options):
    """A helper function."""
    roots = []
    save_base_url = params.base_url
    string_content = resolve_ref(child, params, options)
    if string_content is not None:
        # root is the document to insert
        root = etree.fromstring(string_content, base_url=params.base_url)
        root = _set_schema_defaults(root)
        # https://www.w3schools.com/xml/el_include.asp
        # "Definitive XML Schema", by Priscilla Walmsley, page 66
        if child.tag == '{http://www.w3.org/2001/XMLSchema}include':
            including_TNS = master_schema_root.get('targetNamespace')
            included_TNS = root.get('targetNamespace')
            if included_TNS == 'None':
                included_TNS = None
            good = False
            if including_TNS == included_TNS:
                good = True
            elif including_TNS is None and included_TNS is None:
                good = True
            elif including_TNS is not None and included_TNS is None:
                good = True
            assert good, "targetNamespace match error"
        # uniquify
        make_names_unique(root, rename_data, options)
        roots.append(root)
        schema_ns_dict.update(root.nsmap)
        update_ns_dict(root, ns_dict, options)
        for child1 in root:
            if (child1.tag in _IGNORE_TAGS or
                    isinstance(child1, etree._Comment)):
                continue
            namespace = child1.nsmap[child1.prefix]
            _log.debug(
                'Processing "%s", attribs "%s".',
                repr(child1),
                repr(child1.attrib))
            comment = etree.Comment(etree.tostring(child))
            comment.tail = '\n'
            inserts.append(comment)
            child2 = copy.copy(child1)
            # copy settings
            for p in _PUSH_ATTRIBUTES:
                child2.attrib[p] = root.attrib[p]
            _log.debug(
                'Node "%s", attribs: "%s"',
                repr(child2),
                repr(child2.attrib))
            # copy targetNamespace from right source
            if child.tag == '{%s}import' % namespace:
                child2.attrib['targetNamespace'] = root.attrib[
                    'targetNamespace']
                child2.attrib['mustOverrideTargetNamespace'] = 'true'
            elif child.tag == '{%s}include' % namespace:
                child2.attrib['targetNamespace'] = master_schema_root.attrib[
                    'targetNamespace']
            _log.debug(
                'Saving node "%s", attribs: "%s"',
                repr(child2),
                repr(child2.attrib))
            inserts.append(child2)

        insert_roots = collect_inserts(
            root, params, inserts, ns_dict, schema_ns_dict,
            rename_data, options)
        roots.extend(insert_roots)

    params.base_url = save_base_url
    return roots
# end collect_inserts_aux


def make_map_name(root, name):
    target_namespace = root.get('targetNamespace')
    if target_namespace is not None:
        qname = '{%s}%s' % (target_namespace, name, )
    else:
        qname = name
    return qname


# uniquify
def make_names_unique(root,
                      rename_data, options):
    """If there are duplicate names, rename each to something unique."""
    nsmap = get_fixed_schema_nsmap(root)
    # Get all top level xs:(complex|simple)Type definitions in this schema
    ct_defs = root.xpath('./xs:complexType', namespaces=nsmap)
    st_defs = root.xpath('./xs:simpleType', namespaces=nsmap)
    for type_def in itertools.chain(ct_defs, st_defs):
        name = type_def.get('name')
        map_name = make_map_name(root, name)
        if name in rename_data.global_names:
            new_name = unique_name(name, rename_data)
            if new_name != name:
                type_def.attrib['name'] = new_name
                # Hold a ref to the lxml element so that the python
                # representation does not disappear.
                rename_data.modified_elements.add(type_def)
        else:
            new_name = name
        if new_name != name:
            rename_data.name_mappings[map_name] = new_name
        rename_data.global_names.add(name)


def update_ns_dict(root, ns_dict, options):
    """Update the namespace dictionary with the target namespace prefix,
    if there is one, for each global xs:element and xs:complexType.
    """
    if 'targetNamespace' in root.attrib:
        namespace = root.get('targetNamespace')
        defs = [nsdef for nsdef in root.nsmap.items() if nsdef[1] == namespace]
        if defs:
            prefix = defs[0][0]
            # Get top level xs:complexType and xs:element elements.
            nsmap = {'xs': XSDNameSpace}
            items1 = root.xpath('./xs:complexType', namespaces=nsmap)
            items2 = root.xpath('./xs:element', namespaces=nsmap)
            names = ([item.get('name') for item in items1] +
                     [item.get('name') for item in items2])
            for name in names:
                ns_dict[name] = (prefix, namespace)


def get_root_file_paths(node, params, rootPaths, shallow):
    """Get the file path for all imported and included schema files."""
    namespace = node.nsmap[node.prefix]
    child_iter1 = node.iterfind('{%s}include' % (namespace, ))
    child_iter2 = node.iterfind('{%s}import' % (namespace, ))
    for child in itertools.chain(child_iter1, child_iter2):
        get_root_file_paths_aux(child, params, rootPaths, shallow)


def get_root_file_paths_aux(child, params, rootPaths, shallow):
    """Helper function"""
    save_base_url = params.base_url
    path, _ = get_ref_info(child, params)
    string_content = resolve_ref(child, params, None)
    if string_content is not None:
        if not shallow:
            root = etree.fromstring(string_content, base_url=params.base_url)
            get_root_file_paths(root, params, rootPaths, shallow)
    if path is not None and path not in rootPaths:
        if path.startswith('file://'):
            path = path[7:]
        rootPaths.append(path)
    params.base_url = save_base_url


def make_file(outFileName, options):
    outFile = None
    if (not options.force) and os.path.exists(outFileName):
        if sys.version_info.major == 3:
            raw_input = input
        reply = raw_input(
            'File %s exists.  Overwrite? (y/n): ' % outFileName)
        if reply == 'y':
            outFile = open(outFileName, 'w')
    else:
        outFile = open(outFileName, 'w')
    return outFile


def prep_schema_doc(infile, outfile, inpath, options):
    # Note: infile has been opened in binary mode.
    if inpath.startswith('/'):
        inpath = os.path.relpath(inpath)
    doc1 = etree.parse(infile)
    root1 = doc1.getroot()
    params = Params()
    params.parent_url = infile
    params.base_url = os.path.split(inpath)[0]
    inserts = []
    ns_dict = {}
    schema_ns_dict = {}
    rename_data = RenameData()
    schema_ns_dict.update(root1.nsmap)
    if not options.no_collect_includes:
        collect_inserts(root1, params, inserts, ns_dict,
                        schema_ns_dict, rename_data, options)
        make_names_unique(root1, rename_data, options)
        fixup_refs(root1, inserts, rename_data)
        fixup_refs(root1, root1.getchildren(), rename_data)
        fixup_refs_element(root1, rename_data)
        root2 = copy.copy(root1)
        clear_includes_and_imports(root2)
        for insert_node in inserts:
            root2.append(insert_node)
    else:
        root2 = root1
    if not options.no_redefine_groups:
        process_groups(root2)
    # fix before renaming
    fix_top_level_simpletype_elements(root2, rename_data)
    raise_anon_complextypes(root2, rename_data)
    fix_type_names(root2, options)
    doc2 = etree.ElementTree(root2)
    if sys.version_info.major == 2:
        doc2.write(outfile)
    else:
        outfile.write(etree.tostring(root2).decode('utf-8'))
    # dbg
    #print('\nmapping:')
    #for item in rename_data.name_mappings.items():
    #    print('    {}'.format(item))
    #print('\n')
    # dbg
    #import pprint
    #with open('junk.log', 'w') as dbgfile:
    #    dbgfile.write('\nrename_data.global_names:\n')
    #    msg = pprint.pformat(rename_data.global_names)
    #    dbgfile.write(msg)
    #    dbgfile.write('\n----------------------------\n')
    #    dbgfile.write('\nrename_data.name_mappings:\n')
    #    msg = pprint.pformat(rename_data.name_mappings)
    #    dbgfile.write(msg)
    #    dbgfile.write('\n----------------------------\n')
    #    dbgfile.write('\nns_dict:\n')
    #    msg = pprint.pformat(ns_dict)
    #    dbgfile.write(msg)
    # dbg
    return doc2, ns_dict, schema_ns_dict, rename_data
# end prep_schema_doc


def prep_schema(inpath, outpath, options):
    if inpath:
        infile = open(inpath, 'rb')
    else:
        infile = sys.stdin
    if outpath:
        outfile = make_file(outpath, options)
    else:
        outfile = sys.stdout
    if outfile is None:
        return
    prep_schema_doc(infile, outfile, inpath, options)
    if inpath:
        infile.close()
    if outpath:
        outfile.close()


def process_groups(root):
    """Get all the xs:group definitions at top level."""
    if root.prefix:
        namespaces = {root.prefix: root.nsmap[root.prefix]}
        pattern = './%s:group' % (root.prefix, )
        defs = root.xpath(pattern, namespaces=namespaces)
    else:
        pattern = './group'
        defs = root.xpath(pattern)
    defs = [node for node in defs if node.get('name') is not None]
    # Get all the xs:group references (below top level).
    if root.prefix:
        namespaces = {root.prefix: root.nsmap[root.prefix]}
        pattern = './*//%s:group' % (root.prefix, )
        refs = root.xpath(pattern, namespaces=namespaces)
    else:
        pattern = './*//group'
        refs = root.xpath(pattern)
    refs = [node for node in refs if node.get('ref') is not None]
    # Create a dictionary of the named model groups (definitions).
    def_dict = {}
    for node in defs:
        def_dict[trim_prefix(node.get('name'))] = node
    replace_group_defs(def_dict, refs)


def fix_type_names(root, options):
    """Fix up (complexType) type names."""
    fixnamespec = options.fixtypenames
    if fixnamespec:
        namespecs = fixnamespec.split(';')
    else:
        namespecs = []
    for namespec in namespecs:
        names = namespec.split(':')
        if len(names) == 2:
            oldname = names[0]
            newname = names[1]
        elif len(names) == 1:
            oldname = names[0]
            newname = '%sxx' % (oldname, )
        else:
            continue
        # Change the name (name attribute) of the complexType.
        pat = './/%s:complexType[@name="%s"]' % (
            root.prefix, oldname)
        elements = xpath_find(root, pat)
        if len(elements) < 1:
            sys.stderr.write(
                "\nWarning: fix-type-names can't find complexType '%s'.  "
                "Exiting.\n\n" % (oldname, ))
            sys.exit(1)
        if len(elements) < 1:
            sys.stderr.write(
                "Warning: fix-type-names found more than "
                "one complexType '%s'.  "
                "Changing first." % (oldname, ))
        element = elements[0]
        element.set('name', newname)
        # Change the reference (type attribute) of child elements.
        pat = './/%s:element' % (root.prefix, )
        elements = xpath_find(root, pat)
        for element in elements:
            typename = element.get('type')
            if not typename:
                continue
            names = typename.split(':')
            if len(names) == 2:
                typename = names[1]
            elif len(names) == 1:
                typename = names[0]
            else:
                continue
            if typename != oldname:
                continue
            if not element.getchildren():
                element.set('type', newname)
        # Change the extensions ('base' attribute) that refer to the old type.
        pat = './/%s:extension' % (root.prefix, )
        elements = xpath_find(root, pat)
        for element in elements:
            typename = element.get('base')
            if not typename:
                continue
            names = typename.split(':')
            if len(names) == 2:
                typename = names[1]
            elif len(names) == 1:
                typename = names[0]
            else:
                continue
            if typename != oldname:
                continue
            element.set('base', newname)
# end fix_type_names


def fixup_refs(root, inserts, rename_data):
    "Fixup/change references for duplicate unqualified names."""
    nsmap = get_fixed_schema_nsmap(root)
    ct_tag = '{{{}}}complexType'.format(nsmap['xs'])
    st_tag = '{{{}}}simpleType'.format(nsmap['xs'])
    for node in inserts:
        if node.tag == ct_tag:
            fixup_refs_complextype(node, nsmap, rename_data)
            fixup_refs_extension_base(node, nsmap, rename_data)
        elif node.tag == st_tag:
            fixup_refs_simpletype(node, nsmap, rename_data)


def fixup_refs_element(element, rename_data):
    "Fixup/change references for names top-level elements."""
    nsmap = get_fixed_schema_nsmap(element)
    elements = element.xpath('./xs:element', namespaces=nsmap)
    for node in elements:
        fixup_refs_complextype_helper(node, 'type', nsmap, rename_data)


def fixup_refs_complextype(complextype, nsmap, rename_data):
    "Fixup/change references for duplicate unqualified names."""
    nsmap = get_fixed_schema_nsmap(complextype)
    elements = complextype.xpath('.//xs:element', namespaces=nsmap)
    attributes = complextype.xpath('.//xs:attribute', namespaces=nsmap)
    for node in itertools.chain(elements, attributes):
        fixup_refs_complextype_helper(node, 'type', nsmap, rename_data)
        fixup_refs_complextype_helper(node, 'ref', nsmap, rename_data)


def fixup_refs_complextype_helper(node, spec, nsmap, rename_data):
    """Change references for specified attribute, e.g. 'type' or 'ref'."""
    type_name = node.get(spec)
    if type_name:
        prefix, type_name1 = split_prefix(type_name)
        if prefix:
            namespace = node.nsmap.get(prefix)
            if namespace:
                qname = '{{{}}}{}'.format(namespace, type_name1)
                uniquename = rename_data.name_mappings.get(qname)
                if uniquename and uniquename != type_name:
                    node.attrib[spec] = uniquename
                    rename_data.modified_elements.add(node)


def fixup_refs_extension_base(complextype, nsmap, rename_data):
    """Fixup/change extension base refs for duplicate unqualified names."""
    extension = complextype.xpath('./*/xs:extension', namespaces=nsmap)
    if extension:
        extension = extension[0]
        base = extension.get('base')
        if base:
            prefix, name = split_prefix(base)
            if prefix:
                namespace = complextype.nsmap.get(prefix)
                if namespace:
                    qname = '{{{}}}{}'.format(namespace, name)
                    unique_name = rename_data.name_mappings.get(qname)
                    if unique_name:
                        extension.attrib['base'] = unique_name
                        rename_data.modified_elements.add(extension)


def fixup_refs_simpletype(simpletype, nsmap, rename_data):
    """Fixup/change restriction references for duplicate unqualified names."""
    restriction = simpletype.xpath('./xs:restriction', namespaces=nsmap)
    if restriction:
        restriction = restriction[0]
        base = restriction.get('base')
        if base:
            prefix, name = split_prefix(base)
            if prefix:
                namespace = simpletype.nsmap.get(prefix)
                if namespace:
                    qname = '{{{}}}{}'.format(namespace, name)
                    unique_name = rename_data.name_mappings.get(qname)
                    if unique_name:
                        restriction.attrib['base'] = unique_name
                        rename_data.modified_elements.add(restriction)


def fix_top_level_simpletype_elements(root, rename_data):
    """Fix top level elements that are defined with a simpleType."""
    # Find all the top-level element declarations.
    el = etree.Comment(text="complexType wrappers for a simpleType")
    el.tail = "\n\n"
    root.append(el)
    el_decls = xpath_find(root, './xs:element')
    prefix = 'xs' if 'xs' in root.nsmap else (
        'xsd' if 'xsd' in root.nsmap else None)
    # If a top-level element is defined as a simpleType, create
    #   a complexType containing a simpleContent under the same name,
    #   and rename the simple_type to something known.
    for e in el_decls:
        orig_name = e.get('ref')
        if orig_name is None:
            orig_name = e.get('type')
        if orig_name is None:
            continue
        st = find_top_level_st_object(root, orig_name)
        if st is None:
            continue
        # change name: append _impl
        st.set('name', st.get('name') + '_impl')
        rename_data.modified_elements.add(st)
        # add ct-as-st-wrapper under old name
        create_complex_simplecontent_item(
            root, orig_name, st, prefix, rename_data)


def create_complex_simplecontent_item(root, ct_name, st, prefix, rename_data):
    """Create a complexType containing simpleContent. Add it at top-level."""
    # copy attributes, they contain configuration
    ct_attribs = {k: v for k, v in st.attrib.items()}
    ct_attribs['name'] = ct_name
    complextype_obj = etree.SubElement(
        root,
        '{{{}}}complexType'.format(root.nsmap.get(prefix)),
        attrib=ct_attribs,
    )
    simplecontent_obj = etree.SubElement(
        complextype_obj,
        '{{{}}}simpleContent'.format(root.nsmap.get(prefix)),
    )
    etree.SubElement(
        simplecontent_obj,
        '{{{}}}extension'.format(root.nsmap.get(prefix)),
        attrib={'base': st.attrib['name']},
    )


def find_top_level_st_object(root, obj_name):
    """Find a top-level simpleType object by name."""
    obj = None
    pat = './xs:simpleType[@name="%s"]' % (obj_name, )
    objs = xpath_find(root, pat)
    if objs:
        obj = objs[0]
    else:
        names = obj_name.split(':')
        if len(names) == 2:
            name = names[1]
            pat = './xs:simpleType[@name="%s"]' % (name, )
            objs = xpath_find(root, pat)
            if objs:
                obj = objs[0]
    return obj


def xpath_find(node, pat):
    """A helper function for using xpath"""
    namespaces = get_fixed_schema_nsmap(node, prefix='xs')
    #namespaces = {node.prefix: node.nsmap[node.prefix]}
    elements = node.xpath(pat, namespaces=namespaces)
    return elements


def replace_group_defs(def_dict, refs):
    """Copy group definitions and replace the reference."""
    for ref_node in refs:
        name = trim_prefix(ref_node.get('ref'))
        if name is None:
            continue
        def_node = def_dict.get(name)
        namespaces = {def_node.prefix: def_node.nsmap[def_node.prefix]}
        if def_node is not None:
            pattern = './%s:sequence|./%s:choice|./%s:all' % (
                def_node.prefix, def_node.prefix, def_node.prefix, )
            content = def_node.xpath(
                pattern,
                namespaces=namespaces)
            if content:
                content = content[0]
                parent = ref_node.getparent()
                for node in content:
                    if not isinstance(node, etree._Comment):
                        new_node = deepcopy(node)
                        # Copy minOccurs and maxOccurs attributes to new node.
                        value = ref_node.get('minOccurs')
                        if value is not None:
                            new_node.set('minOccurs', value)
                        value = ref_node.get('maxOccurs')
                        if value is not None:
                            new_node.set('maxOccurs', value)
                        ref_node.addprevious(new_node)
                parent.remove(ref_node)


def raise_anon_complextypes(root, rename_data):
    """ Raise each anonymous complexType to top level and give it a name.
    Rename if necessary to prevent duplicates.
    """
    def_names = collect_type_names(root)
    # Find all complexTypes below top level.
    #   Raise them to top level and name them.
    #   Re-name if there is a duplicate (simpleType, complexType, or
    #   previous renamed type).
    #   Change the parent (xs:element) so the "type" attribute refers to
    #   the raised and renamed type.
    #   Collect the new types.
    el = etree.Comment(text="Raised anonymous complexType definitions")
    el.tail = "\n\n"
    root.append(el)
    prefix = 'xs'
    nsmap = get_fixed_schema_nsmap(root, prefix=prefix)
    pattern = './*/*//xs:complexType|./*/*//xs:simpleType'
    annotation_pattern = './xs:annotation'
    element_tag = '{%s}element' % (nsmap[prefix], )
    attribute_tag = '{%s}attribute' % (nsmap[prefix], )
    defs = root.xpath(pattern, namespaces=nsmap)
    for node in defs:
        parent = node.getparent()
        if parent.tag != element_tag and parent.tag != attribute_tag:
            continue
        name = parent.get('name')
        if not name:
            continue
        type_name = '%sType' % (name, )
        if Inner_name_map is None:
            type_name = unique_name(type_name, rename_data)
            rename_data.global_names.add(type_name)
        else:
            type_name = map_inner_name(node, Inner_name_map)
        annotations = parent.xpath(annotation_pattern, namespaces=nsmap)
        for annotation in reversed(annotations):
            type_annotation = deepcopy(annotation)
            node.insert(0, type_annotation)
        def_names.add(type_name)
        parent.set('type', type_name)
        node.set('name', type_name)
        # Move the complexType node to top level.
        root.append(node)


def map_inner_name(node, inner_name_map):
    """Use a user-supplied mapping table to look up a name for this class/type.
    """
    # find the name for the enclosing type definition and
    # the name of the type definition that encloses that.
    node1 = node
    name2 = node1.get('name')
    while name2 is None:
        node1 = node1.getparent()
        if node1 is None:
            raise InnerNameMapError('cannot find parent with "name" attribute')
        name2 = node1.get('name')
    node1 = node1.getparent()
    name1 = node1.get('name')
    while name1 is None:
        node1 = node1.getparent()
        if node1 is None:
            raise InnerNameMapError('cannot find parent with "name" attribute')
        name1 = node1.get('name')
    new_name = inner_name_map.get((name1, name2))
    if new_name is None:
        msg1 = '("{}", "{}")'.format(
            name1, name2)
        sys.stderr.write('\n*** error.  Must add entry to inner_name_map:\n')
        sys.stderr.write('\n    {}: "xxxx",\n\n'.format(msg1))
        raise InnerNameMapError('mapping missing for {}'.format(msg1))
    return new_name


def collect_type_names(node):
    """Collect the names of all currently defined types (complexType,
    simpleType, element).
    """
    prefix = node.prefix
    if prefix is not None and prefix.strip():
        pattern = './/%s:complexType|.//%s:simpleType|.//%s:element' % (
            prefix, prefix, prefix)
        # Must make sure that we have a namespace dictionary that does *not*
        # have a key None.
        namespaces = {prefix: node.nsmap[prefix]}
        elements = node.xpath(pattern, namespaces=namespaces)
    else:
        pattern = './/complexType|.//simpleType|.//element'
        elements = node.xpath(pattern)
    names = {
        el.attrib['name'] for el in elements if
        'name' in el.attrib and el.getchildren()
    }
    return names


def unique_name(new_name, rename_data):
    """If necessary, create a new name that is not in def_names."""
    orig_name = new_name
    while True:
        if new_name not in rename_data.global_names:
            break
        rename_data.global_count += 1
        new_name = '{}{}'.format(orig_name, rename_data.global_count)
    return new_name


def trim_prefix(name):
    """Trim off the name space prefix."""
    names = name.split(':')
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return names[1]
    return None


def split_prefix(name):
    """Split a name into (prefix, name).  Return them."""
    name = name.split(':')
    if len(name) == 1:
        prefix = ''
        name = name[0]
    elif len(name) == 2:
        prefix = name[0]
        name = name[1]
    else:
        prefix = ''
        name = ''
    return prefix, name


USAGE_TEXT = __doc__


def usage(parser):
    """Display usage info and exit."""
    parser.print_help()
    sys.exit(1)


def main():
    """A main function for running from the command line"""
    parser = OptionParser(USAGE_TEXT)
    parser.add_option(
        "-f", "--force", action="store_true",
        dest="force", default=False,
        help="force overwrite without asking")
    parser.add_option(
        "--fix-type-names", action="store",
        dest="fixtypenames", default=None,
        help="Fix up (replace) complex type names.")
    parser.add_option(
        "--no-collect-includes", action="store_true",
        dest="no_collect_includes", default=False,
        help="do not process and insert schemas referenced by "
             "xs:include and xs:import elements")
    parser.add_option(
        "--no-redefine-groups", action="store_true",
        dest="no_redefine_groups", default=False,
        help="do not pre-process and redefine xs:group elements")
    (options, args) = parser.parse_args()
    if len(args) == 2:
        inpath = args[0]
        outpath = args[1]
    elif len(args) == 1:
        inpath = args[0]
        outpath = None
    elif len(args) == 0:
        inpath = None
        outpath = None
    else:
        usage(parser)
    prep_schema(inpath, outpath, options)


if __name__ == "__main__":
    #import pdb; pdb.set_trace()
    #import ipdb; ipdb.set_trace()
    main()
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
