from django.urls import path
from . import views

app_name = 'gestion'  # Namespace para evitar conflictos entre apps

urlpatterns = [
    # Página principal
    path('', views.inicio, name='inicio'),
    
    # Gestión de insumos
    path('insumos/', views.listar_insumos, name='listar_insumos'),
    path('insumos/crear/', views.crear_insumo, name='crear_insumo'),
    path('insumos/editar/<int:id>/', views.editar_insumo, name='editar_insumo'),
    path('insumos/eliminar/<int:id>/', views.eliminar_insumo, name='eliminar_insumo'),
    
    # Autenticación y usuarios
    path('registro/', views.registro_usuario, name='registro'),
    path('cuenta/', views.perfil_usuario, name='perfil'),  # Nueva ruta recomendada
    
    # Proveedores (si los has implementado)
    # path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
] 