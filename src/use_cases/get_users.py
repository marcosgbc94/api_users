from sqlalchemy.orm import Session
from src.domain.user import User
from src.data.repositories.user_repository import UserRepository

class GetUsers:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, session: Session):
        return self.user_repo.list_users(session)