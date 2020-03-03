from django.db import models
from django.urls import reverse




class AddProduct(models.Model):

    Category_Choices=(
        ('Otomotiv','Otomotiv'),
        ('Sağlık','Sağlık'),
        ('Eğitim','Eğitim'),
    )

    Tag_Choices=(
        ('Yeni','Yeni'),
        ('Son3','Son3'),
        ('Son2','Son2'),
        ('Özel','Özel'),
        ('Stok Yok','Stok Yok'),
    )
    name= models.CharField(blank=False, max_length=120, verbose_name='Ürün Adı')
    price=models.CharField(blank=False,max_length=120,verbose_name='Ürün Fiyatı')
    discount=models.CharField(blank=False,max_length=120,verbose_name='İndirimli Fiyatı')
    available_number=models.CharField(blank=False,max_length=120,verbose_name='Stok Adedi')
    category=models.CharField(blank=False,max_length=120,verbose_name='Ürün Kategorisi',choices=Category_Choices)
    tag=models.CharField(blank=False,max_length=120,verbose_name='Ürün Tag',choices=Tag_Choices)
    range1=models.DateField(blank=False,verbose_name='İndirimli Fiyat Aralığı')
    range2=models.DateField(blank=False,verbose_name='')
    image1=models.ImageField(null=True,blank=True,verbose_name='Ürün Ana Görseli')
    image2=models.ImageField(null=True,blank=True,verbose_name='Ürün Galeri')