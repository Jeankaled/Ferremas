from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Producto, CategoriaProducto, PrecioProducto
from .serializers import ProductoSerializer, CategoriaProductoSerializer, PrecioProductoSerializer

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    
class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    
class CategoriaProductoList(generics.ListCreateAPIView):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
    
    
class CategoriaProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
    
    
class PrecioProductoList(generics.ListCreateAPIView):
    queryset = PrecioProducto.objects.all()
    serializer_class = PrecioProductoSerializer
    
    
class PrecioProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrecioProducto.objects.all()
    serializer_class = PrecioProductoSerializer