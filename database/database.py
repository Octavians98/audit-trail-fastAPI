from sqlmodel import SQLModel, create_engine
from config import settings

postgresql_url = settings.DATABASE_URL

engine = create_engine(postgresql_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
