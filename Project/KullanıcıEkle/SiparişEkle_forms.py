from django import forms
from django.forms import ModelForm
from .SiparişEkle_models import SiparişEkle,İlçe

class SiparişEkleForm(forms.ModelForm):

    class Meta:
        model = SiparişEkle
        fields = [
            "kullanıcı",
            "ürün",
            "il",
            "ilçe",
            "adet",
            "adres",
            "kredi",
            "eft",
            "onayla",

        ]

        widgets = {
            'kullanıcı': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı'}),
            'ürün': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ürün'}),
            'il': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İl'}),
            'İlçe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İlçe'}),
            'adet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adet'}),
            'adres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adres'}),
            'kredi':forms.CheckboxInput(attrs={'class': 'iCheck-helper'}),
            'eft':forms.CheckboxInput(attrs={'class': 'iCheck-helper'}),
            'onayla': forms.CheckboxInput(attrs={'class': 'iCheck-helper'}),

        }

    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  self.fields['ilçe'].queryset = İlçe.objects.none()
#
 #       if 'il' in self.data:
  #          try:
   #             id = int(self.data.get('il'))
    #            self.fields['ilçe'].queryset = City.objects.filter(id=id).order_by('ilçe')
     #       except (ValueError, TypeError):
      #          pass  # invalid input from the client; ignore and fallback to empty City queryset
       # elif self.instance.pk:
        #    self.fields['ilçe'].queryset = self.instance.country.city_set.order_by('ilçe')




