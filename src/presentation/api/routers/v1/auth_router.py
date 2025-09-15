from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.data.database.data_source import get_db
from src.core import security
from src.use_cases.user_auth import AuthenticateUser
from src.presentation.schemas.user_schema import Token
from src.data.database.data_source import get_db
from src.data.repositories.user_repository import UserRepository

router = APIRouter()
user_repo = UserRepository()

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    authenticate_user = AuthenticateUser(user_repo)
    user = authenticate_user.execute(db, form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos"
        )

    if not security.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos"
        )

    token_data = {"sub": user.username}
    token = security.create_access_token(token_data)
    
    return {"access_token": token, "token_type": "bearer"}