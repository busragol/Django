from django import forms
from .AddUser_models import AddUser
from django.forms import ModelForm



class AddUserForm(forms.ModelForm):
    image= forms.ImageField(label='Fotoğraf',required=False,widget=forms.ClearableFileInput(
        attrs={'class': 'form-control-file'}))
    class Meta:
        model=AddUser
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
                                           'style': 'width: 100%;'}),#'placeholder':'Seçiniz','allowClear':'True', bu kısıma bak search için
            'job':forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%;'}),
            'education_grade':forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%;'}),
            'birthdate':forms.DateInput(
                attrs={'class': 'form-control  pull-right' , 'id':'datepicker','placeholder':'Seçiniz'}),#type ı kullanıcıya gün seçtirebilmek
                                                                                               # için ekliyoruz
            'referrence':forms.TextInput(attrs={'class':'form-control','placeholder':'Referans Kodu'}),
            'confirmation': forms.CheckboxInput(attrs={'class': 'iCheck-helper'}),


        }

    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        self.fields["city"].choices = [("", "Seçiniz"), ] + list(
            self.fields["city"].choices)[1:]
        self.fields["job"].choices = [("", "Seçiniz"), ] + list(
           self.fields["job"].choices)[1:]
        self.fields["education_grade"].choices = [("", "Seçiniz"), ] + list(
           self.fields["education_grade"].choices)[1:]


