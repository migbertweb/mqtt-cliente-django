"""
Archivo: wsgi.py

Descripción: Configuración WSGI para el proyecto Django. Define la aplicación
WSGI que será utilizada por servidores web como Gunicorn o uWSGI para servir
la aplicación en producción.

Autor: migbertweb

Fecha: 2024

Repositorio: https://github.com/migbertweb/mqtt-cliente-django

Licencia: MIT License

Uso: Punto de entrada WSGI para despliegue en producción. Configura el módulo
de settings y crea la aplicación WSGI.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mqtt_project.settings')
application = get_wsgi_application()
