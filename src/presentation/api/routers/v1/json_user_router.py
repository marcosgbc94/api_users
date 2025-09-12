from fastapi import APIRouter, Depends
from src.data.repositories.json_user_repository import JSONUserRepository
from src.presentation.schemas.user_schema import UserCreate, UserOut

router = APIRouter()
repo = JSONUserRepository()

@router.post("/users", response_model=UserOut)
def create_user(user: UserCreate):
    new_user = repo.create(user.username, user.password)
    if not new_user:
        return {"error": "Usuario ya existe"}
    return {"username": new_user.username, "role": new_user.role}

@router.get("/users", response_model=list[UserOut])
def list_users():
    # Cargar usuarios actuales
    users = repo.users
    return [{"username": u.username, "role": u.role} for u in users]
