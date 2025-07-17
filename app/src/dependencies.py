import jwt
from fastapi import Header, HTTPException

from sqlmodel import Session
from app.src.database import engine

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


def decode(token):
    striped_token = token.replace("Bearer ", "")
    return jwt.decode(striped_token, SECRET_KEY, algorithms=[ALGORITHM])

def encode():
    return jwt.encode({"email": "payload"}, SECRET_KEY, algorithm=ALGORITHM)

def get_db():
    with Session(engine) as session:
        yield session

def get_db2():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

async def get_token_header(x_token: str = Header(...)):
    payload = decode(x_token)
    username: str = payload.get("email")
    if username == None:
        raise HTTPException(status_code=403, detail="Unauthorized")

async def get_query_token(token: str):
    ''' Exemplo of header validation dependency '''
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
