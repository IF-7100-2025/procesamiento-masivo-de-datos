from fastapi import APIRouter, HTTPException
from kafka import KafkaProducer
import smtplib
from typing import Dict, Any

router = APIRouter(tags=["Health Checks"])

def check_kafka() -> bool:
    """Verifica conexión con Kafka."""
    try:
        producer = KafkaProducer(bootstrap_servers="localhost:9092")
        producer.close()
        return True
    except Exception:
        return False

def check_smtp() -> bool:
    """Verifica conexión con el servidor SMTP."""
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
        return True
    except Exception:
        return False

@router.get("/health", summary="Verifica el estado del servicio")
async def health_check() -> Dict[str, Any]:
    """Endpoint de health check que verifica:
    - Estado de Kafka
    - Estado de SMTP
    - Estado general del servicio
    """
    services = {
        "kafka": check_kafka(),
        "smtp": check_smtp(),
    }
    all_healthy = all(services.values())

    if not all_healthy:
        raise HTTPException(
            status_code=503,
            detail="Service Unavailable",
            headers={"Retry-After": "30"},
        )

    return {
        "status": "OK",
        "services": services,
        "details": "All systems operational"
    }