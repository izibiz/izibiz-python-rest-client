from Create_Access_Token import CreateAccessToken


class Variable(CreateAccessToken):
    create_access_token = CreateAccessToken()
    access_token = create_access_token.getAccessToken()

    HEADERS = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
    BASE_URL_SMM = "https://apitest.izibiz.com.tr/v1/esmms"
    BASE_URL_INVOICE = "https://apitest.izibiz.com.tr/v1/einvoices/"
    BASE_URL_EMUSTAHSIL = "https://apitest.izibiz.com.tr/v1/ecreditnotes"
    BASE_URL_INVOICE_INBOX = "https://apitest.izibiz.com.tr/v1/einvoices/inbox"
    BASE_URL_INVOICE_OUTBOX = "https://apitest.izibiz.com.tr/v1/einvoices/outbox"
    DOWNLOAD_UBL = "/download/ubl"
    DOWNLOAD_PDF = "/download/pdf"
    DOWNLOAD_HTML = "/download/html"
    SERIES = "/series"
    XSLTS = "/xslts"
    LOAD_UBL = "/load/ubl"
    SEND_UBL = "/send/ubl"
    READ = "/portal-read-flag/READ"
    UNREAD = "/erp-read-flag/UNREAD"

    DELIVERED = "?status=Delivered"
    UNDELIVERED = "?status=unDelivered"
    LIST_COPY = "?status=New"
    W_FOR_APPROVE = "?status=WaitingForResponse"
    RESPONSE_TIME_EXPIRED = "?status=ResponseTimeExpired"
    RESPONSE_UN_DELIVERED = "?status=ResponseUnDelivered"
    REJECTED = "?status=Rejected"
    ERP_READ = "/erp-read-flag/READ"
    ERP_UNREAD = "/erp-read-flag/UNREAD"
    LOOKUP_STATUS = "/lookup-statuses"

    E_MUSTAHSIL = "E_Mustahsil"
    E_SMM = "E_Smm"
    E_INVOICE = "E_Fatura"
    E_INVOICE_INCOMING = "E_Fatura/Gelen"
    E_INVOICE_OUTGOING = "E_Fatura/Giden"
    UBL = "ubl"
    HTML = "html"
    PDF = "pdf"

