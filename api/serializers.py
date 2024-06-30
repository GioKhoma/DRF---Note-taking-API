from rest_framework import serializers
from storeapp.models import Product, Category, Review, Cart, Cartitems


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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date_created', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    sub_total = serializers.SerializerMethodField(method_name='total')

    class Meta:
        model = Cartitems
        fields = ['id', 'cart', 'product', 'quantity', 'sub_total']

    def total(self, cartitem: Cartitems):
        return cartitem.quantity * cartitem.product.price


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    itemsss = CartItemSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')

    class Meta:
        model = Cart
        fields = ['id', 'itemsss', 'grand_total']

    def main_total(self, cart: Cart):
        items = cart.itemsss.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total
