import json
import requests
import unittest
from Create_Access_Token import CreateAccessToken
from Variables import Variable
from Utilities import Tools


class TestEFaturaGiden(unittest.TestCase, Variable):
    tools = Tools()
    create_access_token = CreateAccessToken()
    access_token = create_access_token.getAccessToken()
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}

    def test_00_einvoice_listing_waiting_for_approve(self):
        """-->> onay bekleyen e fatura listeleme testi."""

        response = requests.get(url=self.BASE_URL_INVOICE_OUTBOX + self.W_FOR_APPROVE, headers=self.HEADERS)

        self.assertIsNotNone(response.json()['data']['contents'])
        self.assertIsNone(response.json()['error'])

        path = "Files/E_Fatura/Giden/efatura_onay_bekleyen_liste.txt"
        contents = response.json()['data']['contents']

        self.tools.write_invoice_to_path(path, contents)

    def test_01_einvoice_listing_response_time_expired(self):
        """-->> onay süresi geçmiş  e fatura listeleme testi."""

        response = requests.get(url=self.BASE_URL_INVOICE_OUTBOX + self.RESPONSE_TIME_EXPIRED, headers=self.HEADERS)

        self.assertIsNotNone(response.json()['data']['contents'])
        self.assertIsNone(response.json()['error'])

        path = "Files/E_Fatura/Giden/efatura_onay_suresi_gecmis_liste.txt"
        contents = response.json()['data']['contents']

        self.tools.write_invoice_to_path(path, contents)

    def test_02_einvoice_listing_undelivered(self):
        """-->> cevap teslim edilemeyen e fatura listeleme testi."""

        response = requests.get(url=self.BASE_URL_INVOICE_OUTBOX + self.UNDELIVERED, headers=self.HEADERS)

        self.assertIsNotNone(response.json()['data']['contents'])
        self.assertIsNone(response.json()['error'])

        path = "Files/E_Fatura/Giden/efatura_teslim_edilemeyen_liste.txt"
        contents = response.json()['data']['contents']

        self.tools.write_invoice_to_path(path, contents)

    def test_03_einvoice_listing_rejected(self):
        """-->> reddedilen e fatura listeleme testi."""

        response = requests.get(url=self.BASE_URL_INVOICE_OUTBOX + self.REJECTED, headers=self.HEADERS)

        self.assertIsNotNone(response.json()['data']['contents'])
        self.assertIsNone(response.json()['error'])

        path = "Files/E_Fatura/Giden/efatura_reddedilmis_liste.txt"
        contents = response.json()['data']['contents']

        self.tools.write_invoice_to_path(path, contents)

    def test_04_einvoice_outgoing_statuses(self):
        """-->> giden e fatura durumları testi."""

        response = requests.get(url=self.BASE_URL_INVOICE_OUTBOX + self.LOOKUP_STATUS, headers=self.HEADERS)
        self.assertIsNotNone(response.json()['data'])
        self.assertIsNone(response.json()['error'])

        path = "Files/E_Fatura/Giden/efatura_giden_durumları_liste.txt"
        contents = response.json()['data']

        for content in contents:
            print(f"Value :{content['value']} - Label : {content['label']}")

    def test_05_einvoice_download_ubl(self):
        """-->> giden e fatura ubl indirme testi"""

        id_values = self.tools.get_customer_id(self.E_INVOICE_OUTGOING)
        for id in id_values:
            login_request = [{'id': id}]
            body_json = json.dumps(login_request)

            response = requests.post(url=self.BASE_URL_INVOICE_OUTBOX + self.DOWNLOAD_UBL, headers=self.headers,
                                     data=body_json)
            self.assertIsNotNone(response.json()['data'])
            self.assertIsNone(response.json()['error'])

            self.tools.write_content_to_zip(response, self.UBL, self.E_INVOICE_OUTGOING)

    def test_06_einvoice_download_html(self):
        """-->> giden e fatura html indirme testi"""

        id_values = self.tools.get_customer_id(self.E_INVOICE_OUTGOING)
        for id in id_values:
            login_request = [{'id': id}]
            body_json = json.dumps(login_request)

            response = requests.post(url=self.BASE_URL_INVOICE_OUTBOX + self.DOWNLOAD_HTML, headers=self.headers,
                                     data=body_json)
            response_data = response.json()['data']

            self.assertIsNotNone(response_data)
            self.assertIsNone(response.json()['error'])

            self.tools.write_content_to_zip(response, self.HTML, self.E_INVOICE_OUTGOING)

    def test_07_einvoice_download_pdf(self):
        """-->> giden e fatura pdf indirme testi"""

        id_values = self.tools.get_customer_id(self.E_INVOICE_OUTGOING)
        for id in id_values:
            login_request = [{'id': id}]
            body_json = json.dumps(login_request)

            response = requests.post(url=self.BASE_URL_INVOICE_OUTBOX + self.DOWNLOAD_PDF, headers=self.headers,
                                     data=body_json)
            response_data = response.json()['data']

            self.assertIsNotNone(response_data)
            self.assertIsNone(response.json()['error'])

            self.tools.write_content_to_zip(response, self.PDF, self.E_INVOICE_OUTGOING)


if __name__ == '__main__':
    unittest.main()
