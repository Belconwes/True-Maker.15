from django.db import models
from Aplications.Usuarios.models import User
from Aplications.productos.models import Producto
from Aplications.pedido.models import Pedido

# Create your models here.





class Carrito (models.Model):
    id_carritos = models.BigAutoField (primary_key=True)
    customer = models.OneToOneField (User, on_delete=models.CASCADE)
    productos = models.ManyToManyField (Producto, through = 'CarritoProducto')
    
    def get_cart_total(self):
        items = self.items.all()
        total = sum(item.id_producto.precio * item.cantidad for item in items)
        return total
    class Meta:
        verbose_name = ('Carrito')
        verbose_name_plural = ('Carritos')
        ordering = ['customer']
        
    def __str__(self):
        return f"ID:{self.id_carritos} - User:{self.customer.nombre}"
    
    
    
class CarritoProducto (models.Model):
    id_carrito = models.ForeignKey (Carrito, on_delete=models.CASCADE,related_name='items')
    id_pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE,null=True)
    id_producto = models.ForeignKey (Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField ('Cantidad', default=0)
    estado = models.BooleanField ('Estado activo', default=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.id_producto.precio * self.cantidad
        return total



    


    
    
