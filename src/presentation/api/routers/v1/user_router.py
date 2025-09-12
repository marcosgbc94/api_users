from fastapi import APIRouter, Depends
from src.data.repositories.user_repository import UserRepository
from src.presentation.schemas.user_schema import UserCreate, UserOut

router = APIRouter()
repo = UserRepository()

@router.post("/users", response_model=UserOut)
def create_user(user: UserCreate):
    new_user = repo.create(user.username, user.password)
    if not new_user:
        return {"error": "Usuario ya existe"}
    return {"username": new_user.username, "role": new_user.role}
