from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionContentType:
    """
    :ivar other_element: Any element in any namespace other than the UBL
        extension namespace is allowed to be the apex element of an
        extension. Only those elements found in the UBL schemas and in
        the trees of schemas imported in this module are validated. Any
        element for which there is no schema declaration in any of the
        trees of schemas passes validation and is not treated as a
        schema constraint violation.
    """
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
