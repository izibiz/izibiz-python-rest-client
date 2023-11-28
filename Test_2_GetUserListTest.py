import json
import requests
import unittest


class TestGibUserList(unittest.TestCase):

    URL = "https://apitest.izibiz.com.tr/v1/resources/gib-users?identifier=4840847211"

    def test_GibUserList(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.URL, headers=headers)
        response_data = response.json()["data"]

        self.assertNotEqual(len(response_data), 0)
        self.assertIsNone(response.json()['error'])

        print(f"Mukellef Listesi :  {response.json()['data'][0]['identifier']}")
        print(f"Mukellef Turu-1 :  {response.json()['data'][0]['documentType']}")
        print(f"Mukellef Turu-2 :  {response.json()['data'][1]['documentType']}")
        print("************************************************************")

if __name__ == '__main__':
    unittest.main()
