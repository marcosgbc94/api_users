from sqlalchemy.orm import Session
from src.data.repositories.user_repository import UserRepository
from src.core.security import verify_password

def authenticate_user(repo: UserRepository, session: Session, username: str, password: str):
    user = repo.get_user_by_username(session, username)
    if not user or not verify_password(password, user.password):
        return None
    return user
