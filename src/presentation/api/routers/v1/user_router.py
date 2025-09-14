from fastapi import APIRouter
from src.presentation.schemas.user_schema import UserOut
from src.data.database.data_source import DataSource
from src.data.repositories.user_repository import UserRepository
from src.use_cases.user_create import CreateUserUseCase

router = APIRouter()

# Crear sesión de SQLAlchemy
ds = DataSource()

user_repo = UserRepository(ds.get_data_source().get_session())
create_user_uc = CreateUserUseCase(user_repo)

@router.post("/users", response_model=UserOut)
def create_user(username: str, password: str):
    return create_user_uc.execute(username, password)
