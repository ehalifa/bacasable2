from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.db.models import Count,Sum, Avg
from django.shortcuts import get_object_or_404
from django.db.models import Q

# je dois pouvoir visualiser les stocks des produits dans chaque building
# 1) liste des buildings (order by type of building) dans un premeir temps  "BuildingList(ListView)"
# 2) ensuite liste des produits existants (product description with count query on product class) pour chaque building "ProductList(ListView)"
# 3) finallement on doit pouvoir afficher la description de chaque produit "ProductDetail(DetailView)"

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
