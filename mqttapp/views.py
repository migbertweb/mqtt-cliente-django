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
