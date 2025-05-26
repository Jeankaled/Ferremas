from rest_framework import serializers
from .models import Pago


class PagoSerializer(serializers.ModelSerializer):
    cliente = serializers.CharField(source='cliente.nombre_cliente', read_only=True)
    
    class Meta:
        model = Pago
        fields = [
            'id',
            'fecha_pago',
            'cliente',
            'total_pago',
            'metodo_pago',
            'estado_pago',
        ]
        
    