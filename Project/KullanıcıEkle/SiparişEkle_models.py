from django.db import models
from django.urls import reverse

class İl(models.Model):
    il=models.CharField(max_length=100,verbose_name='İl')

    def __str__(self):
        return self.il

class İlçe(models.Model):
    il=models.ForeignKey(İl,on_delete=models.CASCADE)#il in id si
    ilçe=models.CharField(max_length=100,verbose_name='İlçe')

    def __str__(self):
        return self.ilçe

class SiparişEkle(models.Model):
    kullanıcı=models.CharField(max_length=100,verbose_name='Kullanıcı')
    ürün=models.CharField(blank=False,max_length=120,verbose_name='Ürün Adı')
    #şehir=models.ForeignKey(Şehir, on_delete=models.SET_NULL, null=True)
    il=models.ForeignKey(İl,on_delete=models.SET_NULL, null=True,verbose_name='İl')
    ilçe=models.ForeignKey(İlçe,on_delete=models.SET_NULL, null=True,verbose_name='İlçe')
    adet=models.CharField(blank=False,max_length=120,verbose_name='Adet')
    adres=models.CharField(blank=False,max_length=120,verbose_name='Adres')
    kredi=models.BooleanField(verbose_name='Kredi Kartı')
    eft=models.BooleanField(verbose_name='EFT/Havale')
    onayla=models.BooleanField(verbose_name='')

    def __str__(self):
        return self.kullanıcı




