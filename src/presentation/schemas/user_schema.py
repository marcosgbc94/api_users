# src/domain/schemas.py
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: Optional[int]
    username: str
    date: Optional[datetime]

class Token(BaseModel):
    access_token: str
    token_type: str

class Config:
    orm_mode = True  # Esto permite recibir objetos SQLAlchemy
