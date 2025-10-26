# MQTT web client (Django)

Proyecto mínimo para usar como cliente MQTT desde el navegador y desde backend Python (publish). Diseñado para uso personal en laptop.

Supuestos importantes:
- Broker MQTT accesible en 37.27.243.58. Se asume que tiene soporte WebSockets en el puerto 9001 para el cliente web (ws://37.27.243.58:9001). Si no es así, cambie `MQTT_WS_PORT` en `mqtt_project/settings.py` o use la publicación desde backend en TCP (1883).

Cómo ejecutar (Linux / zsh):

```bash
# crear venv y activarlo
python -m venv .venv
source .venv/bin/activate

# instalar dependencias
pip install -r requirements.txt

# aplicar migraciones y arrancar
python manage.py migrate
python manage.py runserver

# abrir http://127.0.0.1:8000/
```

Detalles:
- La página principal (`/`) carga un cliente JS que se conecta por WebSockets al broker. Host/puerto configurables en la plantilla o en `settings.py`.
- También hay un endpoint HTTP POST `/publish/` que publica un mensaje usando paho-mqtt desde el servidor (usa TCP a 1883 por defecto).

Archivos clave:
- `mqtt_project/settings.py` — configuración mínima del proyecto y variables MQTT.
- `mqttapp/templates/mqttapp/index.html` — UI web y ejemplo de conexión con `mqtt.js` (CDN).
- `mqttapp/mqtt_client.py` — helper para publicar mensajes desde Python.

Notas:
- Si el broker no expone WebSockets, el navegador no podrá conectarse directamente; use el endpoint `/publish/` para publicar desde el servidor.
