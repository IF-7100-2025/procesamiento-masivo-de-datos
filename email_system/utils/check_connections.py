import imaplib
import json
import os
from kafka import KafkaProducer
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Variables de entorno
IMAP_SERVER = os.getenv("IMAP_SERVER")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
KAFKA_SERVER = os.getenv("KAFKA_SERVER")

# Verificar conexión IMAP
def check_imap_connection():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")  # Seleccionar la bandeja de entrada
        print("✅ Conexión IMAP exitosa")
        mail.logout()
    except Exception as e:
        print(f"❌ Error al conectar a IMAP: {e}")

# Verificar conexión Kafka
def check_kafka_connection():
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_SERVER,
            value_serializer=lambda x: json.dumps(x).encode("utf-8")
        )
        # Enviar un mensaje de prueba
        producer.send('test_topic', value={'status': 'test'})
        producer.flush()  # Asegura que el mensaje sea enviado
        print("✅ Conexión a Kafka exitosa")
        producer.close()
    except Exception as e:
        print(f"❌ Error al conectar a Kafka: {e}")

# Ejecutar las verificaciones
def check_connections():
    print("🔍 Verificando conexiones...")
    check_imap_connection()
    check_kafka_connection()

if __name__ == "__main__":
    check_connections()
