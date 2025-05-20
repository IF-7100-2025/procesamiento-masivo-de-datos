from fastapi import APIRouter
from kafka import KafkaConsumer
import threading
import json
import time

router = APIRouter()

stats = {"raw_emails": 0, "acknowledged": 0}

def consume_kafka():
    consumer = KafkaConsumer(
    "raw_emails", "acknowledgement_queue",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    group_id="metrics_consumer_group",      
    enable_auto_commit=True,               
    auto_commit_interval_ms=5000,         
    consumer_timeout_ms=1000
)

    while True:
        for msg in consumer:
            if msg.topic == "raw_emails":
                stats["raw_emails"] += 1
            elif msg.topic == "acknowledgement_queue":
                stats["acknowledged"] += 1
        time.sleep(1)

@router.on_event("startup")
def startup_event():
    thread = threading.Thread(target=consume_kafka, daemon=True)
    thread.start()

@router.get("/stats")
def get_stats():
    return stats
