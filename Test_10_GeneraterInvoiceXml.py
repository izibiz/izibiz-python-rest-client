
from generated.common import AdditionalDocumentReference, Attachment, EmbeddedDocumentBinaryObject
from generated.common.ubl_common_aggregate_components_2_1 import Signature, SignatoryParty, PostalAddress, \
    Country, DigitalSignatureAttachment, ExternalReference, AccountingSupplierParty, Party, \
    PartyIdentification, PartyName, PartyTaxScheme, TaxScheme, Contact, AccountingCustomerParty, TaxTotal, TaxSubtotal, \
    TaxCategory, LegalMonetaryTotal, InvoiceLine, Item, Price, PaymentMeans, PayeeFinancialAccount, \
    FinancialInstitutionBranch, FinancialInstitution, SellersItemIdentification
from generated.common.ubl_common_basic_components_2_1 import PriceAmount, TaxAmount, Id, TaxableAmount, LineExtensionAmount, \
    TaxExclusiveAmount, TaxInclusiveAmount, AllowanceTotalAmount, ChargeTotalAmount, PayableAmount, InvoicedQuantity
from generated.maindoc.ubl_invoice_2_1 import Invoice
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from Utilities import Tools


import uuid
from datetime import datetime

class CreateXmlForInvoice():

    parser = XmlParser()
    invoice = Invoice()
    tools = Tools()

    def create_invoice(self):

        self.invoice.ublversion_id = "2.1"
        self.invoice.customization_id = "TR1.2"
        self.invoice.profile_id = "TICARIFATURA"
        self.invoice.id = f"MUH{datetime.now().today().year}000018182"
        self.invoice.copy_indicator = False
        self.invoice.uuid = str(uuid.uuid4())
        self.invoice.issue_date = self.tools.get_date()
        self.invoice.issue_time = self.tools.get_time()
        self.invoice.invoice_type_code = "SATIS"
        self.invoice.document_currency_code = "TRY"
        self.invoice.line_count_numeric = 1

        additionalDocumentReference = AdditionalDocumentReference()
        additionalDocumentReference.document_type = "XSLT"
        additionalDocumentReference.id = str(uuid.uuid4())
        additionalDocumentReference.issue_date = self.tools.get_date()

        attachment = Attachment()
        embeddedDocumentBinaryObject = EmbeddedDocumentBinaryObject()
        embeddedDocumentBinaryObject.character_set_code = "UTF-8"
        embeddedDocumentBinaryObject.encoding_code = "Base64"
        embeddedDocumentBinaryObject.filename = "DMY20231020113229.xslt"
        embeddedDocumentBinaryObject.mime_code = "application/xml"
        file = open("Required_Files/XML_CONTENTS/invoice_template_context.txt", 'r')
        data = file.read()
        embeddedDocumentBinaryObject.value =data
        attachment.embedded_document_binary_object = embeddedDocumentBinaryObject
        additionalDocumentReference.attachment = attachment
        self.invoice.additional_document_reference = additionalDocumentReference

        signature = Signature()
        id_1 =Id()
        id_1.scheme_id ="VKN_TCKN"
        id_1.value = 4840847211
        signature.id = id_1

        signatoryParty = SignatoryParty()
        partyIdentification = PartyIdentification()
        id_2 = Id()
        id_2.scheme_id = "VKN"
        id_2.value = 4840847211
        partyIdentification.id = id_2
        signatoryParty.party_identification = partyIdentification

        postalAddress = PostalAddress()
        postalAddress.street_name = "Altayçeşme Mh. Çamlı Sk. DAP Royal Center"
        postalAddress.building_name = ""
        postalAddress.building_number = "A Blok Kat15"
        postalAddress.city_subdivision_name = "MALTEPE"
        postalAddress.city_name = "ISTANBUL"
        postalAddress.postal_zone = "34843"
        postalAddress.region = "MALTEPE"
        country = Country()
        country.name = "TR"
        postalAddress.country = country

        signatoryParty.postal_address = postalAddress
        signature.signatory_party = signatoryParty


        digitalSignatureAttachment = DigitalSignatureAttachment()
        externalReferance = ExternalReference()
        externalReferance.uri = "#Signature_IYU2023000000182"
        digitalSignatureAttachment.external_reference = externalReferance
        signature.digital_signature_attachment = digitalSignatureAttachment
        self.invoice.signature = signature

        accountingSupplierParty = AccountingSupplierParty()
        party = Party()
        party.website_uri = "www.izibiz.com.tr"

        partyIdentification = PartyIdentification()
        id_3 = Id()
        id_3.scheme_id = "VKN"
        id_3.value =4840847211
        partyIdentification.id = id_3

        partyIdentification_1 = PartyIdentification()
        id_4 = Id()
        id_4.scheme_id = "MERSISNO"
        id_4.value = "0484084721100010"
        partyIdentification_1.id = id_4

        partyIdentification_2 = PartyIdentification()
        id_5 = Id()
        id_5.scheme_id = "TICARETSICILNO"
        id_5.value = "873195"
        partyIdentification_2.id = id_5

        party.party_identification = partyIdentification, partyIdentification_1, partyIdentification_2

        partyName = PartyName()
        partyName.name = "İZİBİZ BİLİŞİM TEKNOLOJİLERİ ANONİM ŞİRKETİ"
        party.party_name = partyName

        postalAddress_1 = PostalAddress()
        postalAddress_1.street_name = "Yıldız Teknik Üniversitesi Teknoloji Geliştirme Bölgesi D2 Blok Z07"
        postalAddress_1.building_name = ""
        postalAddress_1.building_number = "C-1 Blok"
        postalAddress_1.city_subdivision_name = "MALTEPE"
        postalAddress_1.city_name = "ISTANBUL"
        postalAddress_1.postal_zone = "34220"
        postalAddress_1.region = "MALTEPE"
        country_1 = Country()
        country_1.name = "TR"
        postalAddress_1.country = country_1
        party.postal_address = postalAddress_1

        partyTaxScheme = PartyTaxScheme()
        taxScheme = TaxScheme()
        taxScheme.name = "KÜÇÜKYALI655"
        partyTaxScheme.tax_scheme = taxScheme
        party.party_tax_scheme = partyTaxScheme

        contact = Contact()
        contact.telephone = "(850) 811 11 99"
        contact.telefax =""
        contact.electronic_mail = "operasyonekibi@izibiz.com.tr"
        party.contact = contact

        accountingSupplierParty.party = party
        self.invoice.accounting_supplier_party = accountingSupplierParty


        accountingCustomerParty = AccountingCustomerParty()
        party_1 = Party()
        partyIdentification = PartyIdentification()
        id_5 = Id()
        id_5.scheme_id = "VKN"
        id_5.value = "4840847211"
        partyIdentification.id = id_5
        party_1.party_identification = partyIdentification

        partyName = PartyName()
        partyName.name = "Muhammet CÖMERT"
        party_1.party_name = partyName
        postalAddress_3 = PostalAddress()
        postalAddress_3.street_name = "Cumhuriyet Caddesi"
        postalAddress_3.building_name = ""
        postalAddress_3.building_number = "10"
        postalAddress_3.city_subdivision_name = "MALTEPE"
        postalAddress_3.city_name = "İSTANBUL"
        postalAddress_3.postal_zone = ""
        postalAddress_3.region = ""
        country_3 = Country()
        country_3.name = "Türkiye"
        postalAddress_3.country = country_3
        party_1.postal_address = postalAddress_3

        partyTaxScheme_1 = PartyTaxScheme()
        taxScheme_1 = TaxScheme()
        taxScheme_1.name = "KÜÇÜKYALI"
        partyTaxScheme_1.tax_scheme = taxScheme_1
        party_1.party_tax_scheme = partyTaxScheme_1

        contact = Contact()
        contact.telephone = "(111) 111-1111"
        contact.telefax = ""
        contact.electronic_mail = "analiz@izibiz.com.tr"
        party_1.contact = contact

        accountingCustomerParty.party = party_1
        self.invoice.accounting_customer_party = accountingCustomerParty

        paymentMeans = PaymentMeans()
        paymentMeans.payment_means_code = "46"
        payeeFinancialAccount = PayeeFinancialAccount()
        payeeFinancialAccount.id = "TR111111111111111111111111"
        payeeFinancialAccount.currency_code ="TRY"
        financialInstitutionBranch = FinancialInstitutionBranch()
        financialInstitutionBranch.name ="X ŞUBESİ"
        financialInstitution = FinancialInstitution()
        financialInstitution.name ="X BANKASI"
        financialInstitutionBranch.financial_institution = financialInstitution
        payeeFinancialAccount.financial_institution_branch = financialInstitutionBranch
        paymentMeans.payee_financial_account = payeeFinancialAccount
        self.invoice.payment_means = paymentMeans


        taxTotal = TaxTotal()
        taxAmount =TaxAmount()
        taxAmount.currency_id ="TRY"
        taxAmount.value = 5.00
        taxTotal.tax_amount = taxAmount

        taxSubtotal = TaxSubtotal()
        taxableAmount = TaxableAmount()
        taxableAmount.currency_id ="TRY"
        taxableAmount.value = 25.00
        taxSubtotal.taxable_amount = taxableAmount
        taxAmount_1 = TaxAmount()
        taxAmount_1.currency_id = "TRY"
        taxAmount_1.value = 5.00
        taxSubtotal.tax_amount = taxAmount_1
        taxSubtotal.calculation_sequence_numeric = "1"
        taxSubtotal.percent = "20.00"
        taxCategory = TaxCategory()
        taxScheme_2 = TaxScheme()
        taxScheme_2.name = "KDV"
        taxScheme_2.tax_type_code = "0015"
        taxCategory.tax_scheme = taxScheme_2
        taxSubtotal.tax_category = taxCategory
        taxTotal.tax_subtotal = taxSubtotal

        self.invoice.tax_total = taxTotal

        legalMonetaryTotal = LegalMonetaryTotal()
        lineExtensionAmount = LineExtensionAmount()
        lineExtensionAmount.currency_id = "TRY"
        lineExtensionAmount.value = 25.00
        taxExclusiveAmount = TaxExclusiveAmount()
        taxExclusiveAmount.currency_id = "TRY"
        taxExclusiveAmount.value = 25.00
        taxInclusiveAmount = TaxInclusiveAmount()
        taxInclusiveAmount.currency_id = "TRY"
        taxInclusiveAmount.value = 30.00
        allowanceTotalAmount = AllowanceTotalAmount()
        allowanceTotalAmount.currency_id = "TRY"
        allowanceTotalAmount.value = 0.00
        chargeTotalAmount = ChargeTotalAmount()
        chargeTotalAmount.currency_id = "TRY"
        chargeTotalAmount.value = 0.00
        payableAmount = PayableAmount()
        payableAmount.currency_id = "TRY"
        payableAmount.value = 30.00
        legalMonetaryTotal.line_extension_amount = lineExtensionAmount
        legalMonetaryTotal.tax_exclusive_amount = taxExclusiveAmount
        legalMonetaryTotal.tax_inclusive_amount = taxInclusiveAmount
        legalMonetaryTotal.allowance_total_amount = allowanceTotalAmount
        legalMonetaryTotal.charge_total_amount = chargeTotalAmount
        legalMonetaryTotal.payable_amount = payableAmount

        self.invoice.legal_monetary_total = legalMonetaryTotal

        invoiceLine = InvoiceLine()
        invoiceLine.id = "1"
        invoiceLine.note = ""
        invoicedQuantity = InvoicedQuantity()
        invoicedQuantity.unit_code ="C62"
        invoicedQuantity.value = 5
        invoiceLine.invoiced_quantity = invoicedQuantity
        lineExtensionAmount =LineExtensionAmount()
        lineExtensionAmount.currency_id ="TRY"
        lineExtensionAmount.value = 25.00
        invoiceLine.line_extension_amount = lineExtensionAmount

        taxTotal_2 = TaxTotal()
        taxAmount_2 = TaxAmount()
        taxAmount_2.currency_id = "TRY"
        taxAmount_2.value = 5.00
        taxTotal_2.tax_amount = taxAmount_2

        taxSubtotal_1 = TaxSubtotal()
        taxableAmount_1 = TaxableAmount()
        taxableAmount_1.currency_id = "TRY"
        taxableAmount_1.value = 25.00
        taxSubtotal_1.taxable_amount = taxableAmount_1

        taxAmount_1 = TaxAmount()
        taxAmount_1.currency_id = "TRY"
        taxAmount_1.value = 5.00
        taxSubtotal_1.tax_amount = taxAmount_1
        taxSubtotal_1.calculation_sequence_numeric = "1"
        taxSubtotal_1.percent = "20.00"

        taxCategory_1 = TaxCategory()
        taxScheme_2 = TaxScheme()
        taxScheme_2.name = "KDV"
        taxScheme_2.tax_type_code = "0015"
        taxCategory_1.tax_scheme = taxScheme_2
        taxSubtotal_1.tax_category = taxCategory_1
        taxTotal_2.tax_subtotal = taxSubtotal_1
        invoiceLine.tax_total = taxTotal_2


        item = Item()
        item.name = "ddd"
        sellersItemIdentification = SellersItemIdentification()
        sellersItemIdentification.id = "01"
        item.sellers_item_identification = sellersItemIdentification
        invoiceLine.item = item

        price = Price()
        price_amount = PriceAmount()
        price_amount.value = 123.23
        price_amount.currency_id = "TRY"
        price.price_amount = price_amount
        invoiceLine.price = price

        self.invoice.invoice_line = invoiceLine

        serializer = XmlSerializer(config=SerializerConfig(
            pretty_print=True,
            xml_declaration=True,
            ignore_default_attributes=True,
            schema_location="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2 UBL-Invoice-2.1.xsd"

        ))

        data = serializer.render(self.invoice,
                                 ns_map={"cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
                                         "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
                                         "xsi": "http://www.w3.org/2001/XMLSchema-instance"})
        print(serializer.render(self.invoice,
                                ns_map={"cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
                                        "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"}))

        file = open('Files/GENERATED_XML/invoice_xml.xml', 'w', encoding="utf-8")
        file.write(data)
        file.close()


create_xml = CreateXmlForInvoice()
create_xml.create_invoice()
