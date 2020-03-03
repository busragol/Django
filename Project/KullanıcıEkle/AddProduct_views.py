from django.shortcuts import render
from .AddProduct_models import AddProduct
from .AddProduct_forms import AddProductForm

def AddProduct_create(request,*args,**kwargs):

    form2 = AddProductForm(request.POST or None,request.FILES or None)

    if form2.is_valid():
        form2.save()


    context={
        'form2':form2,
    }
    return render(request,'AddProduct.html',context)
