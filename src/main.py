import os
import time
from fastapi import FastAPI
from src.data.database.data_source import DataSource
from src.presentation.errors import error_handler
from src.presentation.api.routers.v1 import user_router, auth_router
from sqlalchemy.exc import OperationalError

app = FastAPI()

ENV = os.getenv("ENVIRONMENT", "dev")
MAX_TIMEOUT_DB = int(os.getenv("MAX_DB_TIMEOUT", 30))  # por defecto 30 segundos

ds = DataSource()

# Espera a que la DB esté lista
MAX_WAIT = MAX_TIMEOUT_DB
WAIT_INTERVAL = 2
elapsed = 0
db_status = False;

while elapsed < MAX_WAIT:
    try:
        conn = ds.get_data_source().engine.connect()
        conn.close()
        db_status = True;
        print("La base de datos está lista")
        break
    except OperationalError:
        print("Esperando a que la base de datos arranque...")
        time.sleep(WAIT_INTERVAL)
        elapsed += WAIT_INTERVAL
else:
    raise RuntimeError("Timeout: la base de datos no se levantó a tiempo")

if ENV == "dev" and db_status: # Crea tablas automáticamente en dev y si la DB está disponible
    ds.get_data_source().init_db() 

#  Middleware global
app.middleware("http")(error_handler)

if db_status: # Routers solo si la DB está disponible
    app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["auth"])
    app.include_router(user_router.router, prefix="/api/v1", tags=["users"])
