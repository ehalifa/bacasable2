from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.urls import reverse, reverse_lazy
from django.db.models import Count,Sum, Avg

# je dois pouvoir visualiser les stocks des produits dans chaque building
# 1) liste des buildings (order by type of building) dans un premeir temps  "BuildingList(ListView)"
# 2) ensuite liste des produits existants (product description with count query on product class) pour chaque building "ProductList(ListView)"
# 3) finallement on doit pouvoir afficher la description de chaque produit "ProductDetail(DetailView)"

class BuildingList(ListView):
    model = Building
    template_name = "building_list.html"
    context_object_name = "building_list"
    queryset = Building.objects.values("name","type","capacity").order_by("type").annotate( total_product = Count("product__id_product_description__name"))
"""
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.values("id").order_by()
        return queryset
    #queryset = Building.objects.values('product__id_product_description__name').annotate(total = Sum('capacity'),bagnb = Count('product__id_building'))
"""

class ProductList(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "product_list"
    #queryset = Product_Description.objects.values('name','type').annotate(bagnb = Count('product__id_product_description'))
    queryset = Product.objects.values('id_product_description__name', 'id_building__name').annotate(bagnb = Count('id_product_description'))


    def search(request):
        query = request.GET.get('query')
        if not query:
            products = Product.objects.all()
        else:
            products = Product.objects.filter(id_product_description__name__icontains=query)
        if not products.exists():
            products = Product.objects.filter(id_product_description__brand__icontains=query)
        brand = "Résultats pour la requête %s"%query
        context = {
            'product':products,
            'brand' : brand
        }
        return render(request, 'product_list.html', context)

"""
class ProductDetailList(DetailView):
    XXXX
"""
