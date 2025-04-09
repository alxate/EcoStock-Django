from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')


def index(request):
    contexto = {
        'Titulo': 'Inicio',
        'Mensaje': 'Controla tu inventario'
    }
    return render(request, 'main_app/index.html', contexto)