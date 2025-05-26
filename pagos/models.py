from django.db import models

# Create your models here.
class Pago(models.Model):
    METODO_PAGO = [
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta de credito/debito'),
        ('transferencias' , 'Transferencia bancaria'),
        ]   
    
    ESTADO_PAGO = [
        ('pendiente', 'Pendiente'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
        ('enviado', 'Enviado'),
    ]
    
    fecha_pago = models.DateField()
    cliente = models.ForeignKey('clientes.cliente', on_delete=models.CASCADE)
    total_pago = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=METODO_PAGO)
    estado_pago = models.CharField(max_length=50, choices=ESTADO_PAGO, default='pendiente')
    
    def __str__(self):
        return f"{self.id} - cliente: {self.cliente} - total: {self.total_pago} - estado: {self.estado_pago}"
    def get_absolute_url(self):
        return f"/pagos/{self.id}/"
    
