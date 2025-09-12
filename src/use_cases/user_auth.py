from src.data.repositories.user_repository import UserRepository
from src.core.security import verify_password

repo = UserRepository()  # Inyección manual (podría usarse Depends)

def authenticate_user(username: str, password: str):
    user = repo.get_by_username(username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
