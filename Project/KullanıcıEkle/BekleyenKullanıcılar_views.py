from django.shortcuts import render,redirect,get_object_or_404
from .AddUser_models import AddUser

def BekleyenKullanıcılar_create(request,*args,**kwargs):
    kullanıcı_list=AddUser.objects.all()


    context={
        'kullanıcı_list':kullanıcı_list,
    }
    return render(request,'BekleyenKullanıcılar.html',context)


def BekleyenKullanıcılar_delete(request,id,*args,**kwargs):
    kullanıcı = get_object_or_404(AddUser, id=id)
    kullanıcı.delete()
    return redirect('BekleyenKullanıcılar')


