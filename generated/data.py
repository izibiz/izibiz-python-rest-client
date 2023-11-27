from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"


@dataclass
class InvoiceType:
    ublextensions: Optional[str] = field(
        default=None,
        metadata={
            "name": "UBLExtensions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
            "required": True,
        }
    )
    ublversion_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UBLVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    customization_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomizationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    copy_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    issue_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    invoice_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    tax_currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    pricing_currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricingCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_alternative_currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentAlternativeCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_count_numeric: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineCountNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    invoice_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoicePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    order_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    billing_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    despatch_document_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DespatchDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    receipt_document_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ReceiptDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    originator_document_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OriginatorDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contract_document_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ContractDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    additional_document_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    signature: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )
    accounting_supplier_party: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountingSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    accounting_customer_party: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountingCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    buyer_customer_party: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    seller_supplier_party: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_representative_party: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxRepresentativeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_means: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_terms: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_exchange_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pricing_exchange_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricingExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_exchange_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_alternative_exchange_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentAlternativeExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_total: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )
    withholding_tax_total: List[str] = field(
        default_factory=list,
        metadata={
            "name": "WithholdingTaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    legal_monetary_total: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegalMonetaryTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    invoice_line: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class Invoice(InvoiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
