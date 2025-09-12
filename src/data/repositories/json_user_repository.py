import json
from pathlib import Path
from src.domain.user import User
from src.core.security import hash_password

FILE_PATH = Path(__file__).parent.parent / "json" / "users.json"

class JSONUserRepository:
    def __init__(self):
        FILE_PATH.touch(exist_ok=True)  # crea el archivo si no existe
        self._load_users()

    def _load_users(self):
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                self.users = [User(**u) for u in json.load(f)]
        except json.JSONDecodeError:
            self.users = []

    def _save_users(self):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump([u.__dict__ for u in self.users], f, indent=4)

    def create(self, username: str, password: str):
        if self.get_by_username(username):
            return None
        user = User(username=username, hashed_password=hash_password(password))
        self.users.append(user)
        self._save_users()
        return user

    def get_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user
        return None
