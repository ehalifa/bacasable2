from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^building/$', BuildingList.as_view(), name= 'building'),
    url(r'^products/$', ProductList.as_view(), name='products'),
    url(r'^products/(?P<product_type>[\w]*)$', ProductList.as_view(), name='products'),
    url(r'^productstocrud/$', ProductToCRUD.as_view(), name='productstocrud'),
    url(r'^productstocrud/(?P<product_type>[\w]*)$', ProductToCRUD.as_view(), name='productstocrud'),
    url(r'^productdetail/?P<pk>\d+/$', ProductDetail.as_view(), name='productdetail')
    # url(r'^product/(?P<id_building>\d+)', ProductListFilter.as_view(), name='product_filter')
]
