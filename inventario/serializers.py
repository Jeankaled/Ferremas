from rest_framework import serializers
from .models import Inventario


class InventarioSerializer(serializers.ModelSerializer):
    producto = serializers.CharField(source='producto.nombre_producto', read_only=True)
    
    class Meta:
        model = Inventario
        fields = [
            'id',
            'fecha_ingreso',
            'cantidad_disponible',
            'producto',
        ]
        
    