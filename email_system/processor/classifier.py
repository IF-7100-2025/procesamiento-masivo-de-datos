import json
import logging
from kafka import KafkaConsumer, KafkaProducer
from config import KAFKA_SERVER, CLASSIFICATION_RULES

# Configura logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def classify_email(email_data):
    """Clasifica el email basado en reglas configuradas."""
    subject = email_data.get("subject", "").lower()
    body = email_data.get("body", "").lower()

    for category, rules in CLASSIFICATION_RULES.items():
        if any(keyword in subject or keyword in body for keyword in rules["keywords"]):
            return category
    return "acknowledgement_queue"  # Categoría por defecto

def main():
    consumer = KafkaConsumer(
        "raw_emails",
        bootstrap_servers=KAFKA_SERVER,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        group_id="email-classifier"
    )

    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVER,
        value_serializer=lambda x: json.dumps(x).encode("utf-8")
    )

    for message in consumer:
        try:
            email_data = message.value
            topic = classify_email(email_data)
            producer.send(topic, value=email_data)
            logger.info(f"Clasificado email ID {email_data['id']} → {topic}")
        except json.JSONDecodeError:
            logger.error("Error decodificando el mensaje de Kafka")
        except Exception as e:
            logger.error(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()