from django.contrib import admin
from django.contrib.admin.sites import AdminSite

# Títulos personalizados
admin.site.site_header = "EcoStock Admin"
admin.site.site_title = "EcoStock Panel"
admin.site.index_title = "Bienvenido a EcoStock"

# Esto aplica el CSS a TODO el admin
class MyAdminSite(admin.AdminSite):
    class Media:
        css = {
            'all': ("css/ecostock_admin.css",)  # Asegúrate de tener esta ruta
        }

# Esto no se registra directamente, pero Django lo cargará si el static está bien configurado
