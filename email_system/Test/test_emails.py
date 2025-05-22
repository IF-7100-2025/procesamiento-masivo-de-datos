# test_producer.py
import json
import time
from kafka import KafkaProducer

KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

test_emails = [
    {
        "id": "email-001",
        "from": "luisdayluke@gmail.com",
        "subject": "Suscripción al newsletter",
        "body": "Hola, quiero suscribirme al newsletter de Daily Planet"
    },
    {
        "id": "email-002",
        "from": "luisdayluke@gmail.com",
        "subject": "Consulta sobre precios",
        "body": "Quisiera saber los precios de sus publicaciones"
    },
    {
        "id": "email-003",
        "from": "luisdayluke@gmail.com",
        "subject": "Reclamo por error en artículo",
        "body": "El artículo de hoy tiene datos incorrectos, por favor revisar"
    },
    {
        "id": "email-004",
        "from": "luisdayluke@gmail.com",
        "subject": "Tengo una queja urgente",
        "body": "Me parece muy mal lo publicado sobre mi ciudad"
    },
    {
        "id": "email-005",
        "from": "luisdayluke@gmail.com",
        "subject": "Felicitaciones por el reportaje",
        "body": "Excelente cobertura del evento político"
    },
    {
        "id": "email-006",
        "from": "luisdayluke@gmail.com",
        "subject": "Solicitud de entrevista",
        "body": "Me gustaría solicitar una entrevista para hablar sobre el artículo publicado"
    },
    {
        "id": "email-007",
        "from": "luisdayluke@gmail.com",
        "subject": "Sugerencia de contenido",
        "body": "Sugiero que cubran más temas de tecnología en sus publicaciones"
    },
    {
        "id": "email-008",
        "from": "luisdayluke@gmail.com",
        "subject": "Problema con suscripción",
        "body": "No he podido completar la suscripción al newsletter"
    },
    {
        "id": "email-009",
        "from": "luisdayluke@gmail.com",
        "subject": "Recomendación para mejorar",
        "body": "Sería bueno incluir más imágenes en sus reportajes"
    },
    {
        "id": "email-010",
        "from": "luisdayluke@gmail.com",
        "subject": "Solicitud de información",
        "body": "¿Podrían enviarme información sobre sus próximos eventos?"
    },
    {
        "id": "email-011",
        "from": "luisdayluke@gmail.com",
        "subject": "Reporte de fallo técnico",
        "body": "El sitio web no carga correctamente desde ayer"
    },
    {
        "id": "email-012",
        "from": "luisdayluke@gmail.com",
        "subject": "Consulta sobre publicidad",
        "body": "Estoy interesado en publicitar en su plataforma"
    },
    {
        "id": "email-013",
        "from": "luisdayluke@gmail.com",
        "subject": "Agradecimiento por el apoyo",
        "body": "Gracias por la cobertura del evento benéfico"
    },
    {
        "id": "email-014",
        "from": "luisdayluke@gmail.com",
        "subject": "Petición de corrección",
        "body": "Encontré un error en la sección de deportes"
    },
    {
        "id": "email-015",
        "from": "luisdayluke@gmail.com",
        "subject": "Solicitud de colaboración",
        "body": "Me gustaría colaborar con artículos para su medio"
    },
    {
        "id": "email-016",
        "from": "luisdayluke@gmail.com",
        "subject": "Pregunta sobre archivo histórico",
        "body": "¿Dónde puedo consultar archivos de publicaciones anteriores?"
    },
    {
        "id": "email-017",
        "from": "luisdayluke@gmail.com",
        "subject": "Reclamo por publicidad engañosa",
        "body": "Un anuncio en su sitio parece ser engañoso"
    },
    {
        "id": "email-018",
        "from": "luisdayluke@gmail.com",
        "subject": "Solicitud de entrevista exclusiva",
        "body": "Quisiera coordinar una entrevista exclusiva con el editor"
    },
    {
        "id": "email-019",
        "from": "luisdayluke@gmail.com",
        "subject": "Reporte de contenido inapropiado",
        "body": "Hay contenido que considero inapropiado en la sección de comentarios"
    },
    {
        "id": "email-020",
        "from": "luisdayluke@gmail.com",
        "subject": "Sugerencia para la app móvil",
        "body": "Sería bueno que la app tenga notificaciones push"
    },
    {
        "id": "email-021",
        "from": "luisdayluke@gmail.com",
        "subject": "Consulta sobre suscripciones corporativas",
        "body": "¿Ofrecen suscripciones para empresas?"
    },
    {
        "id": "email-022",
        "from": "luisdayluke@gmail.com",
        "subject": "Comentario positivo",
        "body": "Me gusta la nueva sección de noticias locales"
    },
    {
        "id": "email-023",
        "from": "luisdayluke@gmail.com",
        "subject": "Solicitud de cambio de datos personales",
        "body": "Quisiera actualizar mis datos en la cuenta"
    },
    {
        "id": "email-024",
        "from": "luisdayluke@gmail.com",
        "subject": "Reclamo por demora en entrega",
        "body": "No he recibido el último número impreso"
    },
    {
        "id": "email-025",
        "from": "luisdayluke@gmail.com",
        "subject": "Felicitaciones por aniversario",
        "body": "Felicitaciones por los 10 años de su publicación"
    }
]

for email in test_emails:
    producer.send("raw_emails", value=email)
    print(f"Email enviado: {email['id']}")
    time.sleep(0.5)

producer.flush()
print("Todos los emails de prueba fueron enviados.")
