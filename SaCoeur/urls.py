from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^product/$', ProductList.as_view(), name= 'product')
]
