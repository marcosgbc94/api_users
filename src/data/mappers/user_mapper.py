from src.domain.user import User
from src.data.models.user_model import UserModel

class UserMapper:
    @staticmethod
    def to_model(user_domain: User) -> UserModel:
        return UserModel(
            username=user_domain.username,
            password=user_domain.password
        )

    @staticmethod
    def to_domain(user_model: UserModel) -> User:
        return User(
            id=user_model.id,
            username=user_model.username,
            password=user_model.password,
            date=user_model.date
        )
