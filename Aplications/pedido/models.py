from django.db import models
from Aplications.Usuarios.models import User 
class Pedido (models.Model):
    #TIPOS_PAGOS_CHOICES=(('0','Mercado Pago'),('1','Tarjeta de crédito'),('2','Tarjeta de débito'),)
    
    id_pedido = models.BigAutoField(primary_key=True)
    #total = models.DecimalField('Total a pagar',max_digits=20, decimal_places=2) #! Revisar si eliminar
    fecha_pedido = models.DateTimeField('Fecha',auto_now_add=True)
    Usuario_p = models.ForeignKey (User, on_delete=models.CASCADE)
    #medio_de_pago = models.CharField ('Medio de Pago', max_length=1, choices=TIPOS_PAGOS_CHOICES) #Comentar
    class Meta:
        verbose_name = ('Pedido')
        verbose_name_plural = ('Pedidos')
        ordering = ['fecha_pedido']
        
    """def medio_pago_display(self):
        return dict(self.TIPOS_PAGOS_CHOICES).get(self.medio_de_pago, 'Desconocido')
    ${self.total} - {self.medio_pago_display()}"""
    def __str__(self):
        # Formatea la fecha y hora sin microsegundos usando strftime()
        formatted_fecha = self.fecha_pedido.strftime('%Y-%m-%d %H:%M:%S')
        return f"{formatted_fecha}"
    
    @property
    def get_cart_total(self):
        orderitems = self.carritoproducto_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.carritoproducto_set.all()
        total = sum([item.cantidad for item in orderitems])
        return total
# Create your models here.

print('teshible')
