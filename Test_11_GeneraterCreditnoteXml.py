from Utilities import Tools
from generated.common import AdditionalDocumentReference, Attachment, EmbeddedDocumentBinaryObject
from generated.common.ubl_common_aggregate_components_2_1 import Signature, SignatoryParty, \
    PostalAddress, Country, DigitalSignatureAttachment, ExternalReference, AccountingSupplierParty, Party, \
    PartyIdentification, PartyName, PartyTaxScheme, TaxScheme, Contact, AccountingCustomerParty, TaxTotal, \
    TaxSubtotal, TaxCategory, LegalMonetaryTotal, Item, Price, PaymentMeans, PayeeFinancialAccount, \
    FinancialInstitutionBranch, FinancialInstitution, Delivery, CreditNoteLine
from generated.common.ubl_common_basic_components_2_1 import PriceAmount, TaxAmount, Id, TaxableAmount, \
     LineExtensionAmount, TaxExclusiveAmount, TaxInclusiveAmount, PayableAmount, CreditedQuantity
from generated.maindoc import CreditNote
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from datetime import datetime

import uuid


class CreateXmlForCreditNote():

    parser = XmlParser()
    creditNote = CreditNote()
    tools = Tools()

    def create_creditnote(self):

        self.creditNote.ublversion_id = "2.1"
        self.creditNote.customization_id = "TR1.2"
        self.creditNote.profile_id = "EARSIVBELGE"
        self.creditNote.id = f"MUH{datetime.now().today().year}000018182"
        self.creditNote.copy_indicator = False
        self.creditNote.uuid = str(uuid.uuid4())
        self.creditNote.issue_date = self.tools.get_date()
        self.creditNote.issue_time = self.tools.get_time()
        self.creditNote.credit_note_type_code = "MUSTAHSILMAKBUZ"
        self.creditNote.note = ""
        self.creditNote.document_currency_code = "TRY"
        self.creditNote.line_count_numeric = 1

        additionalDocumentReference = AdditionalDocumentReference()
        additionalDocumentReference.document_type = "KAGIT"
        additionalDocumentReference.document_type_code = "SendingType"
        additionalDocumentReference.id = 1
        additionalDocumentReference.issue_date = self.tools.get_date()

        additionalDocumentReference_1 = AdditionalDocumentReference()
        additionalDocumentReference_1.document_type = "XSLT"
        additionalDocumentReference_1.id = str(uuid.uuid4())
        additionalDocumentReference_1.issue_date = self.tools.get_date()

        attachment = Attachment()
        embeddedDocumentBinaryObject = EmbeddedDocumentBinaryObject()
        embeddedDocumentBinaryObject.character_set_code = "UTF-8"
        embeddedDocumentBinaryObject.encoding_code = "Base64"
        embeddedDocumentBinaryObject.filename = "270ad44f-2b32-49fe-b415-3978aaffe804.xslt"
        embeddedDocumentBinaryObject.mime_code = "application/xml"
        file = open("Required_Files/XML_CONTENTS/creditNote_template_context.txt", 'r')
        data = file.read()
        embeddedDocumentBinaryObject.value = data
        attachment.embedded_document_binary_object = embeddedDocumentBinaryObject
        additionalDocumentReference.attachment = attachment

        self.creditNote.additional_document_reference = additionalDocumentReference_1,additionalDocumentReference

        signature = Signature()
        id = Id()
        id.scheme_id = "VKN_TCKN"
        id.value = 4840847211
        signature.id = id

        signatoryParty = SignatoryParty()
        partyIdentification = PartyIdentification()
        id_1 = Id()
        id_1.scheme_id = "VKN"
        id_1.value = 4840847211
        partyIdentification.id = id_1
        signatoryParty.party_identification = partyIdentification

        postalAddress = PostalAddress()
        postalAddress.street_name = "Yıldız Teknik Üniversitesi Teknoloji Geliştirme Bölgesi D2 Blok Z07"
        postalAddress.building_name = ""
        postalAddress.building_number = "C-1 Blok"
        postalAddress.city_subdivision_name = "MALTEPE"
        postalAddress.city_name = "ISTANBUL"
        postalAddress.postal_zone = "34220"
        postalAddress.region = "MALTEPE"
        country = Country()
        country.name = "TR"
        postalAddress.country = country

        signatoryParty.postal_address = postalAddress
        signature.signatory_party = signatoryParty

        digitalSignatureAttachment = DigitalSignatureAttachment()
        externalReferance = ExternalReference()
        externalReferance.uri = "#Signature_MUH2023000000182"
        digitalSignatureAttachment.external_reference = externalReferance
        signature.digital_signature_attachment = digitalSignatureAttachment
        self.creditNote.signature = signature

        accountingSupplierParty = AccountingSupplierParty()
        party = Party()
        party.website_uri = "www.izibiz.com.tr"

        partyIdentification = PartyIdentification()
        id_2 = Id()
        id_2.scheme_id = "VKN"
        id_2.value = 4840847211
        partyIdentification.id = id_2

        partyIdentification_1 = PartyIdentification()
        id_3 = Id()
        id_3.scheme_id = "MERSISNO"
        id_3.value = "0484084721100010"
        partyIdentification_1.id = id_3

        partyIdentification_2 = PartyIdentification()
        id_4 = Id()
        id_4.scheme_id = "TICARETSICILNO"
        id_4.value = "873195"
        partyIdentification_2.id = id_4

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
        contact.telefax = ""
        contact.electronic_mail = "operasyonekibi@izibiz.com.tr"
        party.contact = contact

        accountingSupplierParty.party = party
        self.creditNote.accounting_supplier_party = accountingSupplierParty

        accountingCustomerParty = AccountingCustomerParty()
        party_1 = Party()
        partyIdentification = PartyIdentification()
        id_5 = Id()
        id_5.scheme_id = "VKN"
        id_5.value = "1111111111"
        partyIdentification.id = id_5
        party_1.party_identification = partyIdentification

        partyName = PartyName()
        partyName.name = "Muhammet CÖMERT"
        party_1.party_name = partyName

        postalAddress_2 = PostalAddress()
        postalAddress_2.street_name = "Cumhuriyet Caddesi"
        postalAddress_2.building_name = " "
        postalAddress_2.building_number = "10"
        postalAddress_2.city_subdivision_name = "MALTEPE"
        postalAddress_2.city_name = "MALTEPE"
        postalAddress_2.postal_zone = ""
        postalAddress_2.region = ""
        country_2 = Country()
        country_2.name = "Türkiye"
        postalAddress_2.country = country_2
        party_1.postal_address = postalAddress_2

        partyTaxScheme = PartyTaxScheme()
        taxScheme = TaxScheme()
        taxScheme.name = "KÜÇÜKYALI"
        partyTaxScheme.tax_scheme = taxScheme
        party_1.party_tax_scheme = partyTaxScheme

        contact_1 = Contact()
        contact_1.telephone = "(111) 111-1111"
        contact_1.telefax = ""
        contact_1.electronic_mail = "analiz@izibiz.com.tr"
        party_1.contact = contact_1

        accountingCustomerParty.party = party_1
        self.creditNote.accounting_customer_party = accountingCustomerParty

        delivery = Delivery()
        delivery.actual_delivery_date = "2023-10-05+03:00"
        self.creditNote.delivery = delivery

        paymentMeans = PaymentMeans()
        paymentMeans.payment_means_code = "46"
        payeeFinancialAccount = PayeeFinancialAccount()
        payeeFinancialAccount.id = "TR111111111111111111111111"
        payeeFinancialAccount.currency_code = "TRY"
        financialInstitutionBranch = FinancialInstitutionBranch()
        financialInstitutionBranch.name = "X ŞUBESİ"
        financialInstitution = FinancialInstitution()
        financialInstitution.name = "X BANKASI"
        financialInstitutionBranch.financial_institution = financialInstitution
        payeeFinancialAccount.financial_institution_branch = financialInstitutionBranch
        paymentMeans.payee_financial_account = payeeFinancialAccount
        self.creditNote.payment_means = paymentMeans

        taxTotal = TaxTotal()
        taxAmount = TaxAmount()
        taxAmount.currency_id = "TRY"
        taxAmount.value = 11.00
        taxTotal.tax_amount = taxAmount

        taxSubtotal = TaxSubtotal()
        taxableAmount = TaxableAmount()
        taxableAmount.currency_id = "TRY"
        taxableAmount.value = 110.00
        taxSubtotal.taxable_amount = taxableAmount
        taxAmount_1 = TaxAmount()
        taxAmount_1.currency_id = "TRY"
        taxAmount_1.value = 11.00
        taxSubtotal.tax_amount = taxAmount_1
        taxSubtotal.calculation_sequence_numeric = "1"
        taxSubtotal.percent = "10.00"
        taxCategory = TaxCategory()
        taxScheme_2 = TaxScheme()
        taxScheme_2.name = "GV. STOPAJI"
        taxScheme_2.tax_type_code = "0003"
        taxCategory.tax_scheme = taxScheme_2
        taxSubtotal.tax_category = taxCategory
        taxTotal.tax_subtotal = taxSubtotal
        self.creditNote.tax_total = taxTotal

        legalMonetaryTotal = LegalMonetaryTotal()
        lineExtensionAmount = LineExtensionAmount()
        lineExtensionAmount.currency_id = "TRY"
        lineExtensionAmount.value = 110.00
        taxExclusiveAmount = TaxExclusiveAmount()
        taxExclusiveAmount.currency_id = "TRY"
        taxExclusiveAmount.value = 99.00
        taxInclusiveAmount = TaxInclusiveAmount()
        taxInclusiveAmount.currency_id = "TRY"
        taxInclusiveAmount.value = 110.00
        payableAmount = PayableAmount()
        payableAmount.currency_id = "TRY"
        payableAmount.value = 99.00
        legalMonetaryTotal.line_extension_amount = lineExtensionAmount
        legalMonetaryTotal.tax_exclusive_amount = taxExclusiveAmount
        legalMonetaryTotal.tax_inclusive_amount = taxInclusiveAmount
        legalMonetaryTotal.payable_amount = payableAmount

        self.creditNote.legal_monetary_total = legalMonetaryTotal

        creditNoteLine = CreditNoteLine()
        creditNoteLine.id = "1"

        creditedQuantity = CreditedQuantity()
        creditedQuantity.unit_code = "C62"
        creditedQuantity.value = 11
        creditNoteLine.credited_quantity = creditedQuantity

        lineExtensionAmount = LineExtensionAmount()
        lineExtensionAmount.currency_id = "TRY"
        lineExtensionAmount.value = 110
        creditNoteLine.line_extension_amount = lineExtensionAmount

        taxTotal_2 = TaxTotal()
        taxAmount_2 = TaxAmount()
        taxAmount_2.currency_id = "TRY"
        taxAmount_2.value = 11.00
        taxTotal_2.tax_amount = taxAmount_2

        taxSubtotal_1 = TaxSubtotal()
        taxableAmount_1 = TaxableAmount()
        taxableAmount_1.currency_id = "TRY"
        taxableAmount_1.value = 110.00
        taxSubtotal_1.taxable_amount = taxableAmount_1

        taxAmount_3 = TaxAmount()
        taxAmount_3.currency_id = "TRY"
        taxAmount_3.value = 11.00
        taxSubtotal_1.tax_amount = taxAmount_3
        taxSubtotal_1.calculation_sequence_numeric = 1
        taxSubtotal_1.percent = 10

        taxCategory_1 = TaxCategory()
        taxScheme_3 = TaxScheme()
        taxScheme_3.name = "GV. STOPAJI"
        taxScheme_3.tax_type_code = "0003"

        taxCategory_1.tax_scheme = taxScheme_3
        taxSubtotal_1.tax_category = taxCategory_1
        taxTotal_2.tax_subtotal = taxSubtotal_1
        creditNoteLine.tax_total = taxTotal_2

        item = Item()
        item.name = "ss"
        creditNoteLine.item = item

        price = Price()

        price_amount = PriceAmount()
        price_amount.value = 10
        price_amount.currency_id = "TRY"
        price.price_amount = price_amount
        creditNoteLine.price = price

        self.creditNote.credit_note_line = creditNoteLine
        #
        serializer = XmlSerializer(config=SerializerConfig(
            pretty_print=True,
            xml_declaration=False,
            ignore_default_attributes=True,
            schema_location="urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2 UBL-CreditNote-2.1.xsd"))

        data = serializer.render(self.creditNote,
                                 ns_map={
                                     "cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
                                     "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
                                     "xsi": "http://www.w3.org/2001/XMLSchema-instance"})
        print(serializer.render(self.creditNote,
                                ns_map={
                                    "cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
                                    "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"}))

        file = open('Files/GENERATED_XML/creditNote_xml.xml', 'w', encoding="utf-8")
        file.write(data)
        file.close()

create_xml = CreateXmlForCreditNote()
create_xml.create_creditnote()









