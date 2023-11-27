import base64
import uuid
import zipfile
import random
import json
import requests
import unittest

from Create_Access_Token import CreateAccessToken
from Variables import Variable
from Utilities import Tools

class TestEFaturaGelen(unittest.TestCase, Variable):

    tools = Tools()
    params = {'status': 'Delivered'}
    create_access_token = CreateAccessToken()
    access_token = create_access_token.getAccessToken()
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}

    def test_00_einvoice_new_coming_listing(self):
        """-->> yeni gelen e fatura listeleme testi."""

        response = requests.get(url=self.BASE_URL_INVOICE_INBOX + self.DELIVERED, headers=self.HEADERS)

        self.assertIsNotNone(response.json()['data']['contents'])
        self.assertIsNone(response.json()['error'])

        path = "Files/E_Fatura/Gelen/efatura_yenigelen_liste.txt"
        contents = response.json()['data']['contents']
        self.tools.write_invoice_to_path(path, contents)

    def test_01_einvoice_new_coming_listing_copy(self):
        """-->> yeni gelen e fatura listeleme-kopya testi."""

        response = requests.get(url=self.BASE_URL_INVOICE_INBOX + self.LIST_COPY, headers=self.HEADERS)

        self.assertIsNotNone(response.json()['data']['contents'])
        self.assertIsNone(response.json()['error'])

        path = "Files/E_Fatura/Gelen/efatura_yenigelen_listecopy.txt"
        contents = response.json()['data']['contents']
        self.tools.write_invoice_to_path(path, contents)

    def test_02_einvoice_listing_waiting_for_approve(self):
        """-->> onay bekleyen e fatura listeleme testi."""

        response = requests.get(url=self.BASE_URL_INVOICE_OUTBOX + self.W_FOR_APPROVE, headers=self.HEADERS)

        self.assertIsNotNone(response.json()['data']['contents'])
        self.assertIsNone(response.json()['error'])

        path = "Files/E_Fatura/Gelen/efatura_onay_bekleyen_liste.txt"
        contents = response.json()['data']['contents']
        self.tools.write_invoice_to_path(path, contents)

    def test_03_einvoice_listing_response_time_expired(self):
        """-->> onay süresi geçmiş  e fatura listeleme testi."""

        response = requests.get(url=self.BASE_URL_INVOICE_INBOX + self.RESPONSE_TIME_EXPIRED, headers=self.HEADERS)

        self.assertIsNotNone(response.json()['data']['contents'])
        self.assertIsNone(response.json()['error'])

        path = "Files/E_Fatura/Gelen/efatura_onay_suresi_gecmis_liste.txt"
        contents = response.json()['data']['contents']
        self.tools.write_invoice_to_path(path, contents)

    def test_04_einvoice_listing_response_undelivered(self):
        """-->> cevap teslim edilemeyen e fatura listeleme testi."""

        response = requests.get(url=self.BASE_URL_INVOICE_INBOX + self.RESPONSE_UN_DELIVERED, headers=self.HEADERS)

        self.assertIsNotNone(response.json()['data']['contents'])
        self.assertIsNone(response.json()['error'])

        path = "Files/E_Fatura/Gelen/efatura_cevap_teslim_edilmemis_liste.txt"
        contents = response.json()['data']['contents']
        self.tools.write_invoice_to_path(path, contents)

    def test_05_einvoice_listing_rejected(self):
        """-->> reddedilen e fatura listeleme testi."""

        response = requests.get(url=self.BASE_URL_INVOICE_INBOX + self.REJECTED, headers=self.HEADERS)

        self.assertIsNotNone(response.json()['data']['contents'])
        self.assertIsNone(response.json()['error'])

        path = "Files/E_Fatura/Gelen/efatura_reddedilmis_liste.txt"
        contents = response.json()['data']['contents']
        self.tools.write_invoice_to_path(path, contents)

    def test_06_einvoice_listing_status(self):
        """-->> gelen e fatura durum sorgulama testi."""

        id = 84
        response = requests.get(url=self.BASE_URL_INVOICE_INBOX+f"/{id}", headers=self.HEADERS)
        self.assertIsNotNone(response.json()['data'])
        self.assertIsNone(response.json()['error'])
        content = response.json()['data']

        id = content["id"]
        documentNo = content["documentNo"]
        uuid = content["uuid"]
        documentStatus = content["documentStatus"]["value"]
        print("Sorgusu yapilan belgenin durumu : \n")
        print(f"id:{id}, key:{uuid}, documentNo:{documentNo}, documentStatus: {documentStatus}\n")

    @unittest.skip
    def test_07_einvoice_making_erp_read(self):
        """-->> gelen e fatura erp okundu yapma testi."""
        """bu kısım test ortamında çalışmıyor dev de testleri yapıldı"""

        row = self.tools.random_choise_row()
        body = [{"id": row['id'], "documentUuid": row['documentUuid'], "documentNo": row['documentNo']}]
        body_json = json.dumps(body)
        response = requests.post(url=self.BASE_URL_INVOICE_INBOX + self.ERP_READ, headers=self.HEADERS, data= body_json)
        contents = response.json()['data']

        self.assertIsNotNone(response.json()['data'])
        self.assertIsNone(response.json()['error'])

        for content in contents:
            id = content["id"]
            readStatus = content["readStatus"]
            status = content["status"]
            documentNo = content["documentNo"]
            documentUuid = content['documentUuid']

            print(f"id:{id}, readStatus:{readStatus}, status:{status}, documentNo: {documentNo},documentUuid: {documentUuid}\n")

    @unittest.skip
    def test_08_einvoice_making_erp_unread(self):
        """-->> gelen e fatura erp okunmadıs yapma testi."""
        """bu kısım test ortamında çalışmıyor dev de testleri yapıldı"""

        row = self.tools.random_choise_row()
        body = [{"id": row['id'], "documentUuid": row['documentUuid'], "documentNo": row['documentNo']}]
        body_json = json.dumps(body)
        response = requests.post(url=self.BASE_URL_INVOICE_INBOX + self.ERP_UNREAD, headers=self.HEADERS,
                                 data=body_json)
        contents = response.json()['data']

        self.assertIsNotNone(response.json()['data'])
        self.assertIsNone(response.json()['error'])

        for content in contents:
            id = content["id"]
            readStatus = content["readStatus"]
            status = content["status"]
            documentNo = content["documentNo"]
            documentUuid = content['documentUuid']

            print(f"id:{id}, readStatus:{readStatus}, status:{status}, documentNo: {documentNo},documentUuid: {documentUuid}\n")

    def test_09_einvoice_incoming_statuses(self):
        """-->> gelen e fatura durumları testi."""

        response = requests.get(url=self.BASE_URL_INVOICE_INBOX + self.LOOKUP_STATUS, headers=self.HEADERS)

        self.assertIsNotNone(response.json()['data'])
        self.assertIsNone(response.json()['error'])

        path = "Files/E_Fatura/Giden/efatura_gelen_durumarı_liste.txt"
        contents = response.json()['data']

        for content in contents:
            print(f"Value :{content['value']} - Label : {content['label']}")

    def test_10_einvoice_download_ubl(self):
        """-->> e fatura ubl indirme testi"""

        id_values = self.tools.get_customer_id(self.E_INVOICE_INCOMING)
        for id in id_values:
            login_request = [{'id': id}]
            body_json = json.dumps(login_request)

            response = requests.post(url=self.BASE_URL_INVOICE_INBOX + self.DOWNLOAD_UBL, headers=self.headers, data=body_json)

            self.assertIsNotNone(response.json()['data'])
            self.assertIsNone(response.json()['error'])
            self.tools.write_content_to_zip(response, self.UBL, self.E_INVOICE_INCOMING)

    def test_11_einvoice_download_html(self):
        """-->> e fatura html indirme testi"""

        id_values = self.tools.get_customer_id(self.E_INVOICE_INCOMING)
        for id in id_values:
            login_request = [{'id': id}]
            body_json = json.dumps(login_request)

            response = requests.post(url=self.BASE_URL_INVOICE_INBOX + self.DOWNLOAD_HTML, headers=self.headers, data=body_json)
            response_data = response.json()['data']

            self.assertIsNotNone(response_data)
            self.assertIsNone(response.json()['error'])

            self.tools.write_content_to_zip(response, self.HTML, self.E_INVOICE_INCOMING)

    def test_12_einvoice_download_pdf(self):
        """-->> e fatura pdf indirme testi"""

        id_values = self.tools.get_customer_id(self.E_INVOICE_INCOMING)
        for id in id_values:
            login_request = [{'id': id}]
            body_json = json.dumps(login_request)

            response = requests.post(url=self.BASE_URL_INVOICE_INBOX + self.DOWNLOAD_PDF, headers=self.headers, data=body_json)
            response_data = response.json()['data']

            self.assertIsNotNone(response_data)
            self.assertIsNone(response.json()['error'])

            self.tools.write_content_to_zip(response, self.PDF, self.E_INVOICE_INCOMING)


if __name__ == '__main__':
    unittest.main()
