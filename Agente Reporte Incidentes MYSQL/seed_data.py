import random
from db.database import SessionLocal
from db.models import Incident

# Lista de posibles valores
titles = [
    "Ataque DDoS", "Intrusión en servidor", "Phishing masivo", "Ransomware",
    "Malware USB", "Fuga de datos", "Ataque interno", "Puerto expuesto",
    "Exploit Zero-Day", "Brute Force Login"
]

descriptions = [
    "Saturación de red detectada", "Acceso no autorizado detectado",
    "Usuarios reportan correos sospechosos", "Archivos cifrados en múltiples equipos",
    "Se encontró malware en un dispositivo removible", "Datos sensibles expuestos públicamente",
    "Empleado accedió a recursos no autorizados", "Puerto inseguro abierto en firewall",
    "Vulnerabilidad no parcheada explotada", "Intentos masivos de inicio de sesión detectados"
]

severities = ["Baja", "Media", "Alta", "Crítica"]

# Crear sesión
session = SessionLocal()

# Limpiar la tabla antes (opcional)
session.query(Incident).delete()

# Crear 100 incidentes aleatorios
for _ in range(100):
    incident = Incident(
        title=random.choice(titles),
        description=random.choice(descriptions),
        severity=random.choice(severities)
    )
    session.add(incident)

# Confirmar cambios
session.commit()
session.close()

print("100 incidentes generados correctamente.")
