from dataclasses import dataclass

# Esta hermosa cosita define lo que llega de BD o JSON

@dataclass
class User:
    username: str
    hashed_password: str
    role: str = "user"
