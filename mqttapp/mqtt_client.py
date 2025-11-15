"""
Archivo: mqtt_client.py

Descripción: Módulo helper para publicar mensajes MQTT de forma síncrona usando 
paho-mqtt. Proporciona una función `publish()` que establece una conexión temporal
al broker, publica el mensaje y cierra la conexión.

Autor: migbertweb

Fecha: 2024

Repositorio: https://github.com/migbertweb/mqtt-cliente-django

Licencia: MIT License

Uso: Utilizado por la vista Django `publish` para reenviar mensajes al broker MQTT
desde el backend. Se conecta al broker mediante TCP (puerto 1883 por defecto).

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
import logging
import time
from django.conf import settings
import paho.mqtt.client as mqtt

logger = logging.getLogger(__name__)


def publish(topic: str, payload: str, qos: int = 0, retain: bool = False, timeout: float = 5.0) -> bool:
    client = mqtt.Client()
    try:
        client.connect(settings.MQTT_HOST, settings.MQTT_TCP_PORT, keepalive=60)
        client.loop_start()
        rc = client.publish(topic, payload=payload, qos=qos, retain=retain)
        # wait for publish
        rc.wait_for_publish(timeout=timeout)
        client.loop_stop()
        client.disconnect()
        logger.info('Published to %s', topic)
        return True
    except Exception as e:
        logger.exception('Failed to publish to MQTT: %s', e)
        try:
            client.disconnect()
        except Exception:
            pass
        return False
