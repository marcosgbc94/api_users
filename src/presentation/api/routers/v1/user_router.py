from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.presentation.schemas.user_schema import UserCreate, UserOut
from src.data.database.data_source import get_db
from src.data.repositories.user_repository import UserRepository
from src.use_cases.user_create import CreateUserUseCase
from src.use_cases.get_users import GetUsers
from typing import List

router = APIRouter()

user_repo = UserRepository()

@router.post("/users", response_model=UserOut, status_code=201)
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    create_user_uc = CreateUserUseCase(user_repo)
    return create_user_uc.execute(db, request.username, request.password)

@router.get("/users", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    get_users = GetUsers(user_repo)
    return get_users.execute(db)