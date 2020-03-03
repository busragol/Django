from django.shortcuts import render
from .AddUser_models import AddUser
from .AddUser_forms import AddUserForm
# Create your views here.
def AddUser_create(request,*args,**kwargs):

    form = AddUserForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        form.save()


    context={
        'form':form,
    }
    return render(request,'AddUser.html',context)
def KullanıcıEkle_home(request,*args,**kwargs):
    context={
        'isim':'büşra',
    }
    return render(request,'home.html',context)