from rest_framework import serializers
from storeapp.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'title', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'slug', 'inventory', 'old_price', 'price']

    # category = serializers.StringRelatedField()
    category = CategorySerializer()
