from django import forms
from .AddProduct_models import AddProduct
from django.forms import ModelForm

class AddProductForm(forms.ModelForm):
    image1 = forms.ImageField(required=False,label='Ürün Ana Görseli',widget=forms.ClearableFileInput(
    attrs={'class': 'form-control-file'}))

    image2 = forms.ImageField(required=False,label='Ürün Galeri',widget=forms.ClearableFileInput(
        attrs={'class': 'form-control-file'}))

    class Meta:
        model=AddProduct
        fields=[
            'name',
            'price',
            'discount',
            'available_number',
            'category',
            'tag',
            'range1',
            'range2',
            'image1',
            'image2',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ürün Adı'}),

            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ürün Fiyatı'}),

            'discount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İndirimli Fiyatı'}),

            'available_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Stok Adedi'}),

            'category': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                         'style': 'width: 100%;'}),

            'tag': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%;'}),


            'range1': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker','placeholder':'Seçiniz'}),

            'range2': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker2','placeholder':'Seçiniz'}),




        }

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields["category"].choices = [("", "Seçiniz"), ] + list(
            self.fields["category"].choices)[1:]
        self.fields["tag"].choices = [("", "Seçiniz"), ] + list(
           self.fields["tag"].choices)[1:]

