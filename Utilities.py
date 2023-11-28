import base64
import uuid
import zipfile
import random
from datetime import datetime
from Variables import Variable
import xml.etree.ElementTree as ET


class Tools:

    def get_customer_id(self, type):

        id_values = []
        path = ""

        if type == Variable.E_MUSTAHSIL:
            path = "Files/E_Mustahsil/E_Mustahsil_liste"
        elif type == Variable.E_SMM:
            path = "Files/E_Smm/E_Smm_liste"
        elif type == Variable.E_INVOICE_INCOMING:
            path = "Files/E_Fatura/Gelen/efatura_yenigelen_liste.txt"
        elif type == Variable.E_INVOICE_OUTGOING:
            path = "Files/E_Fatura/Giden/efatura_onay_bekleyen_liste.txt"

        with open(file=path, mode='r') as file_1:

            for row in file_1:
                parts = row.split(', ')  # Virgül ve boşluğa göre satırı böler

                id_value = None
                for part in parts:
                    if part.startswith('id:'):
                        id_value = part.split(':')[1]  # "id" değerini çıkarırız

                if id_value is not None:
                    id_values.append(id_value)

        return id_values

    def replace_xml(self, file_path, target_label, new_data):

        tree = ET.parse(file_path)
        root = tree.getroot()
        uuid_element = root.find(target_label)
        uuid_element.text = new_data
        tree.write(file_path)

    def set_emustahsil_content(self):

        random_value = str(uuid.uuid4())
        xml_file_path = 'Files/E_Mustahsil/template.xml'
        element_1 = ".//{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UUID"
        element_2 = ".//{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID"
        random_digit = random.randint(0, 99999)
        random_digit = str(random_digit).zfill(5)

        self.replace_xml(xml_file_path, element_1, random_value)
        self.replace_xml(xml_file_path, element_2, f"HSN20220000{random_digit}")

        compressed_file = 'compressed.zip'
        with zipfile.ZipFile(compressed_file, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.write(xml_file_path, arcname=xml_file_path)

        with open(compressed_file, "rb") as zip:
            zip_data = zip.read()
        zip_base64 = base64.b64encode(zip_data).decode('utf-8')

        return zip_base64

    def set_loading_content(self, type):

        random_value = str(uuid.uuid4())
        compressed_file = 'compressed.zip'
        element_1 = ".//{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UUID"
        element_2 = ".//{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID"
        random_digit = random.randint(0, 99999)
        random_digit = str(random_digit).zfill(5)

        if type == Variable.E_MUSTAHSIL:
            xml_file_path = "Required_Files/E_Mustahsil/template.xml"
            # xml_file_path = "Files/GENERATED_XML/creditNote_xml.xml"  # elle üretilen xml belgesinin yolu
            self.replace_xml(xml_file_path, element_1, random_value)
            self.replace_xml(xml_file_path, element_2, f"MUH{datetime.now().today().year}0000{random_digit}")

            with zipfile.ZipFile(compressed_file, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.write(xml_file_path, arcname=xml_file_path)

        if type == Variable.E_SMM:
            xml_file_path = 'Required_Files/E_Smm/template.xml'
            self.replace_xml(xml_file_path, element_1, random_value)
            self.replace_xml(xml_file_path, element_2, f"MUH{datetime.now().today().year}0000{random_digit}")

            with zipfile.ZipFile(compressed_file, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.write(xml_file_path, arcname=xml_file_path)

        if type == Variable.E_INVOICE:
            xml_file_path = "Required_Files/E_Fatura/template.xml"
            # xml_file_path = "Files/GENERATED_XML/invoice_xml.xml" # elle üretilen xml belgesinin yolu

            self.replace_xml(xml_file_path, element_1, random_value)
            self.replace_xml(xml_file_path, element_2, f"MUH{datetime.now().today().year}0000{random_digit}")

            with zipfile.ZipFile(compressed_file, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.write(xml_file_path, arcname=xml_file_path)

        with open(compressed_file, "rb") as zip:
            zip_data = zip.read()
        zip_base64 = base64.b64encode(zip_data).decode('utf-8')

        return zip_base64

    def get_prefix(self):
        """ bu foksiyon gelen e fatura listesindeki prefix leri elde eder """

        path_1 = "Files/E_Fatura/Gelen/efatura_yenigelen_liste.txt"
        path_2 = "Files/E_Fatura/Gelen/efatura_prefix_liste.txt"
        prefix_list = ['XXX']
        # baslangıcta liste bos olacagı icin null hatası almamak adına XXX degeri verildi

        with open(file=path_1, mode='r') as file_1:
            with open(file=path_2, mode='w') as file_2:

                for row in file_1:
                    parts = row.split(', ')  # Virgül ve boşluğa göre satırı böler
                    prefix = ""

                    for part in parts:
                        if part.startswith('documentNo:'):
                            data = part.split(':')[1]  # "id" değerini çıkarırız
                            prefix = data[:3]

                            if prefix is not None:
                                if prefix not in prefix_list:
                                    prefix_list.append(prefix)
                                    file_2.write(f"{prefix}\n")

        return

    def random_choise_prefix(self, type):

        path = ""

        if type == Variable.E_MUSTAHSIL:
            path = "Files/E_Mustahsil/active_prefix_list"

        elif type == Variable.E_SMM:
            path = "Files/E_Smm/active_prefix_list"

        elif type == Variable.E_INVOICE:

            path = "Files/E_Fatura/Gelen/efatura_prefix_liste.txt"

        else:
            print(">>  gecerli bir dosya adresi girin <<\n")

        with open(path, 'r', encoding='utf-8') as file:
            rows = file.readlines()

        pure_rows = [row.rstrip() for row in rows]
        random_row = random.choice(pure_rows)

        return random_row

    def write_content_to_file(self, contents, app_type):

        path = f"Files/{app_type}/{app_type}_liste"

        file = open(path, "w")
        for content in contents:
            id = content["id"]
            documentNo = content["documentNo"]
            uuid = content["uuid"]
            documentStatus = content["documentStatus"]["value"]

            if documentStatus != "UnReported":
                file.write(f"id:{id}, key:{uuid}, documentNo:{documentNo}, documentStatus: {documentStatus}\n")

        file.close()

    def write_invoice_to_path(self, path, contents):

        file = open(path, "w")
        for content in contents:
            id = content["id"]
            documentNo = content["documentNo"]
            uuid = content["uuid"]
            documentStatus = content["documentStatus"]["value"]

            file.write(f"id:{id}, key:{uuid}, documentNo:{documentNo}, documentStatus: {documentStatus}\n")

        file.close()

    def write_content_to_zip(self, response, download_type, app_type):

        encoded_data = response.json()['data']['content']
        file_name = response.json()["data"]['filename']
        decoded_data = base64.b64decode(encoded_data)

        if app_type == Variable.E_INVOICE_INCOMING:
            path = f"Files/{app_type}/{Variable.E_INVOICE}_liste_{download_type}/{file_name}"
        elif app_type == Variable.E_INVOICE_OUTGOING:
            path = f"Files/{app_type}/{Variable.E_INVOICE}_liste_{download_type}/{file_name}"
        else:
            path = f"Files/{app_type}/{app_type}_liste_{download_type}/{file_name}"

        file_2 = open(path, "wb")
        file_2.write(decoded_data)
        file_2.close()

    def random_choise_row(self):

        path = "Files/E_Fatura/Gelen/efatura_yenigelen_liste.txt"

        with open(path, 'r') as dosya:
            rows = dosya.readlines()

        random_row = random.choice(rows)

        key_value = random_row.split(', ')
        veri = {}
        for data in key_value:
            key, value = data.split(':')

            veri[key] = value

        return veri

    def get_time(self):
        # Şu anki tarih, saat ve saniye bilgisi
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    def get_date(self):

        # Şu anki tarih ve saat bilgisi
        now = datetime.now()
        current_datetime = now.strftime("%Y-%m-%d")
        return current_datetime
