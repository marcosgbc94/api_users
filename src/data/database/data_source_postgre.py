import os
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()  # Carga variables del .env

class DataSourcePostgre:
    def __init__(self):
        self.user = os.getenv("POSTGRE_USER")
        self.password = os.getenv("POSTGRE_PASSWORD")
        self.host = os.getenv("POSTGRE_HOST")
        self.port = os.getenv("POSTGRE_PORT")
        self.db_name = os.getenv("POSTGRE_DB")

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

