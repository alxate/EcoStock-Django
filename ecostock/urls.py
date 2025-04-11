from django.contrib import admin
from django.urls import path, include  # Importa 'include'
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),   
]