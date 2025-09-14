import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# importa la app y la dependencia real a sobreescribir
from src.main import app
from src.data.database.data_source import get_db

# --- 1) Configuración DB de pruebas (archivo pequeño para Windows compatibilidad) ---
# Puedes cambiar a "sqlite:///:memory:" si quieres, pero en memoria a veces
# falla cuando FastAPI abre conexiones separadas; el archivo es más fiable.
TEST_DB_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DB_URL,
    connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- 2) Importa explícitamente tus modelos aquí (asegura que se registren) ---
# IMPORTANTE: importa cada modelo que tengas para que sus tablas queden registradas
from src.data.models.user_model import UserModel

# --- 3) Usa la metadata asociada a los modelos para crear las tablas ---
# Esto usa la MetaData real (la que está ligada a UserModel) — evita desajustes.
metadata = UserModel.metadata
print("Tablas registradas por metadata:", list(metadata.tables.keys()))
metadata.create_all(bind=engine)  # crea las tablas en test.db si no existen

# --- 4) Sobrescribe la dependencia get_db para que use la sesión de pruebas ---
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# --- 5) Fixture del cliente de pruebas ---
@pytest.fixture()
def client():
    """
    Devuelve TestClient(app) para las pruebas.
    Limpia todas las tablas al terminar cada test.
    """
    test_client = TestClient(app)
    yield test_client

    # Limpieza: borrar todos los registros (no dropear tablas)
    with engine.connect() as connection:
        with connection.begin():
            # eliminamos filas en orden inverso por seguridad (FKs)
            for table in reversed(metadata.sorted_tables):
                connection.execute(table.delete())
