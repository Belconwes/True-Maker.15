from django.contrib import admin
from .models import Cupon

@admin.register(Cupon)
class DescuentosAdmin (admin.ModelAdmin):
    list_display = (
        'fecha',
        'codigo',
        'descuento_porcentaje',
        'descuento_valor',
        #'mostrar_productos',
    )
# Register your models here.
