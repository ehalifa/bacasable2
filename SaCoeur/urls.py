from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^building/$', BuildingList.as_view(), name= 'building'),
    url(r'^product/list_stock/$', ProductList.as_view(), name='products'),
    url(r'^product/list_stock/(?P<product_type>[\w]*)$', ProductList.as_view(), name='products'),
    url(r'^product/list_crud/$', ProductToCRUD.as_view(), name='producttocrud'),
    url(r'^product/new/$', CreateProduct.as_view(), name='new_product'),
    url(r'^product/update/(?P<pk>[\d]+)$', UpdateProduct.as_view (), name='update_product'),
    url(r'^product/delete/(?P<pk>[\d]+)$', DeleteProduct.as_view (), name='delete_product'),
    url(r'^product/detail/(?P<pk>[-\d]+)$', ProductDetail.as_view (), name='product_detail'),
]
