from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('inventario', 'Operador de Inventario')
    )
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='inventario'
    )
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username