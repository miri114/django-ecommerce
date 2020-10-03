import django_filters
from store.models import Category, Product


class ProductFilter(django_filters.FilterSet):
    price1 = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price2 = django_filters.NumberFilter(field_name="price", lookup_expr="lt")
    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains", widget=django_filters.widgets.forms.HiddenInput())

    class Meta:
        model = Product
        fields = ('name',)
