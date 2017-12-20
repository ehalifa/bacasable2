from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^building/$', BuildingList.as_view(), name= 'building'),
    url (r'^products/$', ProductList.as_view(), name='products'),
    #url (r'^(?P<pk>\d+)$', ProductDetailList.as_view(), name='product-details'),
]
