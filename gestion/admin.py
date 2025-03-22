from django.contrib import admin
from .models import Proveedor, Insumo, Categoria, MovimientoInventario

admin.site.register(Proveedor)
admin.site.register(Insumo)
admin.site.register(Categoria)
admin.site.register(MovimientoInventario)