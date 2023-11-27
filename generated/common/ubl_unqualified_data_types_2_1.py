from dataclasses import dataclass, field
from typing import Optional
from generated.common.ccts_cct_schema_module_2_1 import (
    AmountType as CctsCctSchemaModule21AmountType,
    BinaryObjectType as CctsCctSchemaModule21BinaryObjectType,
    CodeType as CctsCctSchemaModule21CodeType,
    IdentifierType as CctsCctSchemaModule21IdentifierType,
    MeasureType as CctsCctSchemaModule21MeasureType,
    NumericType as CctsCctSchemaModule21NumericType,
    QuantityType as CctsCctSchemaModule21QuantityType,
    TextType as CctsCctSchemaModule21TextType,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2"


@dataclass
class AmountType(CctsCctSchemaModule21AmountType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000001
    </ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Amount.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">A number of monetary units specified using a given unit of currency.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Amount</ns1:RepresentationTermName>

    :ivar currency_id: <ns1:UniqueID
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">UNDT000001-SC2</ns1:UniqueID>
        <ns1:CategoryCode
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">SC</ns1:CategoryCode>
        <ns1:DictionaryEntryName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Amount.
        Currency. Identifier</ns1:DictionaryEntryName> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">The currency
        of the amount.</ns1:Definition> <ns1:ObjectClass
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Amount
        Currency</ns1:ObjectClass> <ns1:PropertyTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Identification</ns1:PropertyTermName>
        <ns1:RepresentationTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Identifier</ns1:RepresentationTermName>
        <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">string</ns1:PrimitiveType>
        <ns1:UsageRule
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Reference
        UNECE Rec 9, using 3-letter alphabetic codes.</ns1:UsageRule>
    """
    currency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BinaryObjectType(CctsCctSchemaModule21BinaryObjectType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000002
    </ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Binary Object.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">A set of finite-length sequences of binary octets.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Binary Object</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">binary</ns1:PrimitiveType>

    :ivar mime_code: <ns1:UniqueID
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">UNDT000002-SC3</ns1:UniqueID>
        <ns1:CategoryCode
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">SC</ns1:CategoryCode>
        <ns1:DictionaryEntryName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Binary Object.
        Mime. Code</ns1:DictionaryEntryName> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">The mime type
        of the binary object.</ns1:Definition> <ns1:ObjectClass
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Binary
        Object</ns1:ObjectClass> <ns1:PropertyTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Mime</ns1:PropertyTermName>
        <ns1:RepresentationTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Code</ns1:RepresentationTermName>
        <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">string</ns1:PrimitiveType>
    """
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CodeType(CctsCctSchemaModule21CodeType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000007
    </ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Code.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">A character string (letters, figures, or symbols) that for brevity and/or language independence may be used to represent or replace a definitive value or text of an attribute, together with relevant supplementary information.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Code</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">string</ns1:PrimitiveType>
    <ns1:UsageRule xmlns:ns1="urn:un:unece:uncefact:documentation:2">Other supplementary components in the CCT are captured as part of the token and name for the schema module containing the code list and thus, are not declared as attributes. </ns1:UsageRule>
    """


@dataclass
class GraphicType(CctsCctSchemaModule21BinaryObjectType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000003
    </ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Graphic.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">A diagram, graph, mathematical curve, or similar representation.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Graphic</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">binary</ns1:PrimitiveType>

    :ivar mime_code: <ns1:UniqueID
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">UNDT000003-SC3</ns1:UniqueID>
        <ns1:CategoryCode
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">SC</ns1:CategoryCode>
        <ns1:DictionaryEntryName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Graphic. Mime.
        Code</ns1:DictionaryEntryName> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">The mime type
        of the graphic object.</ns1:Definition> <ns1:ObjectClass
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Graphic</ns1:ObjectClass>
        <ns1:PropertyTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Mime</ns1:PropertyTermName>
        <ns1:RepresentationTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Code</ns1:RepresentationTermName>
        <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">normalizedString</ns1:PrimitiveType>
    """
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class IdentifierType(CctsCctSchemaModule21IdentifierType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000001
    1</ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Identifier.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">A character string to identify and uniquely distinguish one instance of an object in an identification scheme from all other objects in the same scheme, together with relevant supplementary information.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Identifier</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">string</ns1:PrimitiveType>
    <ns1:UsageRule xmlns:ns1="urn:un:unece:uncefact:documentation:2">Other supplementary components in the CCT are captured as part of the token and name for the schema module containing the identifier list and thus, are not declared as attributes. </ns1:UsageRule>
    """


@dataclass
class MeasureType(CctsCctSchemaModule21MeasureType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000001
    3</ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Measure.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">A numeric value determined by measuring an object using a specified unit of measure.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Measure</ns1:RepresentationTermName>
    <ns1:PropertyTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Type</ns1:PropertyTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">decimal</ns1:PrimitiveType>

    :ivar unit_code: <ns1:UniqueID
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">UNDT000013-SC2</ns1:UniqueID>
        <ns1:CategoryCode
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">SC</ns1:CategoryCode>
        <ns1:DictionaryEntryName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Measure. Unit.
        Code</ns1:DictionaryEntryName> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">The type of
        unit of measure.</ns1:Definition> <ns1:ObjectClass
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Measure
        Unit</ns1:ObjectClass> <ns1:PropertyTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Code</ns1:PropertyTermName>
        <ns1:RepresentationTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Code</ns1:RepresentationTermName>
        <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">normalizedString</ns1:PrimitiveType>
        <ns1:UsageRule
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Reference
        UNECE Rec. 20 and X12 355</ns1:UsageRule>
    """
    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class NameType(CctsCctSchemaModule21TextType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000002
    0</ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Name.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">A character string that constitutes the distinctive designation of a person, place, thing or concept.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Name</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">string</ns1:PrimitiveType>
    """


@dataclass
class NumericType(CctsCctSchemaModule21NumericType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000001
    4</ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Numeric.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">Numeric information that is assigned or is determined by calculation, counting, or sequencing. It does not require a unit of quantity or unit of measure.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Numeric</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">string</ns1:PrimitiveType>
    """


@dataclass
class PercentType(CctsCctSchemaModule21NumericType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000001
    6</ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:VersionID
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Percent.

    Type</ns1:DictionaryEntryName>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">Numeric information that is assigned or is determined by calculation, counting, or sequencing and is expressed as a percentage. It does not require a unit of quantity or unit of measure.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Percent</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">string</ns1:PrimitiveType>
    """


@dataclass
class PictureType(CctsCctSchemaModule21BinaryObjectType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000004
    </ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Picture.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">A diagram, graph, mathematical curve, or similar representation.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Picture</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">binary</ns1:PrimitiveType>

    :ivar mime_code: <ns1:UniqueID
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">UNDT000004-SC3</ns1:UniqueID>
        <ns1:CategoryCode
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">SC</ns1:CategoryCode>
        <ns1:DictionaryEntryName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Picture. Mime.
        Code</ns1:DictionaryEntryName> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">The mime type
        of the picture object.</ns1:Definition> <ns1:ObjectClass
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Picture</ns1:ObjectClass>
        <ns1:PropertyTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Mime</ns1:PropertyTermName>
        <ns1:RepresentationTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Code</ns1:RepresentationTermName>
        <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">normalizedString</ns1:PrimitiveType>
    """
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class QuantityType(CctsCctSchemaModule21QuantityType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000001
    8</ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Quantity.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">A counted number of non-monetary units, possibly including a fractional part.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Quantity</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">decimal</ns1:PrimitiveType>
    """


@dataclass
class RateType(CctsCctSchemaModule21NumericType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000001
    7</ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:VersionID
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Rate.

    Type</ns1:DictionaryEntryName>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">A numeric expression of a rate that is assigned or is determined by calculation, counting, or sequencing. It does not require a unit of quantity or unit of measure.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Rate</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">string</ns1:PrimitiveType>
    """


@dataclass
class SoundType(CctsCctSchemaModule21BinaryObjectType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000005
    </ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Sound.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">An audio representation.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Sound</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">binary</ns1:PrimitiveType>

    :ivar mime_code: <ns1:UniqueID
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">UNDT000005-SC3</ns1:UniqueID>
        <ns1:CategoryCode
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">SC</ns1:CategoryCode>
        <ns1:DictionaryEntryName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Sound. Mime.
        Code</ns1:DictionaryEntryName> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">The mime type
        of the sound object.</ns1:Definition> <ns1:ObjectClass
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Sound</ns1:ObjectClass>
        <ns1:PropertyTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Mime</ns1:PropertyTermName>
        <ns1:RepresentationTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Code</ns1:RepresentationTermName>
        <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">normalizedString</ns1:PrimitiveType>
    """
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TextType(CctsCctSchemaModule21TextType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000001
    9</ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Text.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">A character string (i.e. a finite set of characters), generally in the form of words of a language.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Text</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">string</ns1:PrimitiveType>
    """


@dataclass
class ValueType(CctsCctSchemaModule21NumericType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000001
    5</ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:VersionID
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Value.

    Type</ns1:DictionaryEntryName>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">Numeric information that is assigned or is determined by calculation, counting, or sequencing. It does not require a unit of quantity or unit of measure.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Value</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">string</ns1:PrimitiveType>
    """


@dataclass
class VideoType(CctsCctSchemaModule21BinaryObjectType):
    """<ns1:UniqueID xmlns:ns1="urn:un:unece:uncefact:documentation:2">UBLUDT000006
    </ns1:UniqueID> <ns1:CategoryCode
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">UDT</ns1:CategoryCode>
    <ns1:DictionaryEntryName
    xmlns:ns1="urn:un:unece:uncefact:documentation:2">Video.

    Type</ns1:DictionaryEntryName>
    <ns1:VersionID xmlns:ns1="urn:un:unece:uncefact:documentation:2">1.0</ns1:VersionID>
    <ns1:Definition xmlns:ns1="urn:un:unece:uncefact:documentation:2">A video representation.</ns1:Definition>
    <ns1:RepresentationTermName xmlns:ns1="urn:un:unece:uncefact:documentation:2">Video</ns1:RepresentationTermName>
    <ns1:PrimitiveType xmlns:ns1="urn:un:unece:uncefact:documentation:2">binary</ns1:PrimitiveType>

    :ivar mime_code: <ns1:UniqueID
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">UNDT000006-SC3</ns1:UniqueID>
        <ns1:CategoryCode
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">SC</ns1:CategoryCode>
        <ns1:DictionaryEntryName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Video. Mime.
        Code</ns1:DictionaryEntryName> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">The mime type
        of the video object.</ns1:Definition> <ns1:ObjectClass
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Video</ns1:ObjectClass>
        <ns1:PropertyTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Mime</ns1:PropertyTermName>
        <ns1:RepresentationTermName
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">Code</ns1:RepresentationTermName>
        <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:2">normalizedString</ns1:PrimitiveType>
    """
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
            "required": True,
        }
    )
