import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

recipients = [SMTP_USER]
senders = ["luisballar@gmail.com", "jeancarlocldrn@gmail.com"]

test_emails = [
    {
        "id": "email-001",
        "subject": "Suscripción al newsletter",
        "body": "Hola, quiero suscribirme al newsletter de Daily Planet"
    },
    {
        "id": "email-002",
        "subject": "Consulta sobre precios",
        "body": "Quisiera saber los precios de sus publicaciones"
    },
    {
        "id": "email-003",
        "subject": "Reclamo por error en artículo",
        "body": "El artículo de hoy tiene datos incorrectos, por favor revisar"
    },
    {
        "id": "email-004",
        "subject": "Tengo una queja urgente",
        "body": "Me parece muy mal lo publicado sobre mi ciudad"
    },
    {
        "id": "email-005",
        "subject": "Felicitaciones por el reportaje",
        "body": "Excelente cobertura del evento político"
    },
    {
        "id": "email-006",
        "subject": "Problema con suscripción",
        "body": "No puedo acceder al contenido premium después del pago"
    },
    {
        "id": "email-007",
        "subject": "Gracias por su excelente servicio",
        "body": "Estoy muy contento con la calidad del contenido"
    },
    {
        "id": "email-008",
        "subject": "ERROR EN PUBLICACIÓN",
        "body": "Hay un error grave en el artículo del día"
    },
    {
        "id": "email-009",
        "subject": "Reclamo por contenido ofensivo",
        "body": "El lenguaje utilizado en el artículo es inaceptable"
    },
    {
        "id": "email-010",
        "subject": "Sugerencia de mejora",
        "body": "Podrían incluir una sección de análisis económico"
    },
    {
        "id": "email-011",
        "subject": "URGENTE: Contenido falso",
        "body": "Lo que publicaron sobre el evento no es cierto"
    },
    {
        "id": "email-012",
        "subject": "Consulta general",
        "body": "¿Tienen contenido educativo para niños?"
    },
    {
        "id": "email-013",
        "subject": "Reclamo por plagio",
        "body": "El artículo parece una copia de otra fuente"
    },
    {
        "id": "email-014",
        "subject": "Me gustaría colaborar con ustedes",
        "body": "Soy periodista y tengo interés en escribir para su medio"
    },
    {
        "id": "email-015",
        "subject": "Queja sobre parcialidad",
        "body": "La cobertura política parece estar muy inclinada"
    }
]

def send_email(sender, recipient, subject, body):
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(sender, recipient, msg.as_string())
            print(f"[✓] Enviado desde {sender} a {recipient} con asunto: {subject}")
    except Exception as e:
        print(f"[✗] Error al enviar desde {sender}: {e}")

if __name__ == "__main__":
    for idx, email_data in enumerate(test_emails):
        sender = senders[idx % len(senders)]
        send_email(sender, recipients[0], email_data["subject"], email_data["body"])
        time.sleep(1)

    print("\nTodos los correos han sido enviados.")