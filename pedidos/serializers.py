from rest_framework import serializers
from .models import Detalle_Pedido, Pedido
from productos.models import Producto, CategoriaProducto, PrecioProducto
from clientes.models import Cliente


class DetallePedidoSerializer(serializers.ModelSerializer):
    producto = serializers.CharField(source='producto.nombre_producto', read_only=True)
    class Meta:
        model = Detalle_Pedido
        fields = [
            'id',
            'pedido',
            'producto',
            'cantidad',
            'precio_unitario',
        ]


class PedidoSerializer(serializers.ModelSerializer):
    Cliente = serializers.CharField(source='cliente.nombre_cliente', read_only=True)
    detalles = DetallePedidoSerializer(many=True, read_only=True)
    class Meta:
        model = Pedido
        fields = [
            'id',
            'fecha_pedido',
            'cliente',
            'total_pedido',
            'metodo_pago',
            'estado_pedido',
            'detalles'
        ]