# test_producer.py
import json
import time
from kafka import KafkaProducer

KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

# Lista de emails de prueba con diferentes temas
test_emails = [
    {
        "id": "email-001",
        "from": "juan@correo.com",
        "subject": "Suscripción al newsletter",
        "body": "Hola, quiero suscribirme al newsletter de Daily Planet"
    },
    {
        "id": "email-002",
        "from": "ana@correo.com",
        "subject": "Consulta sobre precios",
        "body": "Quisiera saber los precios de sus publicaciones"
    },
    {
        "id": "email-003",
        "from": "luis@correo.com",
        "subject": "Reclamo por error en artículo",
        "body": "El artículo de hoy tiene datos incorrectos, por favor revisar"
    },
    {
        "id": "email-004",
        "from": "maria@correo.com",
        "subject": "Tengo una queja urgente",
        "body": "Me parece muy mal lo publicado sobre mi ciudad"
    },
    {
        "id": "email-005",
        "from": "carla@correo.com",
        "subject": "Felicitaciones por el reportaje",
        "body": "Excelente cobertura del evento político"
    }
]

for email in test_emails:
    producer.send("raw_emails", value=email)
    print(f"Email enviado: {email['id']}")
    time.sleep(0.5)  

producer.flush()
print("Todos los emails de prueba fueron enviados.")
