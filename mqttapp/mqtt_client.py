"""Simple helper to publish messages via paho-mqtt synchronously.

This module is used by the Django view `publish` to forward messages to the broker.
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
