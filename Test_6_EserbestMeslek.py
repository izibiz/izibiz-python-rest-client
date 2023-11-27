import json
import requests
import unittest
import base64
import uuid
import zipfile
import random
from Variables import Variable
from Utilities import Tools
from Create_Access_Token import CreateAccessToken
#import xml.etree.ElementTree as ET


class TestEMustahsil(unittest.TestCase, Variable):

    tools = Tools()
    create_access_token = CreateAccessToken()
    access_token = create_access_token.getAccessToken()
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}

    def test_esmm_000_listing(self):

        """ -->> e serbest meslek listeleme testi"""

        response = requests.get(url=self.BASE_URL_SMM, headers=self.HEADERS)

        self.assertNotEqual(len(response.json()['data']['contents']), 0)
        self.assertIsNone(response.json()['error'])
        contents = response.json()['data']['contents']
        self.tools.write_content_to_file(contents, self.E_SMM)

    def test_esmm_001_download_ubl(self):
        """-->> e serbest meslek ubl indirme testi."""

        tools = Tools()
        id_values = tools.get_customer_id(self.E_SMM)

        for id in id_values:
            login_request = [{'id': id}]
            body_json = json.dumps(login_request)
            response = requests.post(url=self.BASE_URL_SMM + self.DOWNLOAD_UBL, headers=self.HEADERS, data=body_json)
            self.assertIsNotNone(response.json()['data'])
            self.assertIsNone(response.json()['error'])

            tools.write_content_to_zip(response, self.UBL, self.E_SMM)

    def test_esmm_002_download_html(self):
        """-->> e serbest meslek html indirme testi."""

        tools = Tools()
        id_values = tools.get_customer_id(self.E_SMM)

        for id in id_values:
            login_request = [{'id': id}]
            body_json = json.dumps(login_request)
            response = requests.post(self.BASE_URL_SMM + self.DOWNLOAD_HTML, headers=self.HEADERS, data=body_json)
            response_data = response.json()['data']
            self.assertIsNotNone(response_data)
            self.assertIsNone(response.json()['error'])
            tools.write_content_to_zip(response, self.HTML, self.E_SMM)

    def test_esmm_003_download_pdf(self):
        """-->> e serbest meslek pdf indirme testi."""

        tools = Tools()
        id_values = tools.get_customer_id(self.E_SMM)

        for id in id_values:

            login_request = [{'id': id}]
            body_json = json.dumps(login_request)
            response = requests.post(self.BASE_URL_SMM + self.DOWNLOAD_PDF, headers=self.HEADERS, data=body_json)
            response_data = response.json()['data']
            self.assertIsNotNone(response_data)
            self.assertIsNone(response.json()['error'])
            tools.write_content_to_zip(response, self.PDF, self.E_SMM)

    def test_esmm_004_series_listing(self):

        """-->> e serbest meslek seri listeleme testi."""

        response = requests.get(self.BASE_URL_SMM + self.SERIES, headers=self.HEADERS)
        response_data = response.json()['data']
        self.assertIsNotNone(response_data)
        self.assertIsNone(response.json()['error'])
        contents = response.json()['data']
        path = "Files/E_Smm/active_prefix_list"

        file = open(path, "w")
        for content in contents:
            lastId = content['lastId']
            prefix = content['prefix']
            yearPrefix = content['yearPrefix']
            active = content['active']

            if active is True:
                if yearPrefix == 2023:
                    file.write(f"{prefix}\n")

            print(f"lastId:{lastId}  - prefix:{prefix} - yearPrefix:{yearPrefix} - active:{active}\n ")
        file.close()
        print("***************************************************")

    def test_esmm_005_xslt_listing(self):
        """-->> e serbest meslek xslts listesi indirme testi."""

        response = requests.get(self.BASE_URL_SMM + self.XSLTS, headers=self.HEADERS)
        contents = response.json()['data']
        self.assertIsNotNone(contents)
        self.assertIsNone(response.json()['error'])
        path = "Files/E_Smm/e_smm_xslts_list.xml"
        file = open(path, mode="wb")

        for content in contents:
            name = content['name']
            description = content['description']
            isMaster = content['isMaster']

            print(f"name:{name}  - description:{description} - isMaster:{isMaster}")
            encoded_data = content['content']
            decoded_data = base64.b64decode(encoded_data)
            file.write(decoded_data)
        print("***************************************************")
        file.close()

    def test_esmm_006_load_scenario_1(self):

        """-->> Belge sisteme yüklenirken numarasının atanmış şekilde yüklenmesi testi.
            assignNumber: False -> yüklenecek belgeye numara ataması gerekmiyor
            idAssigned:   False -> Yüklenecek belgenin numarası atanmamış"""

        tools = Tools()
        zip_base64 = tools.set_loading_content(self.E_SMM)
        prefix = tools.random_choise_prefix(self.E_SMM)

        data = {"seriePrefix": prefix, "assignNumber": False, "idAssigned": False, "compressed": True,
                "content": zip_base64, "sendingType": "KAGIT"}
        body_json = json.dumps(data)
        response = requests.post(self.BASE_URL_SMM + self.LOAD_UBL, headers=self.HEADERS, data=body_json)
        self.assertIsNone(response.json()['error'])
        self.assertIsNotNone(response.json()['data'])

        response_data = response.json()['data']
        print("--->>> seriePrefix : UGR - assignNumber : False - idAssigned : False senaryosu <<<---")
        print(f"Document No : {response_data['documentNo']}")
        print(f"UUID : {response_data['uuid']}")
        print(f"Document Status : {response_data['documentStatus']}\n\n")

    def test_esmm_007_load_scenario_2(self):

        """-->> Belge sisteme yüklenirken numarasının sistem tarafından atanması testi.
            assignNumber: True  -> Yüklenecek belgeye numara ataması gerekiyor
            idAssigned":  False -> Yüklenecek belgenin numarası atanmamış """

        tools = Tools()
        zip_base64 = tools.set_loading_content(self.E_SMM)
        prefix = tools.random_choise_prefix(self.E_SMM)
        data = {"seriePrefix":prefix, "assignNumber": True, "idAssigned": False, "compressed": True,
                "content": zip_base64,"sendingType": "KAGIT"}
        body_json = json.dumps(data)
        response = requests.post(self.BASE_URL_SMM + self.LOAD_UBL, headers=self.HEADERS, data=body_json)
        self.assertIsNone(response.json()['error'])
        self.assertIsNotNone(response.json()['data'])

        response_data = response.json()['data']
        print("--->>> seriePrefix : UGR - assignNumber : True - idAssigned : False senaryosu<<<---")
        print(f"Document No : {response_data['documentNo']}")
        print(f"UUID : {response_data['uuid']}")
        print(f"Document Status : {response_data['documentStatus']}\n\n")

    def test_esmm_008_load_scenario_3(self):

        """-->> Belge sisteme yüklenirken numarasının atanmış varsayılması testi.
                    assignNumber: False -> yüklenecek belgeye numara ataması gerekmiyor
                    idAssigned:   True  -> Yüklenecek belgenin numarası atanmış"""

        tools = Tools()
        zip_base64 = tools.set_loading_content(self.E_SMM)
        prefix = tools.random_choise_prefix(self.E_SMM)
        data = {"seriePrefix": prefix, "assignNumber": False, "idAssigned": True, "compressed": True,
                "content": zip_base64,"sendingType": "KAGIT"}
        body_json = json.dumps(data)
        response = requests.post(self.BASE_URL_SMM + self.LOAD_UBL, headers=self.HEADERS, data=body_json)
        self.assertIsNone(response.json()['error'])
        self.assertIsNotNone(response.json()['data'])

        response_data = response.json()['data']
        print("--->>> assignNumber: False ve idAssigned: True senaryosu <<<---")
        print(f"Document No : {response_data['documentNo']}")
        print(f"UUID : {response_data['uuid']}")
        print(f"Document Status : {response_data['documentStatus']}\n\n")

    def test_esmm_009_load_scenario_4(self):

        """-->>numara atanmış belgeye tekrar numara atanamayacağından dolayı hata verilir.
           assignNumber: True -> yüklenecek belgeye numara ataması gerekiyor
           idAssigned:   True  -> Yüklenecek belgenin numarası atanmış"""

        tools = Tools()
        zip_base64 = tools.set_loading_content(self.E_SMM)
        prefix = tools.random_choise_prefix(self.E_SMM)
        data = {"seriePrefix": prefix, "assignNumber": True, "idAssigned": True, "compressed": True,
                "content": zip_base64,"sendingType": "KAGIT"}
        body_json = json.dumps(data)
        response = requests.post(self.BASE_URL_SMM + self.LOAD_UBL, headers=self.HEADERS, data=body_json)
        self.assertIsNotNone(response.json()['error'])
        self.assertIsNone(response.json()['data'])

        response_data = response.json()['error']
        print("--->>> assignNumber: True ve idAssigned: True senaryosu <<<---")
        print(f" Mesaj : {response_data['message']}\n\n\n")


if __name__ == '__main__':
    unittest.main()
