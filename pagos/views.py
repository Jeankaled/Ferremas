from django.shortcuts import render
from rest_framework import viewsets
from .models import Pago
from .serializers import PagoSerializer


# Create your views here.

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    
    
class PagoClienteViewSet(viewsets.ModelViewSet):
    serializer_class = PagoSerializer

    def get_queryset(self):
        cliente_id = self.kwargs.get('cliente_id')
        return Pago.objects.filter(cliente_id=cliente_id)

    def perform_create(self, serializer):
        cliente_id = self.kwargs.get('cliente_id')
        serializer.save(cliente_id=cliente_id)
        
        