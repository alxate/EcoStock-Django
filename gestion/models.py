from django.contrib.auth.models import AbstractUser
from django.db import models


# Modelo de Usuario Personalizado (RF01)
class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('inventario', 'Operador de Inventario')
    )
    role = models.CharField(max_length=20, choices=ROLES, default='inventario')
    telefono = models.CharField(max_length=15, blank=True, null=True)

# Modelo de Proveedores (RF04)
class Proveedor(models.Model):
    TIPOS = (('natural', 'Natural'), ('juridico', 'Jurídico'))
    tipo = models.CharField(max_length=10, choices=TIPOS)
    nit = models.CharField(max_length=20, unique=True, blank=True)  # Para jurídicos
    rut = models.CharField(max_length=20, blank=True)  # Para naturales
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.TextField()
    estado = models.BooleanField(default=True)

# Modelo de Categorías (RF02.06)
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

# Modelo de Insumos (RF02)
class Insumo(models.Model):
    UNIDADES = (('kg', 'Kilogramos'), ('l', 'Litros'), ('unidad', 'Unidad'))
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    unidad_medida = models.CharField(max_length=10, choices=UNIDADES)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='insumos/', blank=True)

class MovimientoInventario(models.Model):
    TIPOS = (('entrada', 'Entrada'), ('salida', 'Salida'), ('ajuste', 'Ajuste'))
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True)  # <-- Usa 'CustomUser' como string
    motivo = models.TextField(blank=True)