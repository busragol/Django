from django.db import models

# Create your models here.
class AddCustomer(models.Model):
    City_Choices=(
        ('Adana','Adana'),
        ('Adıyaman','Adıyaman'),
        ('Afyon','Afyon'),
        ('Ağrı','Ağrı'),
        ('Amasya','Amasya'),
        ('Ankara','Ankara'),
        ('Antalya','Antalya'),
        ('Artvin','Artvin'),
        ('Aydın','Aydın'),
        ('Balıkesir','Balıkesir'),
        ('Bilecik','Bilecik'),
        ('Bingöl','Bingöl'),
        ('Bitlis','Bitlis'),
        ('Bolu','Bolu'),
        ('Burdur','Burdur'),
        ('Bursa','Bursa'),
        ('Çanakkale','Çanakkale'),
        ('Çankırı','Çankırı'),
        ('Çorum','Çorum'),
        ('Denizli','Denizli'),
        ('Diyarbakır','Diyarbakır'),
        ('Edirne','Edirne'),
        ('Elazığ','Elazığ'),
        ('Erzincan','Erzincan'),
        ('Erzurum','Erzurum'),
        ('Eskişehir','Eskişehir'),
        ('Gaziantep','Gaziantep'),
        ('Giresun','Giresun'),
        ('Gümüşhane','Gümüşhane'),
        ('Hakkari','Hakkari'),
        ('Hatay','Hatay'),
        ('Isparta','Isparta'),
        ('Mersin','Mersin'),
        ('İstanbul','İstanbul'),
        ('İzmir','İzmir'),
        ('Kars','Kars'),
        ('Kastamonu','Kastamonu'),
        ('Kayseri','Kayseri'),
        ('Kırklareli','Kırklareli'),
        ('Kırşehir','Kırşehir'),
        ('Kocaeli','Kocaeli'),
        ('Konya','Konya'),
        ('Kütahya','Kütahya'),
        ('Malatya','Malatya'),
        ('Manisa','Manisa'),
        ('Kahramanmaraş','Kahramanmaraş'),
        ('Mardin','Mardin'),
        ('Muğla','Muğla'),
        ('Muş','Muş'),
        ('Nevşehir','Nevşehir'),
        ('Niğde','Niğde'),
        ('Ordu','Ordu'),
        ('Rize','Rize'),
        ('Sakarya','Sakarya'),
        ('Samsun','Samsun'),
        ('Siirt','Siirt'),
        ('Sinop','Sinop'),
        ('Sivas','Sivas'),
        ('Tekirdağ','Tekirdağ'),
        ('Tokat','Tokat'),
        ('Trabzon','Trabzon'),
        ('Tunceli','Tunceli'),
        ('Şanlıurfa','Şanlıurfa'),
        ('Uşak','Uşak'),
        ('Van','Van'),
        ('Yozgat','Yozgat'),
        ('Zonguldak','Zonguldak'),
        ('Aksaray','Aksaray'),
        ('Bayburt','Bayburt'),
        ('Karaman','Karaman'),
        ('Kırıkkale','Kırıkkale'),
        ('Batman','Batman'),
        ('Şırnak','Şırnak'),
        ('Bartın','Bartın'),
        ('Ardahan','Ardahan'),
        ('Iğdır','Iğdır'),
        ('Yalova','Yalova'),
        ('Karabük','Karabük'),
        ('Kilis','Kilis'),
        ('Osmaniye','Osmaniye'),
        ('Düzce','Düzce'),
    )
    Job_Choices=(
        ('Doktor','Doktor'),
        ('Ev Hanımı','Ev Hanımı'),
        ('Öğretmen','Öğretmen'),
        ('Mühendis','Mühendis'),
        ('Şoför','Şoför'),
        ('Garson','Garson'),
        ('Diğer','Diğer'),
    )
    Education_Choices=(
        ('İlkokul','İlkokul'),
        ('Lise','Lise'),
        ('Lisans','Lisans'),
        ('Master','Master'),
        ('Okumadı','Okumadı'),

    )

    image= models.ImageField(null=True,blank=True,verbose_name='Fotoğraf')
    name_surname=models.CharField(max_length=120,verbose_name='Ad Soyad')
    tc_no=models.CharField(max_length=11,verbose_name='TC Kimlik Numarası')
    email=models.CharField(max_length=120,verbose_name='Email')
    phone_number=models.CharField(max_length=14,verbose_name='Telefon')
    address=models.CharField(max_length=150,verbose_name='Adres')
    city=models.CharField(max_length=120,verbose_name='Yaşadığı Şehir',choices=City_Choices)
    job=models.CharField(max_length=120,verbose_name='Meslek',choices=Job_Choices)
    education_grade=models.CharField(max_length=120,verbose_name='Eğitim Düzeyi',choices=Education_Choices)
    birthdate=models.DateField(verbose_name='Doğum Tarihi')
    referrence=models.CharField(max_length=120,verbose_name='Referans Kodu')
    confirmation=models.BooleanField(verbose_name='')