from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from src.core import security
from src.use_cases import user_auth
from src.presentation.schemas.user_schema import Token

router = APIRouter()

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = security.create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
