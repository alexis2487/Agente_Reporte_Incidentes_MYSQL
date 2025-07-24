import typer
from db.models import Incident
from db.database import SessionLocal
from datetime import datetime
from typing import Optional

app = typer.Typer()

@app.command()
def add(title: str, description: str, severity: str):
    """
    Agrega un nuevo incidente de ciberseguridad.
    """
    db = SessionLocal()
    incident = Incident(
        title=title,
        description=description,
        severity=severity,
        timestamp=datetime.now()
    )
    db.add(incident)
    db.commit()
    db.refresh(incident)
    db.close()
    typer.echo(f"✅ Incidente agregado con ID {incident.id}")

@app.command()
def list():
    """
    Lista todos los incidentes con fecha.
    """
    db = SessionLocal()
    incidents = db.query(Incident).all()
    db.close()
    if incidents:
        for i in incidents:
            print(f"[{i.id}] {i.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | {i.title} | {i.severity} - {i.description}")
    else:
        print("❌ No hay incidentes registrados.")

@app.command()
def search(keyword: str):
    """
    Busca incidentes por palabra clave en el título o descripción.
    """
    db = SessionLocal()
    results = db.query(Incident).filter(
        Incident.title.ilike(f"%{keyword}%") |
        Incident.description.ilike(f"%{keyword}%")
    ).all()
    db.close()
    if results:
        for r in results:
            print(f"[{r.id}] {r.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | {r.title} | {r.severity} - {r.description}")
    else:
        print(f"❌ No se encontraron incidentes con la palabra clave '{keyword}'.")

if __name__ == "__main__":
    app()
