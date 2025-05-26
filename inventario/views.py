from django.shortcuts import render
from rest_framework import generics
from .models import Inventario
from .serializers import InventarioSerializer

# Create your views here.

class InventarioList(generics.ListCreateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    
class InventarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    
class productoInventarioList(generics.ListCreateAPIView):
    serializer_class = InventarioSerializer

    def get_queryset(self):
        producto_id = self.kwargs['producto_id']
        return Inventario.objects.filter(producto__id=producto_id)
    
class productoInventarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InventarioSerializer

    def get_queryset(self):
        producto_id = self.kwargs['producto_id']
        return Inventario.objects.filter(producto__id=producto_id)
    
