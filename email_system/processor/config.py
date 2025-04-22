KAFKA_SERVER = "localhost:9092"

# Reglas de clasificación (personalizables)
CLASSIFICATION_RULES = {
    "acknowledgement_queue": {
        "keywords": ["suscripción", "subscribe", "newsletter", "consulta"]
    },
    "human_review": {
        "keywords": ["queja", "reclamo", "urgente", "complaint", "error"]
    }
}