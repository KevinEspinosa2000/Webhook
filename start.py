from flask import Flask         # Framework
from markupsafe import escape   # Para proteger contra ataques XSS
import requests                 # Solicitudes HTTP
import threading                # Tareas en segundo plano
import time                     # Pausar entre envios
import os                       # Variables de entorno

app = Flask(__name__)

# Configuracion desde variables de entorno
ENDPOINT = os.getenv("Webhook_Endpoint", "https://ejemplo.com/webhook")
INTERVAL = int(os.getenv("Intervalo_Webhook", 60))  #Segundos

def send_message():
    while True:
        try:
            response = requests.post(ENDPOINT, json={"message": "Webhook desde Flask"})
            print(f"Mensaje enviado: {response.status_code}")
        except Exception as e:
            print(f"Error al enviar el mensaje: {e}")
        time.sleep(INTERVAL)    

@app.route("/")
def status():
    return f"Webhook activo. Enviado a {ENDPOINT} cada {INTERVAL} segundos"

if __name__ == "__main__":
    # Inicida el hilo para mandar mensajes periodicos
    thread = threading.Thread(target=send_message, daemon=True)
    thread.start()

    # Inicia el servidor Flask
    app.run (host="0.0.0.0", port=1000)