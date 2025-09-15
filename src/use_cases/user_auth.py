from sqlalchemy.orm import Session
from src.data.repositories.user_repository import UserRepository
from src.core.security import verify_password

class AuthenticateUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, session: Session, username: str, password: str):
        user = self.user_repo.get_user_by_username(session, username)
        if not user or not verify_password(password, user.password):
            return None
        return user