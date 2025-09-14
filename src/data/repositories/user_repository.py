from sqlalchemy.orm import Session
from src.data.mappers.user_mapper import UserMapper
from src.domain.user import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user_domain):
        # Mapea a SQLAlchemy
        user_model = UserMapper.to_model(user_domain)
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)
        # Devuelve el dominio
        return UserMapper.to_domain(user_model)
    
    def get_user_by_username(self, username: str) -> User | None:
        return self.session.query(User).filter_by(username=username).first()

    def list_users(self) -> list[User]:
        return self.session.query(User).all()

    def delete_user(self, user_id: int) -> bool:
        user = self.session.query(User).get(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False
