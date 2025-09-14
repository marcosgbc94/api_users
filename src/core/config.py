# Archivo de configuración central

import os # Interatua con el sistema operativo
from pydantic import BaseModel # Librería que valida y convierte datos

class Settings(BaseModel): # Hereda de la clase padre: BaseModel
    # Valores por defecto
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("30")

settings = Settings() # Se invoca en el mismo archivo
