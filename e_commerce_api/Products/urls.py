from django.urls import path
from .views import get_products, create_products, product_detail

urlpatterns = [
    path("get_products/", get_products, name="get_products"),
    path("create_products/", create_products, name="create_products"),
    path("product_detail/<int:pk>", product_detail, name="product_detail"),
]