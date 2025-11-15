#!/usr/bin/env python
"""
Archivo: manage.py

Descripción: Script de gestión principal de Django. Punto de entrada para comandos
de administración del proyecto (migrate, runserver, etc.).

Autor: migbertweb

Fecha: 2024

Repositorio: https://github.com/migbertweb/mqtt-cliente-django

Licencia: MIT License

Uso: Ejecutar comandos de Django como 'python manage.py runserver' o 
'python manage.py migrate'.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mqtt_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
