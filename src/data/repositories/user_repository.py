from src.domain.user import User
from src.core.security import hash_password

# Repositorio en memoria (podría cambiarse por JSON o DB)
class UserRepository:
    def __init__(self):
        self.users = {}

    def create(self, username: str, password: str):
        if username in self.users:
            return None
        user = User(username=username, hashed_password=hash_password(password))
        self.users[username] = user
        return user

    def get_by_username(self, username: str):
        return self.users.get(username)
