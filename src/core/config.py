import os
from pydantic import BaseModel

class Settings(BaseModel):
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecret")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
