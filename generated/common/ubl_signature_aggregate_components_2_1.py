from dataclasses import dataclass, field
from typing import Optional
from generated.common.ubl_common_basic_components_2_1 import Id
from generated.common.ubl_signature_basic_components_2_1 import ReferencedSignatureId
from generated.common.ubl_xmldsig_core_schema_2_1 import Signature

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2"


@dataclass
class SignatureInformationType:
    """
    :ivar id:
    :ivar referenced_signature_id:
    :ivar signature: This is a single digital signature as defined by
        the W3C specification.
    """
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    referenced_signature_id: Optional[ReferencedSignatureId] = field(
        default=None,
        metadata={
            "name": "ReferencedSignatureID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class SignatureInformation(SignatureInformationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2"
