

![İzibiz](https://izibiz.com.tr/wp-content/uploads/2022/11/400dpiLogo_trns.webp)
# İZİBİZ PYTHON REST CLİENT

# AÇIKLAMLAR

Bu proje **İzibiz Bilişim Teknolojileri** şirketinin Özel Entegrasyon hizmetleri kapsamında geliştirilmiştir. Gerçekleştirilen bu proje kapsamında;
 - **Authentication**
 - **E-Fatura**
 - **E-Müstahsil**
 - **E-Serbest Meslek Makbuzu**
 
Ürünleri için **Rest** mimarisi kullanılarak test metotları geliştirilmiştir. Bu Entegrasyon **Python** dili kullanılarak Pycharm idesi üzerinden geliştirilmiştir.

# KURULUM
İlk olarak **https://github.com/izibiz/izibiz-python-rest-client** adresinden projeye ait tüm dosyalar indirilerek oluşturulan python projesine eklenir. Daha sonra **Test_1_AuthSample.py** dosyasının içindeki;
 - **username** = "kullanici adi giriniz"
 - **password** = "sifre giriniz"

Her python dosyasında import edilen kütüphaneler belirtilmiştir. Bu kütüphanler kodun başarılı bir şekilde çalışması gereklidir. Kurulum esnasında kodu çalıştırmadan önce bu kütüphanelerin import edilmesi gerekmektedir. İmport işlemi ide yardımıyla gerekli kütüphanenin üzerine tıklanarak otomotik olarak yada farklı yöntemler kullanarak yapılabilir. Ayrıca Python interpreter(yorumlayıcı)'in de eklenmiş olduğuna dikkat edilmelidir.

Alanlarına ilgili kullanıcı adı ve şifre değeri girilir. Daha sonra Test_1_AuthSample.py dosyası run edilir. Projede ilk koşulması gereken dosya Test_1_AuthSample.py dosyasıdır. Token alma işlemi bu sınıfta gerçekleştirilir.  Bu aşamada ayrıca proje boyunca kullanılacak olan dosya dizinleri de oluşturulur.

İlgili uygulamaların çeşitli aşamalarında( örneğin belge yükleme senaryoları gibi) gerekli olacak şablon belgeler **Required_Files** dizini altında her uygulamaya ait dosya içerisinde **template.xml** ismiyle mevcuttur. İstenildiğinde bu şablon belgeler belirtilen dizin üzerinden değiştirilebilir.

## XML Belge Üretmi
Xml belge üretme işlemi oluşturulan xml sınıfları üzerinden gerçekleştirilmektedir. Xml sınıfları XSD dosyaları yardımıyla oluşuturulmaktadır. Gerekli olan XSD belgeleri Required_files/XSD yolu altında mevcuttur. İlgili belgeler GİB üzerinde sağlanmıştır.

### XML Belge Üretim Aşamaları:
- ilk olarak **xsdata** kütüphanesi Pycharm idesinin terminali üzerinden aşağıdaki komut yardımıyla indirilip kurulur.
```
pip install xsdata
```
- Kurulumdan sonra yine terminal üzerinden aşağıdaki komut yardımıyla xml sınıfları elde edilir.
```
xsdata  Required_Files/XSD/maindoc/UBL-Invoice-2.1.xsd --package deneme
```
- Burada ilk parametre kütüphane ismi, ikinci parametre xsd dosyasının yolu ve son parametre ise sınıfların kaydedileceği paket ismidir. burada paket isminden önce **--package** ön ekinin yazılması unutulmamalıdır.
- Bu işlem sonucunda terminalde aşağıdakine benzer bir çıktı elde edilir.
  
>(venv) PS C:\Users\Muhammet\IzibizTestEntegration> xsdata  Required_Files/XSD/maindoc/UBL-Invoice-2.1.xsd --package deneme
>========= xsdata v23.8 / Python 3.11.5 / Platform win32 =========
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/maindoc/UBL-Invoice-2.1.xsd
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-CommonAggregateComponents-2.1.xsd
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-CommonBasicComponents-2.1.xsd
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-QualifiedDataTypes-2.1.xsd
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-UnqualifiedDataTypes-2.1.xsd
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/CCTS_CCT_SchemaModule-2.1.xsd
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/CCTS_CCT_SchemaModule-2.1.xsd
>Builder: 10 main and 0 inner classes
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-UnqualifiedDataTypes-2.1.xsd
>Builder: 20 main and 0 inner classes
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-QualifiedDataTypes-2.1.xsd
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-CommonBasicComponents-2.1.xsd
>Builder: 1746 main and 0 inner classes
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-CommonAggregateComponents-2.1.xsd
>Builder: 897 main and 0 inner classes
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-CommonExtensionComponents-2.1.xsd
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-ExtensionContentDataType-2.1.xsd
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-CommonSignatureComponents-2.1.xsd
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-SignatureAggregateComponents-2.1.xsd
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-SignatureBasicComponents-2.1.xsd
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-SignatureBasicComponents-2.1.xsd
>Builder: 2 main and 0 inner classes
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-xmldsig-core-schema-2.1.xsd
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-xmldsig-core-schema-2.1.xsd
>Builder: 49 main and 0 inner classes
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-XAdESv132-2.1.xsd
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-XAdESv132-2.1.xsd
>Builder: 90 main and 0 inner classes
>Parsing schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-XAdESv141-2.1.xsd
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-XAdESv141-2.1.xsd
>Builder: 3 main and 0 inner classes
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-SignatureAggregateComponents-2.1.xsd
>Builder: 2 main and 0 inner classes
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-CommonSignatureComponents-2.1.xsd
>Builder: 2 main and 0 inner classes
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-ExtensionContentDataType-2.1.xsd
>Builder: 1 main and 0 inner classes
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/common/UBL-CommonExtensionComponents-2.1.xsd
>Builder: 19 main and 0 inner classes
>Compiling schema file:///C:/Users/Muhammet/IzibizTestEntegration/Required_Files/XSD/maindoc/UBL-Invoice-2.1.xsd
>Builder: 2 main and 0 inner classes
>Generating package: deneme.common.ubl_signature_aggregate_components_2_1
>Generating package: deneme.common.ubl_common_signature_components_2_1
>Generating package: deneme.common.ubl_extension_content_data_type_2_1
>Generating package: deneme.common.ubl_common_extension_components_2_1
>Generating package: deneme.maindoc.ubl_invoice_2_1

- Bu işlemden sonra xml sınıfları oluşturulacaktır.
- daha sonra proje içinde olan **GenaraterInvoiceXml.py** dosyası gibi xml elementlerinin içeriği doldurulur ve elde edilen xml belgesi kaydedilir.
- xml oluştururken **EmbeddedDocumentBinaryObject** elementinin değerlerini kod karmaşıklığı olmaması açısından dosyadan okuyoruz. Bu nedenle **Required_File** dosyası içinde **XML_CONTENTS** dosyası mevcuttur. Bu dosya içerisine  fatura ve müstahsil xml belgesi üretirken kullanılacak **EmbeddedDocumentBinaryObject** elementinin içeriği konulmuştur. **EmbeddedDocumentBinaryObject** elementinin içeri bu dosyalardan okunur. Yada direkt olarak kod üzerinden manuel olarak da bu veri **EmbeddedDocumentBinaryObject** elementine atanabilir.

Oluşturulan xml belgelerin **şematron** kontrolünden geçip geçmediğini görmek için bazı yollar izlenebilir.Örneğin e fatura xml belgesi için şu yol izlenebilir.
e-fatura belge gönderme kısmına gidilip 
```
zip_base64 = self.tools.set_loading_content(self.E_INVOICE)
```
satırında bulunan **set_loading_content** metodunun tanımlamasına gidilip e invoice için belge yolu olarak verilen yol yerine yorum satırı halinde bulunan ve oluşan xml belgelerinin yolunu gösteren bu yol kullanılabilir.Yada oluşan xml belge nereye kaydedildiyse orası yol olarak verilebilir.

Belge yükleme senaryolarında şablon belge kullanmak yerine artık kod tarafından üretilen xml belgelerin kullanılması isteniyorsa yukarıda belirtilen yöntem kullanılabilir.

✨Kolay Gelsin...
