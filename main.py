from fastapi import FastAPI
from models import User
from database import engine
from init_db import init_db
from routes import users

app = FastAPI()

app.include_router(users.router, prefix="/usuarios", tags=["usuarios"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la tienda Techno Solidario"}
