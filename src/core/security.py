# Módulo de seguridad

from datetime import datetime, timedelta, timezone # Para manejar fechas (expiración del token)
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError # Librería para crear y leer JSON Web Tokens (JWT)
from passlib.context import CryptContext
from pytest import Session # Para hashear y verificar contraseñas (bcrypt)
from src.data.database.data_source import get_db
from src.data.models.user_model import UserModel
from src.core.config import settings # Configuración central

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

# Crea un contexto de encriptación con bcrypt (el algoritmo recomendado para passwords).
# deprecated="auto" hace que si cambias el algoritmo en el futuro, los nuevos hashes usen el nuevo, pero los viejos sigan siendo válidos.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Contexto de hashing

# Convierte una contraseña en un hash irreversible. 
# Ejemplo: "hola123" → "$2b$12$7jLf9M..."
def hash_password(password: str) -> str: 
    return pwd_context.hash(password)

# Compara el password ingresado por el usuario con el hash guardado en BD. 
# Devuelve True si coinciden, False si no
def verify_password(password: str, hashed: str) -> bool: 
    return pwd_context.verify(password, hashed)

# Devuelve un token JWT, que es lo que el cliente usará como credencial
def create_access_token(data: dict, expires_minutes: int = settings.ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy() # Toma un diccionario data (por ejemplo { "sub": "marcos" }
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes) # Le agrega una fecha de expiración (exp)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM) # Lo firma con SECRET_KEY y HS256. 

# Revisa si el token es válido (firma correcta, no está vencido, etc.).
# Devuelve los datos originales (sub, role, etc.).
# Si no es válido → lanza JWTError.
def decode_token(token: str):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UserModel:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    username: str = payload.get("sub")
    return db.query(UserModel).filter(UserModel.username == username).first()