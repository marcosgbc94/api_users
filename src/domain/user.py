from datetime import datetime
from typing import Optional

class User:
    def __init__(self, username: str, password: str, id: Optional[int] = None, date: Optional[datetime] = None):
        self.id = id
        self.username = username
        self.password = password
        self.date = date or datetime.utcnow()  # si no viene, usa fecha/hora actual


