from rest_framework import serializers
from .models import Producto, CategoriaProducto, PrecioProducto

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'
        
        
class ProductoSerializer(serializers.ModelSerializer):
    categoria_producto = CategoriaProductoSerializer(read_only=True)
    
    class Meta:
        model = Producto
        fields = '__all__'
        
        
class PrecioProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    
    class Meta:
        model = PrecioProducto
        fields = '__all__'  
        
        