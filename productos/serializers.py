from rest_framework import serializers
from .models import Producto, CategoriaProducto, PrecioProducto

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'
        
        
class ProductoSerializer(serializers.ModelSerializer):
    imagen_url = serializers.ImageField(source='imagen_producto', read_only=True)
    categoria_producto = CategoriaProductoSerializer(read_only=True)
    
    categoria_producto_id = serializers.PrimaryKeyRelatedField(
        source='categoria_Producto',
        queryset=CategoriaProducto.objects.all(),
        write_only=True
    )
    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre_producto',
            'codigo_producto',
            'marca_producto',
            'descripcion_producto',
            'categoria_producto',     
            'categoria_producto_id',
            'imagen_url'
        ]
        
    def get_imagen(self, obj):
      req = self.context.get('request')
      if obj.imagen_producto and hasattr(obj.imagen_producto, 'url'):
        return req.build_absolute_uri(obj.imagen_producto.url)
      return None
       
        
class PrecioProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    
    producto_id = serializers.PrimaryKeyRelatedField(
        source='producto',
        queryset=Producto.objects.all(),
        write_only=True
    )
    
    class Meta:
        model = PrecioProducto
        fields = '__all__'  
       
        
        