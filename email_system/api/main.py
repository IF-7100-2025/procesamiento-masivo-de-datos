from fastapi import FastAPI
from prometheus_client import make_asgi_app
from dotenv import load_dotenv
import os
from api.routers import metrics, health

load_dotenv()

app = FastAPI(title="Email Processing Metrics")

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

app.include_router(metrics.router)
app.include_router(health.router)
