from django.contrib import admin
from .AddUser_models import AddUser
from .AddProduct_models import AddProduct
from .SiparişEkle_models import SiparişEkle,İl,İlçe
from .AddCustomer_models import AddCustomer

# Register your models here.
class AddUserAdmin(admin.ModelAdmin):
   list_display=['name_surname','tc_no','email','phone_number','address','birthdate']
   list_display_links=['name_surname']


admin.site.register(AddUser,AddUserAdmin)#modeli admin paneline bağlamak için




# Register your models here.
class AddProductAdmin(admin.ModelAdmin):
   list_display=['name','price','discount']
   list_display_links=['name']


admin.site.register(AddProduct,AddProductAdmin)

class SiparişEkleAdmin(admin.ModelAdmin):
   list_display = ['kullanıcı', 'adet', 'ürün']
   list_display_links = ['kullanıcı']
admin.site.register(SiparişEkle,SiparişEkleAdmin)



class İlAdmin(admin.ModelAdmin):
   list_display = ['il']
   list_display_links = ['il']


admin.site.register(İl, İlAdmin)

class İlçeAdmin(admin.ModelAdmin):
   list_display = ['il','ilçe']
   list_display_links = ['il','ilçe']

admin.site.register(İlçe, İlçeAdmin)

class AddCustomerAdmin(admin.ModelAdmin):
   list_display=['name_surname','tc_no','email','phone_number','address','birthdate']
   list_display_links=['name_surname']

admin.site.register(AddCustomer,AddCustomerAdmin)





