import imaplib
import email
import json
from time import sleep
from kafka import KafkaProducer
from config import IMAP_SERVER, EMAIL, PASSWORD, KAFKA_SERVER

# Configura Kafka
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)

def fetch_emails():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")
        
        while True:
            _, data = mail.search(None, "UNSEEN")
            for num in data[0].split():
                _, msg_data = mail.fetch(num, "(RFC822)")
                raw_email = msg_data[0][1]
                email_message = email.message_from_bytes(raw_email)
                
                email_data = {
                    "id": num.decode(),
                    "from": email_message["From"],
                    "subject": email_message["Subject"],
                    "body": email_message.get_payload(),
                    "received_at": str(email_message["Date"])
                }
                
                producer.send("raw_emails", value=email_data)
                print(f"📩 Email {num} enviado a Kafka")
            
            sleep(60)  # Espera 1 minuto antes de revisar nuevamente

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    fetch_emails()