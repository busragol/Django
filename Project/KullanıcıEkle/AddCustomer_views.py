from django.shortcuts import render
from .AddCustomer_models import AddCustomer
from .AddCustomer_forms import AddCustomerForm
# Create your views here.
def AddCustomer_create(request,*args,**kwargs):

    form = AddCustomerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        form.save()


    context={
        'form':form,
    }
    return render(request,'AddCustomer.html',context)