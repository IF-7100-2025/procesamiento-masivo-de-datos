📧 Sistema de Procesamiento de Emails Masivos
Daily Planet Email System es una solución escalable para procesar, clasificar y responder emails automáticamente usando Kafka, Python y FastAPI.

🚀 Requisitos Previos
Docker y Docker Compose

Python 3.9+

Cuenta de email (ej: Gmail) con acceso IMAP/SMTP

📦 Instalación
1. Clonar el repositorio
bash
git clone [URL_DEL_REPOSITORIO]  
cd email_system  
2. Configurar variables de entorno
Crear un archivo .env en la raíz del proyecto con:

ini
# IMAP (ej: Gmail)  
IMAP_SERVER=imap.gmail.com  
EMAIL=tu_email@gmail.com  
PASSWORD=tu_contraseña_o_app_password  

# SMTP (ej: Gmail)  
SMTP_SERVER=smtp.gmail.com  
SMTP_PORT=587  
SMTP_USER=tu_email@gmail.com  
SMTP_PASSWORD=tu_contraseña_o_app_password  

# Kafka  
KAFKA_SERVER=localhost:9092  
3. Instalar dependencias
bash
pip install -r collector/requirements.txt  
pip install -r processor/requirements.txt  
pip install -r responder/requirements.txt  
pip install -r api/requirements.txt  
4. Iniciar Kafka con Docker
bash
docker-compose up -d  
🛠 Estructura del Proyecto
email_system/  
├── collector/                  # Recolector de emails (IMAP → Kafka)  
│   ├── imap_collector.py  
│   └── requirements.txt  
├── processor/                  # Clasificador de emails  
│   ├── classifier.py  
│   └── requirements.txt  
├── responder/                  # Respondedor automático (SMTP)  
│   ├── smtp_responder.py  
│   ├── templates/  
│   └── requirements.txt  
├── api/                        # Dashboard de métricas (FastAPI)  
│   ├── main.py  
│   ├── routers/  
│   └── requirements.txt  
├── docker-compose.yml          # Configuración de Kafka  
└── .env                        # Variables de entorno  
▶ Cómo Ejecutar
1. Iniciar Kafka
bash
docker-compose up -d  
2. Ejecutar servicios en orden
Servicio	Comando	Descripción
Collector	python collector/imap_collector.py	Monitorea el buzón de emails
Processor	python processor/classifier.py	Clasifica emails
Responder	python responder/smtp_responder.py	Envía respuestas
API (Dashboard)	uvicorn api.main:app --reload	Métricas en http://localhost:8000
📌 Nota: Ejecuta cada comando en una terminal separada.

🌐 Endpoints del Dashboard (FastAPI)
Endpoint	Método	Descripción
/health	GET	Verifica el estado del sistema
/stats	GET	Muestra métricas de emails procesados
/metrics	GET	Datos de Prometheus (para monitoreo)
🔍 Pruebas
Envía un email de prueba a tu buzón configurado en IMAP.

Verifica que:

Aparezca en el log del Collector.

Se clasifique correctamente en el Processor.

Se envíe una respuesta automática (verifica tu bandeja de salida SMTP).

🛑 Detener el Sistema
Presiona Ctrl+C en cada terminal de los servicios Python.

Detén Kafka:

bash
docker-compose down  
📌 Notas Importantes
Para Gmail, habilita "Contraseñas de aplicación" si usas 2FA.

Kafka debe estar en ejecución antes de iniciar los demás servicios.
