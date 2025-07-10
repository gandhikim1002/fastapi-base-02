from sqlmodel import SQLModel, create_engine

### add model for create table
from app.src.domain.item import models

###
# Database Configuration
###

SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:example@host.docker.internal:5432/postgres"

engine = create_engine(str(SQLALCHEMY_DATABASE_URI))

def conn():
    SQLModel.metadata.create_all(engine)

'''
def get_session():
    with Session(engine) as session:
        yield session
'''
