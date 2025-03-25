# gestion/forms.py
from django import forms
from .models import Insumo, Categoria, Proveedor

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = [
            'nombre', 
            'descripcion',
            'categoria',
            'proveedor',
            'precio',
            'stock',
            'unidad_medida',
            'imagen'
        ]
        
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Cemento Gris'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción detallada del insumo'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
            'proveedor': forms.Select(attrs={
                'class': 'form-select'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'unidad_medida': forms.Select(attrs={
                'class': 'form-select'
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }
        
        labels = {
            'unidad_medida': 'Unidad de Medida',
            'imagen': 'Imagen del Producto'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra solo categorías activas
        self.fields['categoria'].queryset = Categoria.objects.all()
        # Filtra solo proveedores activos
        self.fields['proveedor'].queryset = Proveedor.objects.filter(estado=True)

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor a cero")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo")
        return stock