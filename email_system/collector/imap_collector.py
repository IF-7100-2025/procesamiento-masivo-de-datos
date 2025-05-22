import imaplib
import email
import json
import os
from kafka import KafkaProducer
from time import sleep
from email.header import decode_header
from dotenv import load_dotenv

load_dotenv()

IMAP_SERVER = os.getenv("IMAP_SERVER")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
KAFKA_SERVER = os.getenv("KAFKA_SERVER")

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

def decode_mime_words(header):
    if header:
        parts = decode_header(header)
        return ''.join([
            part.decode(encoding or 'utf-8', errors='ignore') if isinstance(part, bytes) else part
            for part, encoding in parts
        ])
    return ''

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
            "from": decode_mime_words(email_message["From"]),
            "subject": decode_mime_words(email_message["Subject"]),
            "body": body,
            "received_at": str(email_message["Date"])
        }

        print(f"\n Nuevo correo de {email_data['from']} - {email_data['subject']}")

        producer.send("raw_emails", value=email_data)
        producer.flush()  

        print(f" Correo con ID {email_data['id']} enviado al topic 'raw_emails' de Kafka.")

        # Marcar como leído
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

            for num in nums:
                process_email(num, mail)

            mail.logout()
            sleep(5)

        except Exception as e:
            print(f" Error general: {e}")
            sleep(30)

if __name__ == "__main__":
    fetch_emails()
