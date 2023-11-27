from dataclasses import dataclass, field
from typing import List, Optional
from generated.common.ubl_extension_content_data_type_2_1 import ExtensionContentType
from generated.common.ubl_unqualified_data_types_2_1 import (
    CodeType,
    IdentifierType,
    TextType,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionAgencyIdtype(IdentifierType):
    class Meta:
        name = "ExtensionAgencyIDType"


@dataclass
class ExtensionAgencyNameType(TextType):
    pass


@dataclass
class ExtensionAgencyUritype(IdentifierType):
    class Meta:
        name = "ExtensionAgencyURIType"


@dataclass
class ExtensionContent(ExtensionContentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionReasonCodeType(CodeType):
    pass


@dataclass
class ExtensionReasonType(TextType):
    pass


@dataclass
class ExtensionUritype(IdentifierType):
    class Meta:
        name = "ExtensionURIType"


@dataclass
class ExtensionVersionIdtype(IdentifierType):
    class Meta:
        name = "ExtensionVersionIDType"


@dataclass
class ExtensionAgencyId(ExtensionAgencyIdtype):
    class Meta:
        name = "ExtensionAgencyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionAgencyName(ExtensionAgencyNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionAgencyUri(ExtensionAgencyUritype):
    class Meta:
        name = "ExtensionAgencyURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionReason(ExtensionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionReasonCode(ExtensionReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionUri(ExtensionUritype):
    class Meta:
        name = "ExtensionURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionVersionId(ExtensionVersionIdtype):
    class Meta:
        name = "ExtensionVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class UblextensionType:
    """
    A single extension for private use.

    :ivar extension_content: The definition of the extension content.
    """
    class Meta:
        name = "UBLExtensionType"

    extension_content: Optional[ExtensionContent] = field(
        default=None,
        metadata={
            "name": "ExtensionContent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
            "required": True,
        }
    )


@dataclass
class Ublextension(UblextensionType):
    """
    A single extension for private use.
    """
    class Meta:
        name = "UBLExtension"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class UblextensionsType:
    """
    A container for all extensions present in the document.

    :ivar ublextension: A single extension for private use.
    """
    class Meta:
        name = "UBLExtensionsType"

    ublextension: List[Ublextension] = field(
        default_factory=list,
        metadata={
            "name": "UBLExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class Ublextensions(UblextensionsType):
    """
    A container for all extensions present in the document.
    """
    class Meta:
        name = "UBLExtensions"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
