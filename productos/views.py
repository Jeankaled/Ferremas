from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from rest_framework import generics
from .models import Producto, CategoriaProducto, PrecioProducto
from .serializers import ProductoSerializer, CategoriaProductoSerializer, PrecioProductoSerializer

class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
    
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    
class PrecioProductoViewSet(viewsets.ModelViewSet):
    queryset = PrecioProducto.objects.all()
    serializer_class = PrecioProductoSerializer
    
