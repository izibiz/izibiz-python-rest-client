import os


def create_directories():
    os.makedirs("Files", exist_ok=True)  # e fatura uygulaması içinv
    os.makedirs("Files/E_Fatura", exist_ok=True)

    os.makedirs("Files/E_Fatura/Gelen", exist_ok=True)
    os.makedirs("Files/E_Fatura/Gelen/E_Fatura_liste_html", exist_ok=True)
    os.makedirs("Files/E_Fatura/Gelen/E_Fatura_liste_pdf", exist_ok=True)
    os.makedirs("Files/E_Fatura/Gelen/E_Fatura_liste_ubl", exist_ok=True)

    os.makedirs("Files/E_Fatura/Giden", exist_ok=True)
    os.makedirs("Files/E_Fatura/Giden/E_Fatura_liste_html", exist_ok=True)
    os.makedirs("Files/E_Fatura/Giden/E_Fatura_liste_pdf", exist_ok=True)
    os.makedirs("Files/E_Fatura/Giden/E_Fatura_liste_ubl", exist_ok=True)

    os.makedirs("Files/E_Fatura/Gonderme", exist_ok=True)

    os.makedirs("Files/E_Mustahsil", exist_ok=True)  # e mustahsil uygulaması için
    os.makedirs("Files/E_Mustahsil/E_Mustahsil_liste_html", exist_ok=True)
    os.makedirs("Files/E_Mustahsil/E_Mustahsil_liste_pdf", exist_ok=True)
    os.makedirs("Files/E_Mustahsil/E_Mustahsil_liste_ubl", exist_ok=True)

    os.makedirs("Files/E_Smm", exist_ok=True)  # e smm uygulaması için
    os.makedirs("Files/E_Smm/E_Smm_liste_html", exist_ok=True)
    os.makedirs("Files/E_Smm/E_Smm_liste_pdf", exist_ok=True)
    os.makedirs("Files/E_Smm/E_Smm_liste_ubl", exist_ok=True)

    os.makedirs("Files/GENERATED_XML", exist_ok=True)


    os.makedirs("Required_Files/E_Fatura", exist_ok=True)
    os.makedirs("Required_Files/E_Mustahsil", exist_ok=True)
    os.makedirs("Required_Files/E_Smm", exist_ok=True)
    os.makedirs("Required_Files/XML_CONTENTS", exist_ok=True)
    os.makedirs("Required_Files/XSD", exist_ok=True)


