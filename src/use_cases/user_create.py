from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.domain.user import User
from src.data.repositories.user_repository import UserRepository
from src.core.security import hash_password

class CreateUserUseCase:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, session: Session, username: str, password: str):
        existing_user = self.user_repo.get_user_by_username(session, username)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="El nombre de usuario ya está en uso"
            )
        hashed_pw = hash_password(password)
        user = User(username=username, password=hashed_pw)
        return self.user_repo.create_user(session, user)