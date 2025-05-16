import imaplib
import email
import json
from kafka import KafkaProducer
from time import sleep
from config import IMAP_SERVER, EMAIL, PASSWORD, KAFKA_SERVER

# Configurar el productor de Kafka
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

def fetch_emails():
    try:
        # Conectar al servidor IMAP
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        # Buscar todos los correos (puedes cambiar "ALL" por "UNSEEN" si solo quieres no leídos)
        status, data = mail.search(None, "ALL")
        if status != "OK":
            print("❌ Error al buscar correos")
            return

        # Iterar sobre cada correo
        for num in data[0].split():
            _, msg_data = mail.fetch(num, "(RFC822)")
            raw_email = msg_data[0][1]
            email_message = email.message_from_bytes(raw_email)

            # Extraer cuerpo del mensaje
            if email_message.is_multipart():
                parts = email_message.get_payload()
                body = ''
                for part in parts:
                    if part.get_content_type() == 'text/plain':
                        body += part.get_payload(decode=True).decode(errors="ignore")
            else:
                body = email_message.get_payload(decode=True).decode(errors="ignore")

            email_data = {
                "id": num.decode(),
                "from": email_message["From"],
                "subject": email_message["Subject"],
                "body": body,
                "received_at": str(email_message["Date"])
            }

            # Mostrar el correo en consola
            print("\n📧 Nuevo correo recibido")
            print(f"De: {email_data['from']}")
            print(f"Asunto: {email_data['subject']}")
            print(f"Fecha: {email_data['received_at']}")
            print(f"Cuerpo:\n{email_data['body']}")

            # Enviar a Kafka
            producer.send("raw_emails", value=email_data)

        mail.logout()

    except Exception as e:
        print(f"❌ Error al procesar correos: {e}")

if __name__ == "__main__":
    fetch_emails()
