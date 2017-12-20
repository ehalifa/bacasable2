from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.db.models import Count

class BuildingList(ListView):
    model = Building
    template_name = "building_list.html"
    context_object_name = "building_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.values("name","type","capacity").order_by("type").annotate( total_product = Count("product__id_product_description__name"))
        return queryset

class ProductList(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "product_list"


    def get_queryset(self):
        result = super(ProductList, self).get_queryset()
        result = result.values('id_product_description__name', 'id_building__name').annotate(bagnb = Count('id_product_description'))
        query = self.request.GET.get('q')
        if query:
            result = result.filter(id_product_description__name__icontains = query)
        return result

class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product_detail"

class CreateProduct(CreateView):
    model = Product
    fields = ('arrival_date', 'id_building', 'id_product_description')