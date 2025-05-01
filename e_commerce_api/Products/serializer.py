from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["name", "description", "price", "qty", "in_stock", "created_at"]