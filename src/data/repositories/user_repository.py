from sqlalchemy.orm import Session
from src.data.mappers.user_mapper import UserMapper
from src.data.models.user_model import UserModel
from src.domain.user import User

class UserRepository:
    def create_user(self, session: Session, user_domain: User) -> User:
        user_model = UserMapper.to_model(user_domain)
        session.add(user_model)
        session.commit()
        session.refresh(user_model)
        return UserMapper.to_domain(user_model)

    def get_user_by_username(self, session: Session, username: str) -> User | None:
        user_model = session.query(UserModel).filter_by(username=username).first()
        if user_model:
            return UserMapper.to_domain(user_model)
        return None

    def list_users(self, session: Session) -> list[User]:
        users_model = session.query(UserModel).all()
        return [UserMapper.to_domain(user) for user in users_model]

    def delete_user(self, session: Session, user_id: int) -> bool:
        user = session.query(UserModel).get(user_id)
        if user:
            session.delete(user)
            session.commit()
            return True
        return False