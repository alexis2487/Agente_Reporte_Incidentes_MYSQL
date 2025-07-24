from db.database import Base, engine
from db.models import Incident

print("Inicializando base de datos...")
Base.metadata.create_all(bind=engine)
print("Tablas creadas correctamente.")
