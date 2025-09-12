from pydantic import BaseModel

# Verifica los datos in/out, les agrega tipos :)

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    role: str

class Token(BaseModel):
    access_token: str
    token_type: str
