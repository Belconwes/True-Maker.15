from django.contrib import admin
from .models import Pedido
class PedidoAdmin (admin.ModelAdmin):
    list_display = (
        'Usuario_p',
        #'total',
        #'medio_de_pago',
        'fecha_pedido',
    )
    readonly_fields=['fecha_pedido']
admin.site.register(Pedido,PedidoAdmin)
