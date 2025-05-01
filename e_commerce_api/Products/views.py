from django.shortcuts import render
from .serializer import ProductSerializer
from rest_framework.response import Response
from .models import Products
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_products(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data) 