from django.shortcuts import render
from rest_framework import generics
from .models import Pago
from .serializers import PagoSerializer


# Create your views here.


class PagoList(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    
class PagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    
class ClientePagoList(generics.ListCreateAPIView):
    serializer_class = PagoSerializer
    
    def get_queryset(self):
        cliente_id = self.kwargs['cliente_id']
        return Pago.objects.filter(cliente__id=cliente_id)
    
class ClientePagoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PagoSerializer
    
    def get_queryset(self):
        cliente_id = self.kwargs['cliente_id']
        return Pago.objects.filter(cliente__id=cliente_id)
    
