from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    def list(self, request): # GET/api/products/
        print(request)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request): # POST /api/products/
            pass
    
    def retrieve(self, request, pk=None): # GET /api/products/<str:id>/
         pass
    
    def update(self, request, pk=None): # GET /api/products/<str:id>/
         pass
    
    def destroy(self, request, pk=None): # GET /api/products/<str:id>/
         pass