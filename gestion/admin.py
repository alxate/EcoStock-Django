from django.contrib import admin


# Register your models here.

from .models import Proveedor, Insumo, Categoria, MovimientoInventario

admin.site.register(Proveedor)
admin.site.register(Insumo)
admin.site.register(Categoria)
admin.site.register(MovimientoInventario)

