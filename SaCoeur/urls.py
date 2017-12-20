from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^building/$', BuildingList.as_view(), name= 'building'),
    url (r'^products/$', ProductList.as_view(), name='products'),
    url (r'^products/(?P<product_type>[\w]*)$', ProductList.as_view(), name='products'),
    url (r'^products/details/(?P<pk>[-\d]+)$', ProductDetail.as_view (), name='product_detail'),
    #url (r'^products/new_product/$', CreateProduct.as_view(), name='new_product'),

]
