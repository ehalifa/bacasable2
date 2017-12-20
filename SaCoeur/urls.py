from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^building/$', BuildingList.as_view(), name= 'building'),
    url (r'^products/$', ProductList.as_view(), name='products'),
    url (r'^products/(?P<product_type>[\w]*)$', ProductList.as_view(), name='products'),
    url (r'^products/details/(?P<pk>[-\d]+)$', ProductDetail.as_view (), name='product_detail'),
    url(r'^productstocrud/$', ProductToCRUD.as_view(), name='producttocrud'),
    url (r'^products/details/new/$', CreateProduct.as_view(), name='new_product'),
    url (r'^products/details/update/(?P<pk>[\d]+)$', UpdateProduct.as_view (), name='update_product'),
    url (r'^products/details/delete/(?P<pk>[\d]+)$', DeleteProduct.as_view (), name='delete_product'),
]
