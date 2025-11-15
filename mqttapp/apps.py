"""
Archivo: apps.py

Descripción: Configuración de la aplicación Django mqttapp. Define la clase
de configuración de la aplicación con sus metadatos y configuraciones específicas.

Autor: migbertweb

Fecha: 2024

Repositorio: https://github.com/migbertweb/mqtt-cliente-django

Licencia: MIT License

Uso: Configuración de la aplicación Django. Define el campo de clave primaria
automática por defecto y el nombre de la aplicación.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
from django.apps import AppConfig


class MqttappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mqttapp'
