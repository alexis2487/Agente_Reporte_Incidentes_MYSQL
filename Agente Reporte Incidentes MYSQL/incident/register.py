from db.database import SessionLocal
from db.models import Incident
from datetime import datetime

def register_incident():
    session = SessionLocal()
    try:
        tipo = input("Tipo de incidente: ")
        desc = input("Descripción: ")
        ip = input("IP asociada (opcional): ")
        domain = input("Dominio (opcional): ")
        user = input("Usuario afectado (opcional): ")
        severity = input("Gravedad (baja/media/alta): ")

        incidente = Incident(
            type=tipo,
            description=desc,
            ip=ip or None,
            domain=domain or None,
            user=user or None,
            severity=severity.lower(),
            created_at=datetime.utcnow()
        )

        session.add(incidente)
        session.commit()
        print("✅ Incidente registrado correctamente.")

    except Exception as e:
        print(f"❌ Error: {e}")
        session.rollback()
    finally:
        session.close()
