from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from db.database import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1024), nullable=False)
    severity = Column(String(50), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)  # <--- ESTA LÍNEA ES CLAVE
