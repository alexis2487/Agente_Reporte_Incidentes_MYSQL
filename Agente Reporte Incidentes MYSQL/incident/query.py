from db.database import SessionLocal
from db.models import Incident
from rich.table import Table
from rich.console import Console

def query_incidents():
    session = SessionLocal()
    console = Console()

    tipo = input("Filtrar por tipo (Enter para todos): ")
    severidad = input("Filtrar por gravedad (baja/media/alta): ")

    query = session.query(Incident)

    if tipo:
        query = query.filter(Incident.type == tipo)
    if severidad:
        query = query.filter(Incident.severity == severidad.lower())

    resultados = query.all()

    if not resultados:
        print("⚠️ No se encontraron incidentes.")
        return

    table = Table(title="Incidentes Registrados")
    table.add_column("ID", style="bold")
    table.add_column("Tipo")
    table.add_column("Gravedad")
    table.add_column("Fecha")
    table.add_column("IP")
    table.add_column("Dominio")
    table.add_column("Usuario")

    for inc in resultados:
        table.add_row(
            str(inc.id), inc.type, inc.severity, str(inc.created_at),
            inc.ip or "-", inc.domain or "-", inc.user or "-"
        )

    console.print(table)
    session.close()
