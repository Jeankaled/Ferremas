from django.shortcuts import render
from rest_framework import viewsets
from .models import Inventario
from .serializers import InventarioSerializer

# Create your views here.

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    
  
class ProductoInventarioViewSet(viewsets.ModelViewSet):
    serializer_class = InventarioSerializer

    
    def get_queryset(self):
      producto_id = self.kwargs.get('producto_id')
      return Inventario.objects.filter(producto_id=producto_id)
  
    def perform_create(self, serializer):
        producto_id = self.kwargs.get('producto_id')
        serializer.save(producto_id=producto_id)