from django.contrib import admin
from .models import Producto,Categoria
# Register your models here.
from .models import Stock
# Register your models here.

class StockAdmin (admin.ModelAdmin):
    list_display = (
        'producto',
        'cantidad',
        'fecha_venc',
        'numero_lote',
        'proveedor',
    )
    search_fields = ['producto']
    list_filter =['producto']
    
admin.site.register(Stock, StockAdmin)

class ProductoAdmin (admin.ModelAdmin):
    list_display = (
        'id',
        'categoria',
        'nombre',
        'medida',
        'tipo_medida',    # Para poder listar los datos que quiero en tabla
        'precio',
        'total_stock',
    )
    search_fields = ['nombre','id']
    list_filter = ['categoria']
    list_editable = ['precio']

admin.site.register(Producto,ProductoAdmin)

admin.site.register(Categoria)
