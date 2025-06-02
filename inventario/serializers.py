from rest_framework import serializers
from .models import Inventario
from productos.models import Producto


class InventarioSerializer(serializers.ModelSerializer):
    producto = serializers.CharField(
        source='producto.nombre_producto', 
        read_only=True
        )
    
    producto_id = serializers.PrimaryKeyRelatedField(
        source='producto',
        queryset=Producto.objects.all(),
        write_only=True
    )
    
    class Meta:
        model = Inventario
        fields = [
            'id',
            'fecha_ingreso',
            'cantidad_disponible',
            'producto',
            'producto_id'
        ]
        
    