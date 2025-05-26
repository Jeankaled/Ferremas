from django.db import models

# Create your models here.

class Pedido(models.Model):
    METODO_PAGO = [
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta de credito/debito'),
        ('transferencias' , 'Transferencia bancaria'),
        ]   
    
    ESTADO_PEDIDO = [
        ('pendiente', 'Pendiente'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
        ('enviado', 'Enviado'),
    ]
    
    fecha_pedido = models.DateField()
    cliente = models.ForeignKey('clientes.cliente', on_delete=models.CASCADE)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=METODO_PAGO)
    estado_pedido = models.CharField(max_length=50, choices=ESTADO_PEDIDO, default='pendiente')
    
    def __str__(self):
        return f"{self.id} - cliente: {self.cliente} - total: {self.total_pedido} - estado: {self.estado_pedido}"
    def get_absolute_url(self):
        return f"/pedidos/{self.id}/"
    
class Detalle_Pedido(models.Model):
    pedido = models.ForeignKey('pedidos.pedido', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.pedido.id} - {self.producto} - {self.cantidad} - {self.precio}"