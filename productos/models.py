from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre_categoria_producto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_categoria_producto
    
    
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    codigo_producto = models.CharField(max_length=50)
    categoria_Producto = models.ForeignKey(
        CategoriaProducto, 
        on_delete=models.CASCADE,
        db_column= 'CATEGORIAPRODUCTO_ID'
        )
    marca_producto = models.CharField(max_length=100)
    descripcion_producto = models.TextField()
    imagen_producto = models.ImageField(upload_to='productos/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre_producto
    
    @property
    def precio_actual(self):
        # precioproducto_set ordena ya por fecha descendente según tu Meta
        ultimo = self.precioproducto_set.first()
        return ultimo.precio if ultimo else 0
    


class PrecioProducto(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha']
    
    def __str__(self):
        return str(self.precio)