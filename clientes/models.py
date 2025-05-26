from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField(max_length=100)
    telefono_cliente = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre_cliente} - {self.apellido_cliente}"
    