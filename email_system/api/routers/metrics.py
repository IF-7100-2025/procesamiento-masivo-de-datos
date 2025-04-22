from fastapi import APIRouter
from kafka import KafkaConsumer
import json
from ..models.metrics import EmailStats

router = APIRouter()

@router.get("/stats")
async def get_stats():
    consumer = KafkaConsumer(
        bootstrap_servers="localhost:9092",
        auto_offset_reset="earliest",
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )
    
    stats = {"raw_emails": 0, "acknowledged": 0}
    for msg in consumer:
        stats["raw_emails"] += 1
        if msg.topic == "acknowledgement_queue":
            stats["acknowledged"] += 1
    
    return EmailStats(**stats)