from django.shortcuts import render
from rest_framework import generics
from .models import Pedido, Detalle_Pedido
from .serializers import PedidoSerializer, DetallePedidoSerializer

# Create your views here.


class PedidoListCreateView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    

class PedidoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
class Detalle_PedidoListCreateView(generics.ListCreateAPIView):
    queryset = Detalle_Pedido.objects.all()
    serializer_class = DetallePedidoSerializer
    
class Detalle_PedidoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detalle_Pedido.objects.all()
    serializer_class = DetallePedidoSerializer
    
class ClientePedidoList(generics.ListCreateAPIView):
    serializer_class = PedidoSerializer

    def get_queryset(self):
        cliente_id = self.kwargs['cliente_id']
        return Pedido.objects.filter(cliente__id=cliente_id)
    
class ClientePedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PedidoSerializer

    def get_queryset(self):
        cliente_id = self.kwargs['cliente_id']
        return Pedido.objects.filter(cliente__id=cliente_id)

  