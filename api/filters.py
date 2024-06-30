from django_filters.rest_framework import FilterSet
from storeapp.models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt']  # means lass than and greater than
        }
