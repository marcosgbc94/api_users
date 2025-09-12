from src.data.repositories.json_user_repository import JSONUserRepository
from src.core.security import verify_password

repo = JSONUserRepository()  # Inyección manual (podría usarse Depends)

def authenticate_user(username: str, password: str):
    user = repo.get_by_username(username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user