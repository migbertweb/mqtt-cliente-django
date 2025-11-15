"""
Archivo: urls.py

Descripción: Configuración de URLs de la aplicación mqttapp. Define las rutas
para la página principal (/) y el endpoint de publicación (/publish/).

Autor: migbertweb

Fecha: 2024

Repositorio: https://github.com/migbertweb/mqtt-cliente-django

Licencia: MIT License

Uso: Mapea las URLs de la aplicación a sus respectivas vistas. Incluido en
las URLs principales del proyecto mediante `include('mqttapp.urls')`.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publish/', views.publish, name='publish'),
]
