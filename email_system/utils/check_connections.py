
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
def fetch_emails():
    try:
        # Conectar a IMAP
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")  # Seleccionar la bandeja de entrada
        
        while True:
            _, data = mail.search(None, "UNSEEN")  # Buscar correos no leídos

            if not data[0]:  # Si no hay correos nuevos
                print("🛑 No hay correos nuevos para procesar.")
            else:
                for num in data[0].split():
                    _, msg_data = mail.fetch(num, "(RFC822)")
                    raw_email = msg_data[0][1]
                    email_message = email.message_from_bytes(raw_email)

                    # Extraer los campos relevantes
                    email_data = {
                        "id": num.decode(),
                        "from": email_message["From"],
                        "subject": email_message["Subject"],
                        "body": get_body(email_message),
                        "received_at": str(email_message["Date"])
                    }
                    
                    # Enviar a Kafka
                    producer.send("raw_emails", value=email_data)
                    print(f"📩 Email {num} enviado a Kafka")
            
            sleep(60)  # Espera 1 minuto antes de revisar nuevamente

    except Exception as e:
        print(f"❌ Error: {e}")

