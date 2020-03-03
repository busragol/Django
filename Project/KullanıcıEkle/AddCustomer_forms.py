from django.forms import ModelForm
from .AddCustomer_models import AddCustomer
from django import forms


class AddCustomerForm(forms.ModelForm):
    image= forms.ImageField(label='Fotoğraf',required=False,widget=forms.ClearableFileInput(
        attrs={'class': 'form-control-file'}))
    class Meta:
        model=AddCustomer
        fields=[
            "image",
            "name_surname",
            "tc_no",
            "email",
            "phone_number",
            "address",
            "city",
            "job",
            "education_grade",
            "birthdate",
            "referrence",
            "confirmation",

        ]


        widgets={
            'name_surname':forms.TextInput(attrs={'class':'form-control','placeholder':'Ad Soyad'}),
            'tc_no':forms.TextInput(attrs={'class':'form-control','placeholder':'TC Kimlik Numarası'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Telefon Numarası'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Adres'}),
            'city':forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%;'}),
            'job':forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%;'}),
            'education_grade':forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%;'}),
            'birthdate':forms.DateInput(
                attrs={'class': 'form-control  pull-right' , 'id':'datepicker','placeholder':'Seçiniz'}),
            'referrence':forms.TextInput(attrs={'class':'form-control','placeholder':'Referans Kodu','required':'required'}),
            'confirmation': forms.CheckboxInput(attrs={'class': 'iCheck-helper'}),


        }

    def __init__(self, *args, **kwargs):
        super(AddCustomerForm, self).__init__(*args, **kwargs)
        self.fields["city"].choices = [("", "Seçiniz"), ] + list(
            self.fields["city"].choices)[1:]
        self.fields["job"].choices = [("", "Seçiniz"), ] + list(
           self.fields["job"].choices)[1:]
        self.fields["education_grade"].choices = [("", "Seçiniz"), ] + list(
           self.fields["education_grade"].choices)[1:]


