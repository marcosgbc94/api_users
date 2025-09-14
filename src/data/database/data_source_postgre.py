import os
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()  # Carga variables del .env

class DataSourcePostgre:
    def __init__(self):
        self.user = os.getenv("POSTGRE_USER", "root")
        self.password = os.getenv("POSTGRE_PASSWORD", "1234")
        self.host = os.getenv("POSTGRE_HOST", "localhost")
        self.port = os.getenv("POSTGRE_PORT", "3306")
        self.db_name = os.getenv("POSTGRE_DB", "api_users_db")

        self.SQLALCHEMY_DATABASE_URL = (
            f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
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
        self.Base = declarative_base()

    def get_session(self):
        return self.SessionLocal()

