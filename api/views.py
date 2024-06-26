from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from storeapp.models import Product, Category, Review
from .filters import ProductFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


# viewsets
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['old_price']  # sorts ascending or descending

    pagination_class = PageNumberPagination


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['productt_pk'])

    def get_serializer_context(self):
        return {"product_id": self.kwargs["productt_pk"]}


# generics views ebis sashualebit bevrad martivad vagvarebt saqmes, ar gvchirdeba zedmetad post da get requestebis gawera

# Generics views

# # 1
# class ApiProducts(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# # 2
# class ApiProduct(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# # 3
# class ApiCategories(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# # 4
# class ApiCategory(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# The two functions api_products and ApiProducts achieve the same functionality of
# handling GET and POST requests for a RESTful API endpoint that deals with Product
# objects. However, they use different approaches provided by Django REST framework.

# In summary, both approaches achieve the same goal, but the class-based view provides a
# more structured and organized way to define views, especially for more complex views that
# require additional methods or functionalities.


# # Class-based view (APIView)


# 1

# class ApiProducts(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# 2

# class ApiProduct(APIView):
#     def get(self, request, pk):
#         product = get_object_or_404(Product, id=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         product = get_object_or_404(Product, id=pk)
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         product = get_object_or_404(Product, id=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# 3
# class ApiCategories(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# 4
# class ApiCategory(APIView):
#     def get(self, request, pk):
#         category = get_object_or_404(Category, category_id=pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         category = get_object_or_404(Category, category_id=pk)
#         serializer = CategorySerializer(category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#
#     def delete(self, request, pk):
#         category = get_object_or_404(Category, category_id=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Function-based view (api_view decorator)


# 1

# @api_view(['GET', 'POST'])
# def api_products(request):
#      # Serializing
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#     # Deserializing
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # if serializer.is_valid():
#         #     serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# 2

# @api_view(['GET', 'PUT', 'DELETE'])
# def api_product(request, pk):
#     product = get_object_or_404(Product, id=pk)
#
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#
#         # simple version 1
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         # # version 2
#         # if serializer.is_valid():
#         #     serializer.save()
#         # else:
#         #     return Response(serializer.errors)
#
#         return Response(serializer.data)
#
#     if request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# 3

# @api_view(['GET', 'POST'])
# def api_categories(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# 4

# @api_view(['GET', 'PUT', 'DELETE'])
# def api_category(request, pk):
#     category = get_object_or_404(Category, category_id=pk)
#
#     if request.method == 'GET':
#         serializer = CategorySerializer(category)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == 'PUT':
#         serializer = CategorySerializer(category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == 'DELETE':
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
