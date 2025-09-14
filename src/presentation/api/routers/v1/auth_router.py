from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.core import security
from src.use_cases import user_auth
from src.presentation.schemas.user_schema import Token
from src.data.database.data_source import get_db
from src.data.repositories.user_repository import UserRepository

router = APIRouter()
user_repo = UserRepository()

@router.post("/login", response_model=Token)
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_auth.authenticate_user(user_repo, db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    
    # Añadimos el rol al payload del token
    token_data = {"sub": user.username, "role": user.role}
    token = security.create_access_token(token_data)
    
    return {"access_token": token, "token_type": "bearer"}