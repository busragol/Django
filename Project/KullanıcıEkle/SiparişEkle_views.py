from django.shortcuts import render
from .AddUser_models import AddUser
from .AddProduct_models import AddProduct
from .SiparişEkle_models import SiparişEkle,İl,İlçe
from .SiparişEkle_forms import SiparişEkleForm

def SiparişEkle_create(request,*args,**kwargs):

   form3 = SiparişEkleForm(request.POST or None)

   if form3.is_valid():
       form3.save()

   iller = İl.objects.all()
   #il=request.GET.get('il')
   #ilçeler=İlçe.objects.filter(il=il).order_by('ilçe')
   kullanıcı_list = AddUser.objects.all()
   ürün_list = AddProduct.objects.all()





   context={
       'form3':form3,
       #'ilçeler':ilçeler,
       'iller':iller,
       'kullanıcı_list':kullanıcı_list,
       'ürün_list':ürün_list,
   }

   return render(request,'SiparişEkle.html',context)

def SiparişEkle_İlçeler(request):
    il_id = request.GET.get('il')
    ilçeler = İlçe.objects.filter(il_id=il_id).order_by('ilçe')
    return render(request, 'forms.html', {'ilçeler': ilçeler})

