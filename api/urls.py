from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


# for ModelViewSet

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = router.urls



# for Class-based views and Generics views

# urlpatterns = [
    # path('products/', views.ApiProducts.as_view()),
    # path('products/<str:pk>', views.ApiProduct.as_view()),
    # path('categories/', views.ApiCategories.as_view()),
    # path('categories/<str:pk>', views.ApiCategory.as_view()),
# ]


# for api_views

# urlpatterns = [
    # path('products/', views.ApiProducts),
    # path('products/<str:pk>', views.ApiProduct),
    # path('categories/', views.ApiCategories),
    # path('categories/<str:pk>', views.ApiCategory),
# ]