from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.urls import reverse, reverse_lazy

# Create your views here.
class ProductList(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "product"
    list = Product.objects.values('id_product_description')
