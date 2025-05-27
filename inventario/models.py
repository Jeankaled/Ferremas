from django.db import models

# Create your models here.
class Inventario(models.Model):
    fecha_ingreso = models.DateTimeField(auto_now=True)
    cantidad_disponible = models.PositiveIntegerField()
    producto = models.ForeignKey('productos.producto', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.producto.nombre_producto} - {self.cantidad_disponible} unidades disponibles"
    

