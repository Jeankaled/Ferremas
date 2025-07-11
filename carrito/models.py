from django.db import models
from django.conf import settings
from django.db import models
from productos.models import Producto
from django.utils import timezone
# Create your models here.


class Cart(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("cart", "producto")
