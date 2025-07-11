
# carrito/serializers.py
from rest_framework import serializers
from .models import Cart, CartItem
from productos.models import Producto
from productos.serializers import ProductoSerializer

class CartItemSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model  = CartItem
        fields = ("id", "producto", "cantidad", "subtotal")

    def get_subtotal(self, obj):
        # Usa el helper precio_actual definido en Producto
        return obj.producto.precio_actual * obj.cantidad


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model  = Cart
        fields = ("id", "usuario", "items", "total")

    def get_total(self, obj):
        # Suma subtotales de cada item
        return sum(item.producto.precio_actual * item.cantidad for item in obj.items.all())
