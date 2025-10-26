# Instrucciones para agentes (proyecto mqtt-cliente-django)

Breve: este repo contiene una app Django mínima que expone una UI web (plantilla) que se conecta a un broker MQTT por WebSockets y un endpoint HTTP `/publish/` para publicar desde el servidor via paho-mqtt.

- Punto de entrada: `manage.py` y `mqtt_project/settings.py`.
- App principal: `mqttapp/` (vistas en `mqttapp/views.py`, helper MQTT en `mqttapp/mqtt_client.py`).
- Plantilla UI: `mqttapp/templates/mqttapp/index.html` — ejemplo de uso de `mqtt.js` (CDN) para conectar por WebSockets.

Qué debe saber un agente para ser productivo:

1. Arquitectura y flujos clave

   - Frontend (navegador) utiliza MQTT over WebSockets usando `mqtt.js` y se conecta a `ws://<MQTT_HOST>:<MQTT_WS_PORT>` (por defecto `37.27.243.58:9001`).
   - Backend Django publica mensajes usando `paho-mqtt` (TCP) hacia `MQTT_HOST:MQTT_TCP_PORT` (por defecto `1883`).
   - La plantilla pasa `mqtt_host` y `mqtt_ws_port` desde `settings.py` al cliente JS.

2. Configuración y convenciones del proyecto

   - Variables configurables en `mqtt_project/settings.py`: `MQTT_HOST`, `MQTT_TCP_PORT`, `MQTT_WS_PORT`.
   - No hay autenticación ni permisos por defecto; el endpoint `/publish/` acepta POST sin CSRF (se decoró con `@csrf_exempt`) para facilidad local. Cambiar esto para producción.
   - DB: SQLite por defecto (`db.sqlite3`).

3. Flujos de desarrollo comunes

   - Arrancar local:
     - Crear venv, `pip install -r requirements.txt`, `python manage.py migrate`, `python manage.py runserver`.
   - Ver y modificar la conexión WebSocket en `mqttapp/templates/mqttapp/index.html` o mediante las variables en `settings.py`.
   - Publicar desde backend: POST a `/publish/` con `topic` y `payload` (form-data). Ejemplo en JS en la plantilla.

4. Restricciones y suposiciones detectadas (útiles para el agente)

   - Se asume que el broker expone WebSockets en `MQTT_WS_PORT` (9001 por defecto). Si no, el cliente web no funcionará; usar el endpoint backend como alternativa.
   - No hay manejo de autenticación MQTT en la plantilla/cliente backend; si el broker requiere auth, se debe añadir user/password tanto en `mqtt_client.py` como en la conexión JS.

5. Cambios seguros que un agente puede proponer/realizar

   - Añadir soporte opcional para usuario/contraseña MQTT (envvars y UI para introducir credenciales).
   - Añadir CSRF y autenticación al endpoint `/publish/` si el despliegue no es local.
   - Mejorar el manejo de errores y mostrar estados de reconexión en la UI.

6. Archivos clave a inspeccionar para entender comportamiento real
   - `mqttapp/mqtt_client.py` — lógica de publish desde Python.
   - `mqttapp/templates/mqttapp/index.html` — cliente JS y ejemplo de suscripción/publicación.
   - `mqtt_project/settings.py` — dónde cambiar la dirección del broker y puertos.

Si quieres, actualizo estas instrucciones con ejemplos de tests (p. ej. test para `mqtt_client.publish`) o añado soporte por WebSocket seguro (wss) y autenticación. Indícame qué prefieres.
