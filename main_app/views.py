from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse

def home_view(request):
    return render(request,'home.html')


def index(request):
    contexto = {
        'Titulo': 'Inicio',
        'Mensaje': 'Controla tu inventario'
    }
    return render(request, 'main_app/index.html', contexto)

def login_view(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)    
       if user:
           login(request,user)
           return redirect('index')
       else:
           return render(request, 'main_app/login.html',{'error': 'Credenciales Invalidas'})
    return render(request, 'main_app/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create_user(username=username,password=password,email=email)
        return redirect('login')
    return render(request,'main_app/register.html')