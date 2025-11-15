# MQTT Cliente Django

Cliente MQTT web desarrollado con Django que permite conectarse a un broker MQTT desde el navegador mediante WebSockets y publicar mensajes desde el backend Python.

## 📋 Descripción

Este proyecto es una aplicación web minimalista diseñada para uso personal que permite:

- **Conexión MQTT desde el navegador**: Cliente web que se conecta al broker MQTT mediante WebSockets
- **Publicación desde backend**: Endpoint HTTP para publicar mensajes usando paho-mqtt desde el servidor Django
- **Interfaz moderna**: UI desarrollada con Tailwind CSS y Alpine.js con soporte para modo oscuro
- **Suscripción a todos los tópicos**: El cliente web se suscribe automáticamente a todos los tópicos (`#`) para monitorear el tráfico MQTT

## 🚀 Características

- ✅ Conexión MQTT vía WebSockets desde el navegador
- ✅ Publicación de mensajes desde el navegador (cliente MQTT.js)
- ✅ Publicación de mensajes desde el servidor (paho-mqtt)
- ✅ Interfaz web moderna con modo oscuro
- ✅ Lista de mensajes recibidos con filtrado
- ✅ Detección automática de tópicos
- ✅ Selección rápida de tópicos detectados

## 📦 Requisitos

- Python 3.8+
- Django 4.2+
- paho-mqtt 1.6+
- Broker MQTT con soporte WebSockets (puerto 9001 por defecto)

## 🔧 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/migbertweb/mqtt-cliente-django.git
cd mqtt-cliente-django
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno (opcional)

Por defecto, el proyecto está configurado para conectarse a un broker en `37.27.243.58`. Puedes cambiar esto mediante variables de entorno:

```bash
export MQTT_HOST=tu-broker.com
export MQTT_TCP_PORT=1883
export MQTT_WS_PORT=9001
export DJANGO_SECRET=tu-secret-key-aqui
```

### 5. Ejecutar migraciones

```bash
python manage.py migrate
```

### 6. Iniciar el servidor

```bash
python manage.py runserver
```

### 7. Acceder a la aplicación

Abre tu navegador en: `http://127.0.0.1:8000/`

## 📁 Estructura del Proyecto

```
mqtt-cliente-django/
├── manage.py                 # Script de gestión de Django
├── requirements.txt          # Dependencias del proyecto
├── LICENSE                   # Licencia MIT
├── README.md                 # Este archivo
├── mqtt_project/            # Configuración del proyecto Django
│   ├── __init__.py
│   ├── settings.py          # Configuración y variables MQTT
│   ├── urls.py              # URLs principales
│   └── wsgi.py              # Configuración WSGI
└── mqttapp/                 # Aplicación principal
    ├── __init__.py
    ├── apps.py
    ├── mqtt_client.py       # Helper para publicar mensajes MQTT
    ├── views.py             # Vistas de la aplicación
    ├── urls.py              # URLs de la aplicación
    └── templates/
        └── mqttapp/
            └── index.html   # Interfaz web del cliente MQTT
```

## 🔌 Configuración del Broker MQTT

### Supuestos importantes

- El broker MQTT debe estar accesible en la dirección configurada en `MQTT_HOST`
- Para conexión desde el navegador, el broker debe tener soporte WebSockets en el puerto configurado en `MQTT_WS_PORT` (por defecto 9001)
- Para publicación desde backend, se usa TCP en el puerto `MQTT_TCP_PORT` (por defecto 1883)

### Configuración en settings.py

Las variables MQTT se pueden configurar en `mqtt_project/settings.py` o mediante variables de entorno:

```python
MQTT_HOST = os.environ.get('MQTT_HOST', '37.27.243.58')
MQTT_TCP_PORT = int(os.environ.get('MQTT_TCP_PORT', 1883))
MQTT_WS_PORT = int(os.environ.get('MQTT_WS_PORT', 9001))
```

## 📡 Uso

### Desde el navegador

1. Abre la aplicación en `http://127.0.0.1:8000/`
2. Configura el host y puerto del broker (si es necesario)
3. Haz clic en "Conectar" para establecer la conexión WebSocket
4. El cliente se suscribirá automáticamente a todos los tópicos (`#`)
5. Los mensajes recibidos aparecerán en la sección "Mensajes recibidos"
6. Puedes publicar mensajes usando el formulario de publicación

### Publicación desde backend (API)

Puedes publicar mensajes mediante una petición HTTP POST:

```bash
curl -X POST http://127.0.0.1:8000/publish/ \
  -d "topic=test/topic" \
  -d "payload=Hola desde backend"
```

O usando los parámetros cortos:

```bash
curl -X POST http://127.0.0.1:8000/publish/ \
  -d "t=test/topic" \
  -d "p=Hola desde backend"
```

## 🛠️ Desarrollo

### Archivos principales

- **`mqttapp/mqtt_client.py`**: Módulo helper para publicar mensajes MQTT desde Python usando paho-mqtt
- **`mqttapp/views.py`**: Vistas Django que manejan la página principal y el endpoint de publicación
- **`mqttapp/templates/mqttapp/index.html`**: Interfaz web completa con cliente MQTT.js
- **`mqtt_project/settings.py`**: Configuración del proyecto Django y variables MQTT

### Notas de desarrollo

- Si el broker no expone WebSockets, el navegador no podrá conectarse directamente. En ese caso, usa el endpoint `/publish/` para publicar desde el servidor.
- El cliente web se suscribe a todos los tópicos (`#`) por defecto. Esto puede generar mucho tráfico en brokers con muchos mensajes.
- Los mensajes se almacenan en memoria en el navegador (máximo 1000 mensajes).

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

**Recomendación Opcional para Proyectos Educativos:**

Se recomienda encarecidamente, aunque no es obligatorio, que las obras derivadas mantengan este mismo espíritu de código libre y abierto, especialmente cuando se utilicen con fines educativos o de investigación.

## 👤 Autor

**Migbertweb**

- GitHub: [@migbertweb](https://github.com/migbertweb)
- Repositorio: https://github.com/migbertweb/mqtt-cliente-django

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

## ⚠️ Notas de Seguridad

- Este proyecto está diseñado para uso personal y desarrollo local
- No uses `DEBUG = True` en producción
- Cambia el `SECRET_KEY` antes de desplegar
- Configura `ALLOWED_HOSTS` apropiadamente para producción
- Considera implementar autenticación si vas a exponer el servicio públicamente

## 📚 Recursos

- [Django Documentation](https://docs.djangoproject.com/)
- [MQTT.js Documentation](https://github.com/mqttjs/MQTT.js)
- [paho-mqtt Documentation](https://www.eclipse.org/paho/clients/python/)
- [MQTT Protocol Specification](https://mqtt.org/)
