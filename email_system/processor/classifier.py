import json
import logging
from kafka import KafkaConsumer, KafkaProducer
from config import KAFKA_SERVER, CLASSIFICATION_RULES

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
    return None  

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
            category_topic = classify_email(email_data)

            # Enviar siempre a acknowledgement_queue para acuse rápido
            producer.send("acknowledgement_queue", value=email_data)
            logger.info(f"Enviado email ID {email_data['id']} a acknowledgement_queue")

            # Si clasificó en categoría, enviar también a ese topic
            if category_topic:
                producer.send(category_topic, value=email_data)
                logger.info(f"Clasificado email ID {email_data['id']} → {category_topic}")

        except json.JSONDecodeError:
            logger.error("Error decodificando el mensaje de Kafka")
        except Exception as e:
            logger.error(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
