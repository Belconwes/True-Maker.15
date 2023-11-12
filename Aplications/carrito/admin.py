from django.contrib import admin
from .models import Carrito, CarritoProducto

@admin.register(Carrito)
class CarritoAdmin (admin.ModelAdmin):
    list_display = (
        'customer',
        'mostrar_productos',
    )
    def mostrar_productos(self, obj):
        return ", ".join([producto.nombre for producto in obj.productos.all()])
    mostrar_productos.short_description = 'Productos'
    
@admin.register(CarritoProducto)
class CarritoProductoAdmin (admin.ModelAdmin):
    list_display= (
        'id_carrito',
        'id_producto',
        'cantidad',
        'estado',
    )

