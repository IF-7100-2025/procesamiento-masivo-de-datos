from fastapi import FastAPI
from prometheus_client import make_asgi_app, Counter, Gauge
from routers import metrics, health

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