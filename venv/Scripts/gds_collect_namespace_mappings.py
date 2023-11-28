#!C:\Users\Muhammet\IzibizTestEntegration\venv\Scripts\python.exe

"""
usage: collect_namespace_mappings.py [-h] [-o OUTFILE] [-f] [-s] [-v] [-n]
        [schema_file_names [schema_file_names ...]]

synopsis:
  Collect a mapping of target namespaces to simpleType
  and complexType definitions.

positional arguments:
  schema_file_names     One or more XML schema file names

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        Output file name. Default -- write to stdout.
  -f, --force           Overwrite output file without asking.
  -s, --silence         Silence -- do not print warning messages.
  -v, --verbose         Print messages during actions.
  -n, --no-out          Do not write mapping to stdout.

examples:
  python collect_namespace_mappings.py schema1.xsd schema2.xsd
  python collect_namespace_mappings.py -o outfile.txt schema1.xsd schema2.xsd
"""


#
# imports
import sys
import os
import argparse
from lxml import etree
import requests


def dbg_msg(options, msg):
    """Print a message if verbose is on."""
    if options.verbose:
        print(msg)


def fix_nsmap(node, prefix='xsd'):
    nsmap = {}
    if 'xs' in node.nsmap:
        nsmap[prefix] = node.nsmap.get('xs')
    elif 'xsd' in node.nsmap:
        nsmap[prefix] = node.nsmap.get('xsd')
    elif None in nsmap:
        nsmap[prefix] = nsmap.pop.get(None)
    else:
        nsmap[prefix] = 'http://www.w3.org/2001/XMLSchema'
    return nsmap


def map_schema(schema_file_name, mapping, opts, generateds_envir):
    cleanupName = generateds_envir.get('cleanupName')
    try:
        root = None
        if schema_file_name.startswith('http'):
            headers = {
                'User-Agent':
                    "Mozilla/5.0 (X11; 'Linux x86_64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) ",
            }
            data = requests.get(schema_file_name, headers=headers).content
            root = etree.fromstring(data)
        else:
            doc = etree.parse(schema_file_name)
            root = doc.getroot()
        nsmap = fix_nsmap(root)
        namespace = root.attrib.get('targetNamespace')
        if namespace:
            def_elements = root.xpath('./xsd:simpleType', namespaces=nsmap)
            def_names = [
                node.attrib.get('name') for node in def_elements]
            st_descriptions = [
                (name, schema_file_name, 'ST') for name in def_names]
            def_elements = root.xpath('./xsd:complexType', namespaces=nsmap)
            def_names = [
                cleanupName(node.attrib.get('name')) for node in def_elements]
            ct_descriptions = [
                (name, schema_file_name, 'CT') for name in def_names]
            if namespace not in mapping:
                mapping[namespace] = []
            mapping[namespace].extend(st_descriptions)
            mapping[namespace].extend(ct_descriptions)
    except OSError:
        if not opts.silence:
            print('cannot access "{}": No such file or location'.format(
                schema_file_name))


def show_mapping(outfile, mapping):
    for k, v in mapping.items():
        outfile.write('{}\n'.format(k))
        for name in v:
            outfile.write('    {}\n'.format(name))


def make_output_file(opts):
    if 'outfile' in opts and opts.outfile != "":
        if os.path.exists(opts.outfile) and not opts.force:
            sys.exit('File {} exists.  Use --force to overwrite.'.format(
                opts.outfile))
        else:
            outfile = open(opts.outfile, 'w')
    else:
        outfile = sys.stdout
    return outfile


def create_mapping(opts, generateds_envir):
    """Create a mapping of namespaces to simpleType defs and write it out.

    To call this function from Python, create and pass in an instance
    `argparse.Namespace`.  Use `--verbose` to see an example.

    Args:
        opts (argparse.Namespace) -- command line arguments and options.
    """
    if opts.verbose:
        print(opts)
    mapping = {}
    schema_file_names = opts.schema_file_names
    for schema_file_name in schema_file_names:
        map_schema(schema_file_name, mapping, opts, generateds_envir)
    if not opts.no_out:
        try:
            outfile = make_output_file(opts)
            show_mapping(outfile, mapping)
        finally:
            if outfile is not sys.stdout:
                if opts.verbose:
                    print('closing outfile')
                outfile.close()
    return mapping


def main():
    description = """\
synopsis:
  Collect a mapping of target namespaces to simpleType
  and complexType definitions.
"""
    epilog = """\
examples:
  python collect_namespace_mappings.py schema1.xsd schema2.xsd
  python collect_namespace_mappings.py -o outfile.txt schema1.xsd schema2.xsd
"""
    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "schema_file_names",
        nargs="*",
        help="One or more XML schema file names"
    )
    parser.add_argument(
        "-o", "--outfile",
        type=str,
        default="",
        help="Output file name.  Default -- write to stdout.",
    )
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Overwrite output file without asking.",
    )
    parser.add_argument(
        "-s", "--silence",
        action="store_true",
        help="Silence -- do not print warning messages.",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print messages during actions.",
    )
    parser.add_argument(
        "-n", "--no-out",
        action="store_true",
        help="Do not write mapping to stdout.",
    )
    options = parser.parse_args()
    create_mapping(options)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    #import ipdb; ipdb.set_trace()
    main()
