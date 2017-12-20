from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^building/$', BuildingList.as_view(), name= 'building'),
    url (r'^products/$', ProductList.as_view(), name='products'),
    url (r'^products/(?P<product_type>[\w]*)$', ProductList.as_view(), name='products'),
]
