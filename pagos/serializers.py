from rest_framework import serializers
from .models import Pago
from clientes.models import Cliente


class PagoSerializer(serializers.ModelSerializer):
    cliente = serializers.CharField(
        source='cliente.nombre_cliente',
        read_only=True
        )
    
    cliente_id = serializers.PrimaryKeyRelatedField(
        source='cliente',
        queryset=Cliente.objects.all(),
        write_only=True
    )
    
    class Meta:
        model = Pago
        fields = [
            'id',
            'fecha_pago',
            'cliente',
            'cliente_id',
            'total_pago',
            'metodo_pago',
            'estado_pago',
        ]
        
    