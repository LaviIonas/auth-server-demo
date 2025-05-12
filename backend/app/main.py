from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api import users


app = FastAPI()

app.include_router(users.router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Auth server is alive"}