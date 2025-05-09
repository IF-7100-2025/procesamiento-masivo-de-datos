from fastapi import FastAPI
from prometheus_client import make_asgi_app, Counter, Gauge
from dotenv import load_dotenv
import os
from routers import metrics, health

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Ahora puedes acceder a las variables con os.getenv()
imap_server = os.getenv("IMAP_SERVER")
smtp_user = os.getenv("SMTP_USER")
kafka_server = os.getenv("KAFKA_SERVER")

# Crear la aplicación FastAPI
app = FastAPI(title="Email Processing Metrics")

# Métricas Prometheus
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

# Registra métricas personalizadas
EMAILS_PROCESSED = Counter(
    "emails_processed_total",
    "Total de emails procesados",
    ["topic"]
)

RESPONSE_TIME = Gauge(
    "email_response_time_seconds",
    "Tiempo de respuesta promedio",
    ["topic"]
)

# Incluye routers
app.include_router(metrics.router)
app.include_router(health.router)
