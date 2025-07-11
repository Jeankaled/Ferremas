from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import Producto, CategoriaProducto, PrecioProducto
from .serializers import ProductoSerializer, CategoriaProductoSerializer, PrecioProductoSerializer

# Create your views here.

class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
    
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [AllowAny] 
    
    def get_serializer_context(self):
          ctx = super().get_serializer_context()
          ctx.update({ 'request': self.request })
          return ctx

    
class PrecioProductoViewSet(viewsets.ModelViewSet):
    queryset = PrecioProducto.objects.all()
    serializer_class = PrecioProductoSerializer
    
