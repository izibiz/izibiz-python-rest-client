import requests
import unittest
import base64
import zipfile
import xml.etree.ElementTree as et


class TestGibUserList(unittest.TestCase):
    URL_1 = "https://apitest.izibiz.com.tr/v1/resources/gib-users?identifier=4840847211"
    URL_2 = "https://apitest.izibiz.com.tr/v1/resources/gib-users/binary"

    def test_1_GibUserList(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.URL_1, headers=headers)
        response_data = response.json()["data"]

        self.assertNotEqual(len(response_data), 0)
        self.assertIsNone(response.json()['error'])

        print(f"Mukellef Listesi :  {response.json()['data'][0]['identifier']}")
        print(f"Mukellef Turu-1 :  {response.json()['data'][0]['documentType']}")
        print(f"Mukellef Turu-2 :  {response.json()['data'][1]['documentType']}")
        print("************************************************************")

    def test_GibUserListBinary(self):

        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.URL_2, headers=headers)
        response_data = response.json()['data']

        self.assertNotEqual(len(response_data), 0)
        self.assertIsNone(response.json()['error'])

        encoded_data = response.json()['data']['content']
        decoded_data = base64.b64decode(encoded_data)

        file = open(file="dosya.zip", mode="wb")
        file.write(decoded_data)
        file.close()

        # ZIP dosyasının adı
        zip_file_name = "dosya.zip"

        # ZIP dosyasını açma
        with zipfile.ZipFile(zip_file_name, "r") as zip_file:
            # ZIP dosyasındaki tüm dosyaları listeleme
            file_list = zip_file.namelist()

            # Her bir dosya için XML verilerini çıkarma ve işleme
            for file_name in file_list:
                # ZIP dosyasından XML veriyi çıkarma
                with zip_file.open(file_name) as xml_file:
                    xml_data = xml_file.read()

                    # XML verisini ayrıştırma
                    root = et.fromstring(xml_data)

                    # XML verisini işleme veya yazdırma

                    for user in root.findall('USER')[:10]:
                        identifier = user.find('IDENTIFIER').text
                        alias = user.find('ALIAS').text
                        title = user.find('TITLE').text
                        type = user.find('TYPE').text
                        register_time = user.find('REGISTER_TIME').text
                        unit = user.find('UNIT').text
                        document_type = user.find('DOCUMENT_TYPE').text
                        alias_creation_time = user.find('ALIAS_CREATION_TIME').text

                        print(f"IDENTIFIER: {identifier}")
                        print(f"ALIAS: {alias}")
                        print(f"TITLE: {title}")
                        print(f"TYPE: {type}")
                        print(f"REGISTER_TIME' {register_time}")
                        print(f"UNIT' {unit}")
                        print(f"DOCUMENT_TYPE' {document_type}")
                        print(f"ALIAS_CREATION_TIME' {alias_creation_time}")
                        print("##########################################")


if __name__ == '__main__':
    unittest.main()
