import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Template
import json
from kafka import KafkaConsumer
from config import SMTP_CONFIG, KAFKA_SERVER
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_template():
    with open("templates/acknowledgment.html", "r") as f:
        return Template(f.read())

def send_acknowledgment(email_data):
    template = load_template()
    html_content = template.render(
        subject=email_data.get("subject", "Sin asunto"),
        sender=email_data["from"]
    )

    msg = MIMEMultipart()
    msg["From"] = SMTP_CONFIG["sender_email"]
    msg["To"] = email_data["from"]
    msg["Subject"] = "✅ Confirmación de recepción"
    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP(SMTP_CONFIG["server"], SMTP_CONFIG["port"]) as server:
            server.starttls()
            server.login(SMTP_CONFIG["user"], SMTP_CONFIG["password"])
            server.send_message(msg)
        logger.info(f"📤 Respuesta enviada a {email_data['from']}")
    except Exception as e:
        logger.error(f"❌ Error enviando email: {e}")

def main():
    consumer = KafkaConsumer(
        "acknowledgement_queue",
        bootstrap_servers=KAFKA_SERVER,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        group_id="smtp-responder"
    )

    for message in consumer:
        try:
            email_data = message.value
            send_acknowledgment(email_data)
        except json.JSONDecodeError:
            logger.error("Error decodificando mensaje de Kafka")
        except Exception as e:
            logger.error(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()