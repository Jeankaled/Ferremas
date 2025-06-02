from django.shortcuts import render
from rest_framework import viewsets
from .models import Pedido, Detalle_Pedido
from .serializers import PedidoSerializer, DetallePedidoSerializer

# Create your views here.

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Pedido.objects.all()
    serializer_class = DetallePedidoSerializer
    
class PedidoClienteViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer

    def get_queryset(self):
        cliente_id = self.kwargs.get('cliente_id')
        return Pedido.objects.filter(cliente_id=cliente_id)

    def perform_create(self, serializer):
        cliente_id = self.kwargs.get('cliente_id')
        serializer.save(cliente_id=cliente_id)
        

    