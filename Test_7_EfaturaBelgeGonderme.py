import json
import requests
import unittest
from Create_Access_Token import CreateAccessToken
from Variables import Variable
from Utilities import Tools


class TestEFaturaGonderme(unittest.TestCase, Variable):
    tools = Tools()
    tools.get_prefix()
    create_access_token = CreateAccessToken()
    access_token = create_access_token.getAccessToken()
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}

    def test_00_einvoice_document_load(self):
        """-->> Belge sisteme yüklenirken numarasının atanmış şekilde yüklenmesi testi
                    assignNumber: False -> yüklenecek belgeye numara ataması gerekmiyor"""

        zip_base64 = self.tools.set_loading_content(self.E_INVOICE)
        prefix = self.tools.random_choise_prefix(self.E_INVOICE)

        data = {"seriePrefix": prefix, "assignNumber": False, "compressed": True,
                "content": zip_base64, "documentAction": "DRAFT"}
        body_json = json.dumps(data)
        response = requests.post(self.BASE_URL_INVOICE + self.UBL, headers=self.headers, data=body_json)
        self.assertIsNone(response.json()['error'])
        self.assertIsNotNone(response.json()['data'])

        response_data = response.json()['data']
        print("--->>> seriePrefix : UGR - assignNumber : False - idAssigned : False senaryosu <<<---")
        print(f"Document No : {response_data['documentNo']}")
        print(f"UUID : {response_data['uuid']}")
        print(f"Document Status : {response_data['documentStatus']}\n\n")


if __name__ == '__main__':

    unittest.main()
import json
import requests
import unittest
from Create_Access_Token import CreateAccessToken
from Variables import Variable
from Utilities import Tools


class TestEFaturaGonderme(unittest.TestCase, Variable):
    tools = Tools()
    tools.get_prefix()
    create_access_token = CreateAccessToken()
    access_token = create_access_token.getAccessToken()
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}

    def test_00_einvoice_document_load(self):
        """-->> Belge sisteme yüklenirken numarasının atanmış şekilde yüklenmesi testi
                    assignNumber: False -> yüklenecek belgeye numara ataması gerekmiyor"""

        zip_base64 = self.tools.set_loading_content(self.E_INVOICE)
        prefix = self.tools.random_choise_prefix(self.E_INVOICE)

        data = {"seriePrefix": prefix, "assignNumber": False, "compressed": True,
                "content": zip_base64, "documentAction": "DRAFT"}
        body_json = json.dumps(data)
        response = requests.post(self.BASE_URL_INVOICE + self.UBL, headers=self.headers, data=body_json)
        self.assertIsNone(response.json()['error'])
        self.assertIsNotNone(response.json()['data'])

        response_data = response.json()['data']
        print("--->>> seriePrefix : UGR - assignNumber : False - idAssigned : False senaryosu <<<---")
        print(f"Document No : {response_data['documentNo']}")
        print(f"UUID : {response_data['uuid']}")
        print(f"Document Status : {response_data['documentStatus']}\n\n")


if __name__ == '__main__':

    unittest.main()
import json
import requests
import unittest
from Create_Access_Token import CreateAccessToken
from Variables import Variable
from Utilities import Tools


class TestEFaturaGonderme(unittest.TestCase, Variable):
    tools = Tools()
    tools.get_prefix()
    create_access_token = CreateAccessToken()
    access_token = create_access_token.getAccessToken()
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}

    def test_00_einvoice_document_load(self):
        """-->> Belge sisteme yüklenirken numarasının atanmış şekilde yüklenmesi testi
                    assignNumber: False -> yüklenecek belgeye numara ataması gerekmiyor"""

        zip_base64 = self.tools.set_loading_content(self.E_INVOICE)
        prefix = self.tools.random_choise_prefix(self.E_INVOICE)

        data = {"seriePrefix": prefix, "assignNumber": False, "compressed": True,
                "content": zip_base64, "documentAction": "DRAFT"}
        body_json = json.dumps(data)
        response = requests.post(self.BASE_URL_INVOICE + self.UBL, headers=self.headers, data=body_json)
        self.assertIsNone(response.json()['error'])
        self.assertIsNotNone(response.json()['data'])

        response_data = response.json()['data']
        print("--->>> seriePrefix : UGR - assignNumber : False - idAssigned : False senaryosu <<<---")
        print(f"Document No : {response_data['documentNo']}")
        print(f"UUID : {response_data['uuid']}")
        print(f"Document Status : {response_data['documentStatus']}\n\n")


if __name__ == '__main__':

    unittest.main()
import json
import requests
import unittest
from Create_Access_Token import CreateAccessToken
from Variables import Variable
from Utilities import Tools


class TestEFaturaGonderme(unittest.TestCase, Variable):
    tools = Tools()
    tools.get_prefix()
    create_access_token = CreateAccessToken()
    access_token = create_access_token.getAccessToken()
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}

    def test_00_einvoice_document_load(self):
        """-->> Belge sisteme yüklenirken numarasının atanmış şekilde yüklenmesi testi
                    assignNumber: False -> yüklenecek belgeye numara ataması gerekmiyor"""

        zip_base64 = self.tools.set_loading_content(self.E_INVOICE)
        prefix = self.tools.random_choise_prefix(self.E_INVOICE)

        data = {"seriePrefix": prefix, "assignNumber": False, "compressed": True,
                "content": zip_base64, "documentAction": "DRAFT"}
        body_json = json.dumps(data)
        response = requests.post(self.BASE_URL_INVOICE + self.UBL, headers=self.headers, data=body_json)
        self.assertIsNone(response.json()['error'])
        self.assertIsNotNone(response.json()['data'])

        response_data = response.json()['data']
        print("--->>> seriePrefix : UGR - assignNumber : False - idAssigned : False senaryosu <<<---")
        print(f"Document No : {response_data['documentNo']}")
        print(f"UUID : {response_data['uuid']}")
        print(f"Document Status : {response_data['documentStatus']}\n\n")


if __name__ == '__main__':

    unittest.main()
