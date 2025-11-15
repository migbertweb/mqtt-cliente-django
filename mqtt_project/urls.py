"""
Archivo: urls.py

Descripción: Configuración de URLs principal del proyecto Django. Define las
rutas de nivel superior incluyendo el panel de administración y las URLs de
la aplicación mqttapp.

Autor: migbertweb

Fecha: 2024

Repositorio: https://github.com/migbertweb/mqtt-cliente-django

Licencia: MIT License

Uso: Punto de entrada para el enrutamiento de URLs del proyecto. Incluye
las URLs de la aplicación mqttapp y el panel de administración de Django.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mqttapp.urls')),
]
