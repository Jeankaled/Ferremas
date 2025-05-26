from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre_categoria_producto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_categoria_producto
    
    
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    codigo_producto = models.CharField(max_length=50)
    CategoriaProducto = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    marca_producto = models.CharField(max_length=100)
    descripcion_producto = models.TextField()
    
    def __str__(self):
        return self.nombre_producto
    


class PrecioProducto(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha']
    
    def __str__(self):
        return str(self.precio)