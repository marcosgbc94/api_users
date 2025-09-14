# src/domain/schemas.py
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class UserOut(BaseModel):
    id: Optional[int]
    username: str
    date: Optional[datetime]

    class Config:
        orm_mode = True  # Esto permite recibir objetos SQLAlchemy
