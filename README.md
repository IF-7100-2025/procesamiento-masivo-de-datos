🚀 Sistema de Procesamiento Masivo de Emails con Kafka, Python y FastAPI
📋 Tabla de Contenidos
Arquitectura

Requisitos

Instalación

Configuración

Estructura del Proyecto

Ejecución

Endpoints API

Flujo de Trabajo

Health Checks

Métricas

Solución de Problemas

Mejoras Futuras

Contribución

Licencia

🌟 Arquitectura
Diagrama de Arquitectura

Componentes principales:

Kafka: Backbone para procesamiento de mensajes

Topics: raw_emails, classified_emails, acknowledgement_queue, human_review

Python Services:

IMAP Collector: Extrae emails y envía a Kafka

Email Processor: Clasifica emails usando reglas/NLP

SMTP Responder: Envía respuestas automáticas

FastAPI: Dashboard de monitoreo y métricas

🛠️ Requisitos Previos
Componente	Versión	Notas
Docker	20.10+	Para Kafka y Zookeeper
Python	3.9+	
Cuenta Email	-	IMAP/SMTP habilitado (ej: Gmail)
Memoria	4GB+	Para procesamiento eficiente
📥 Instalación
1. Clonar repositorio
bash
git clone https://github.com/tu-usuario/email-processing-system.git
cd email-processing-system
2. Iniciar infraestructura
bash
# Iniciar Kafka y Zookeeper
docker-compose -f kafka/docker-compose.yml up -d

# Crear topics (opcional)
docker exec kafka kafka-topics --create --topic raw_emails --partitions 3 --replication-factor 1 --bootstrap-server localhost:9092
docker exec kafka kafka-topics --create --topic acknowledgement_queue --partitions 3 --replication-factor 1 --bootstrap-server localhost:9092
3. Entorno virtual Python
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
⚙️ Configuración
Crear archivo .env en la raíz:

ini
# IMAP Collector
IMAP_SERVER=imap.gmail.com
IMAP_EMAIL=tu_email@gmail.com
IMAP_PASSWORD=tu_contraseña_app

# SMTP Responder
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=tu_email@gmail.com
SMTP_PASSWORD=tu_contraseña_app

# Kafka
KAFKA_BOOTSTRAP_SERVERS=localhost:9092

# FastAPI
API_PORT=8000
📂 Estructura del Proyecto
email-system/
├── collector/          # Servicio de recolección IMAP
│   ├── imap_collector.py
│   └── config.py
├── processor/          # Clasificación de emails
│   ├── classifier.py
│   ├── nlp_utils.py
│   └── config.py
├── responder/          # Respuestas automáticas
│   ├── smtp_responder.py
│   ├── templates/
│   └── config.py
├── api/                # Dashboard de monitoreo
│   ├── main.py
│   ├── routers/
│   └── models/
├── kafka/              # Configuración Kafka
│   └── docker-compose.yml
└── tests/              # Pruebas unitarias e integración
▶️ Ejecución
Servicios principales (terminales separadas):

bash
# Terminal 1 - Colector IMAP
python collector/imap_collector.py

# Terminal 2 - Procesador
python processor/classifier.py

# Terminal 3 - Respondedor SMTP
python responder/smtp_responder.py

# Terminal 4 - API de Métricas
uvicorn api.main:app --reload --port $API_PORT
🌐 Endpoints del API
Método	Endpoint	Descripción
GET	/health	Estado del sistema y dependencias
GET	/stats	Métricas de procesamiento
GET	/metrics	Datos en formato Prometheus
Dashboard: http://localhost:8000/docs (Swagger UI)

🔄 Flujo de Trabajo Completo
Recepción:

Colector verifica buzón IMAP cada 60 segundos

Nuevos emails se publican en raw_emails

Procesamiento:

python
if "suscripción" in email.subject.lower():
    send_to = "acknowledgement_queue"
else:
    send_to = "human_review"
Respuesta:

Plantilla HTML personalizada

SMTP con autenticación TLS

Monitoreo:

Prometheus scrapea métricas cada 15s

Alertas configurables en Grafana

🩺 Health Checks Avanzados
Código del endpoint /health:

python
def check_kafka():
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            request_timeout_ms=3000
        )
        producer.close()
        return True
    except Exception as e:
        logger.error(f"Kafka health check failed: {str(e)}")
        return False
Respuesta típica:

json
{
    "status": "OK",
    "services": {
        "kafka": true,
        "smtp": true,
        "imap": true
    },
    "details": "All systems operational",
    "timestamp": "2023-11-15T12:34:56Z"
}
📊 Sistema de Métricas
Métricas clave:

Métrica	Tipo	Etiquetas
emails_processed_total	Counter	topic, status
email_processing_time_seconds	Histogram	topic
email_queue_size	Gauge	queue_name
Ejemplo de consulta Prometheus:

promql
rate(emails_processed_total{topic="raw_emails"}[5m])
🐛 Solución de Problemas Comunes
1. Kafka no responde
bash
# Verificar estado del contenedor
docker ps -a | grep kafka

# Ver logs
docker logs kafka-1

# Probar conexión manual
kafka-console-producer --topic test --bootstrap-server localhost:9092
2. Errores de autenticación SMTP
python
# responder/config.py
SMTP_CONFIG = {
    "server": "smtp.gmail.com",
    "port": 587,
    "use_tls": True,  # ← Asegurar que esté True
    "username": "tu_email@gmail.com",
    "password": "contraseña_app"  # No usar contraseña directa
}
3. Alto uso de CPU
python
# collector/config.py
OPTIMIZATIONS = {
    "max_emails_per_batch": 50,  # Limitar procesamiento por lote
    "polling_interval": 60       # Segundos entre verificaciones
}
🚀 Mejoras Futuras
1. Procesamiento Avanzado con NLP
python
# processor/nlp_utils.py
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="bert-base-multilingual-cased",
    tokenizer="bert-base-multilingual-cased"
)

def analyze_sentiment(text):
    return classifier(text[:512])  # Limitar longitud para eficiencia
2. Sistema de Reintentos
python
# responder/smtp_responder.py
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def send_email(msg):
    # Lógica de envío
3. Despliegue en Kubernetes
yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: email-processor
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: processor
        image: email-processor:1.0
        resources:
          limits:
            cpu: "1"
            memory: "1Gi"
🤝 Guía de Contribución
Reporte de Bugs:

Usar el template de GitHub Issues

Incluir logs y pasos para reproducir

Nuevas Features:

Crear una rama feature/feature-name

Actualizar documentación

Incluir pruebas unitarias

Estilo de Código:

PEP 8 para Python

Type hints en funciones públicas

Docstrings Google Style
