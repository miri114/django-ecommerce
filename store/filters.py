import django_filters
from store.models import Category, Product


class ProductFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        label="Categories", queryset=Category.objects.all())
    price1 = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price2 = django_filters.NumberFilter(field_name="price", lookup_expr="lt")

    class Meta:
        model = Product
        fields = ('category',)
