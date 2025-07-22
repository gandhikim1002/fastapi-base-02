from sqlmodel import SQLModel, create_engine
from app.src.config import SQLALCHEMY_DATABASE_URI


engine = create_engine(str(SQLALCHEMY_DATABASE_URI))


def conn():
    SQLModel.metadata.create_all(engine)
