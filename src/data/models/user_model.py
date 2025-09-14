from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from src.data.database.data_source import DataSource

# Crea una instancia del DataSource para acceder a Base
ds = DataSource()

class UserModel(ds.get_data_source().Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    date = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
