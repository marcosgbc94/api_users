import os
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from src.data.database.base import Base

load_dotenv()  # Carga variables del .env

class DataSourceMySQL:
    def __init__(self):
        self.user = os.getenv("MYSQL_USER")
        self.password = os.getenv("MYSQL_PASSWORD")
        self.host = os.getenv("MYSQL_HOST")
        self.port = os.getenv("MYSQL_PORT")
        self.db_name = os.getenv("MYSQL_DB")

        self.SQLALCHEMY_DATABASE_URL = (
            f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        )

        self.engine = create_engine(
            self.SQLALCHEMY_DATABASE_URL,
            pool_pre_ping=True,
            echo=True
        )
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )
        self.Base = Base

    def get_session(self):
        return self.SessionLocal()
    
    def init_db(self):
        # Importa tus modelos aquí para que SQLAlchemy los registre en Base
        import src.data.models.user_model  # importa todos tus modelos aquí
        self.Base.metadata.create_all(bind=self.engine)
    
