import json
import requests
import unittest
from Create_Access_Token import CreateAccessToken
from CreateRequiredDirectory import create_directories


class AuthAdapter(unittest.TestCase):

    URL = "https://apitest.izibiz.com.tr/v1/auth/token"
    create_directories()

    def test_login_Access(self):
        """basarili login olma testi"""

        headers = {'Content-Type': 'application/json'}
        username = "kullanici adi giriniz"
        password = "sifre giriniz"
        login_request = {"username": username, "password": password}
        body_json = json.dumps(login_request)

        response = requests.post(self.URL, headers=headers, data=body_json)
        response_data = response.json()['data']

        self.assertIsNotNone(response_data)
        self.assertIsNotNone(response_data.get('accessToken', None))
        print("\nBasarili Login Olma Testi : ")
        print("Erisim Anahtari : ")
        print(response.json()['data']['accessToken'])

        access_token = response.json()['data']['accessToken']
        create_access_token = CreateAccessToken()
        create_access_token.setAccessToken(access_token)

    def test_login_Failure(self):
        """basarisiz login olma testi"""

        headers = {'Content-Type': 'application/json'}
        login_request = {"username": "user123", "password": "pass123"}
        body_json = json.dumps(login_request)

        response = requests.post(self.URL, headers=headers, data=body_json)
        self.assertIsNone(response.json()['data'])
        self.assertIsNotNone(response.json()['error'])
        print("\nBasarisiz Login Olma Testi : ")
        print(f"Hata Kodu :  {response.json()['error']['code']}")
        print(f"Hata Mesaji :  {response.json()['error']['message']}")


if __name__ == '__main__':
    unittest.main()

