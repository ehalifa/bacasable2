from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.db.models import Count
from django.urls import reverse_lazy,reverse


class HomePageView(TemplateView):
    template_name = "index.html"


class BuildingList(ListView):
    model = Building
    template_name = "building_list.html"
    context_object_name = "building_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.values("name","type","capacity","id").order_by("type").annotate( total_product = Count("product__id_product_description__name"))
        return queryset

#TODO_DONE En tant que vendeur, je dois pouvoir visualiser la disponibilité d’un produit afin de connaitre le délai de livraison des produits pour en acheter un
#TODO_DONE En tant que coordinateur, je dois pouvoir visualiser la disponibilité d’un produit afin de savoir si un produit est en stock et s’il faut en acheter un
#TODO_DONE En tant que magasinier, je dois pouvoir visualiser la disponibilité d’un produit afin de savoir si un mouvement de stock est possible
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

#TODO_DONE En tant que magasinier, je dois pouvoir ajouter des produits entrant afin d’actualiser les stocks
class ProductToCRUD(ListView):
    model = Product
    template_name = "product_tocrud.html"
    context_object_name = "product_crud"

    def get_queryset(self):
        result = super(ProductToCRUD, self).get_queryset()
        result = result.values('id_product_description__name', 'id_building__name', 'id')
        query = self.request.GET.get("q")
        if query:
            result = result.filter(id_product_description__name__icontains = query)
        return result


#TODO_DONE En tant que coordinateur, je dois pouvoir visualiser les stocks des magasins et de l’entrepôt afin de les suivre
class ProductByBuilding(ListView):
    model = Product
    template_name = "product_building.html"
    context_object_name = "product_building"

    def get_queryset(self, **kwargs):
        result = super(ProductByBuilding,self).get_queryset()
        result = result.values('id_product_description__name', 'arrival_date', 'id', 'id_building').annotate(bagnb = Count('id_product_description'))
        query = self.kwargs['id_building']

        if query:
            result = result.filter(id_building = query)
        return result

#TODO_DONE En tant que magasinier, je dois pouvoir enregistrer les mouvements de stock afin de contrôler les mouvements des produits
class CreateProduct(CreateView):
    model = Product
    fields = ('arrival_date', 'id_building', 'id_product_description')
    template_name = "new_product.html"
    success_url = reverse_lazy('producttocrud')

    def get_absolute_url(self):
        return reverse('producttocrud')

#TODO_DONE En tant que magasinier, je dois pouvoir enregistrer les mouvements de stock afin de contrôler les mouvements des produits
class UpdateProduct(UpdateView):
    model = Product
    fields = ('arrival_date', 'id_building', 'id_product_description')
    template_name = "update_product.html"
    success_url = reverse_lazy('producttocrud')
    context_object_name = "products"

    def get_absolute_url(self):
        return reverse('producttocrud')

#TODO_DONE En tant que magasinier, je dois pouvoir enregistrer les mouvements de stock afin de contrôler les mouvements des produits
class DeleteProduct(DeleteView):
    model = Product
    fields = ('arrival_date', 'id_building', 'id_product_description')
    template_name = "delete_product.html"
    success_url = reverse_lazy('producttocrud')
    context_object_name = "products"

    def get_absolute_url(self):
        return reverse('producttocrud')
