from django.conf.urls import url
from .AddUser_views import *
from .AddProduct_views import *
from .SiparişEkle_views import SiparişEkle_create,SiparişEkle_İlçeler
from .BekleyenKullanıcılar_views import BekleyenKullanıcılar_create,BekleyenKullanıcılar_delete
from .AddCustomer_views import AddCustomer_create
from .UserList_views import UserList_create,UserList_update
urlpatterns = [

    url(r'^Usercreate/$', AddUser_create,name='AddUsercreate'),
    url(r'^$', KullanıcıEkle_home, name='home'),
    url(r'^Productcreate/$', AddProduct_create,name='AddProductcreate'),
    url(r'^Siparişcreate/$', SiparişEkle_create, name='Siparişcreate'),
    url(r'^SiparişEkleİlçeler/$', SiparişEkle_İlçeler, name='SiparişEkleİlçeler'),
    url(r'^BekleyenKullanıcılar/$',BekleyenKullanıcılar_create,name='BekleyenKullanıcılar'),
    url(r'^(?P<id>\d+)/delete/$',BekleyenKullanıcılar_delete,name='delete'),
    url(r'^(?P<id>\d+)/update/$',UserList_update,name='update'),
    url(r'^Customercreate/$', AddCustomer_create, name='AddCustomercreate'),
    url(r'^UserList/$', UserList_create, name='UserListcreate'),

]