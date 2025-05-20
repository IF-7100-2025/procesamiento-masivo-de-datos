import imaplib
import email
import json
import os
from kafka import KafkaProducer
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
# from config import IMAP_SERVER, EMAIL, PASSWORD, KAFKA_SERVER


load_dotenv()

IMAP_SERVER = os.getenv("IMAP_SERVER")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
KAFKA_SERVER = os.getenv("KAFKA_SERVER")

# Configurar el productor de Kafka
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

def get_body(email_message):
    if email_message.is_multipart():
        for part in email_message.walk():
            if part.get_content_type() == "text/plain" and not part.get("Content-Disposition"):
                return part.get_payload(decode=True).decode(errors="ignore")
    else:
        return email_message.get_payload(decode=True).decode(errors="ignore")
    return ""

def process_email(num, mail):
    try:
        _, msg_data = mail.fetch(num, "(RFC822)")
        raw_email = msg_data[0][1]
        email_message = email.message_from_bytes(raw_email)

        body = get_body(email_message)

        email_data = {
            "id": num.decode(),
            "from": email_message["From"],
            "subject": email_message["Subject"],
            "body": body,
            "received_at": str(email_message["Date"])
        }

        print(f"\n📧 Nuevo correo de {email_data['from']} - {email_data['subject']}")

        producer.send("raw_emails", value=email_data)
        producer.flush()  # Para asegurar que se envíe inmediatamente

        print(f"✅ Correo con ID {email_data['id']} enviado al topic 'raw_emails' de Kafka.")

        # Marcar como leído para no procesar otra vez
        mail.store(num, '+FLAGS', '\\Seen')

    except Exception as e:
        print(f" Error procesando email {num}: {e}")

def fetch_emails():
    while True:
        try:
            mail = imaplib.IMAP4_SSL(IMAP_SERVER)
            mail.login(EMAIL, PASSWORD)
            mail.select("inbox")

            status, data = mail.search(None, "UNSEEN")
            if status != "OK":
                print(" Error al buscar correos")
                mail.logout()
                sleep(10)
                continue

            nums = data[0].split()
            if not nums:
                print("No hay correos nuevos. Esperando...")
                mail.logout()
                sleep(10)
                continue

            with ThreadPoolExecutor(max_workers=10) as executor:
                for num in nums:
                    executor.submit(process_email, num, mail)

            mail.logout()
            sleep(5)

        except Exception as e:
            print(f" Error general: {e}")
            sleep(30)

if __name__ == "__main__":
    fetch_emails()
