"""
Archivo: views.py

Descripción: Vistas de la aplicación Django. Contiene dos vistas principales:
- `index`: Renderiza la página principal con el cliente MQTT web
- `publish`: Endpoint HTTP POST para publicar mensajes MQTT desde el backend

Autor: migbertweb

Fecha: 2024

Repositorio: https://github.com/migbertweb/mqtt-cliente-django

Licencia: MIT License

Uso: Maneja las peticiones HTTP de la aplicación. La vista `index` pasa la 
configuración MQTT al template, y `publish` permite publicar mensajes mediante
peticiones POST.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from . import mqtt_client


def index(request):
    # pass MQTT info to template
    ctx = {
        'mqtt_host': settings.MQTT_HOST,
        'mqtt_ws_port': settings.MQTT_WS_PORT,
    }
    return render(request, 'mqttapp/index.html', ctx)


@csrf_exempt
@require_POST
def publish(request):
    topic = request.POST.get('topic') or request.POST.get('t')
    payload = request.POST.get('payload') or request.POST.get('p')
    if not topic:
        return JsonResponse({'ok': False, 'error': 'missing topic'}, status=400)
    ok = mqtt_client.publish(topic, payload or '')
    return JsonResponse({'ok': ok})
