from django.shortcuts import render
from django.views import generic
from store.models import Product
from django_filters.views import FilterView
from store.filters import ProductFilter
from cart.forms import CartForm
from django.db.models import Count

# Create your views here.


class ProductList(FilterView):
    model = Product
    queryset = Product.objects.all()
    paginate_by = 20
    filterset_class = ProductFilter
    context_object_name = "products"
    template_name = "store/product_list.html"


class ProdcutDetails(generic.DetailView):
    model = Product
    template_name = "store/product_details.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super(ProdcutDetails, self).get_context_data(**kwargs)
        context['form'] = CartForm
        return context

    def get_queryset(self):
        product = super().get_queryset()
        return product.annotate(total_purchases=Count('ordered'))
