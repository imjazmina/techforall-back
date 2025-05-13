from fastapi import FastAPI
from models import User
from database import engine, db
from init_db import init_db

app = FastAPI()


init_db()


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la tienda Techno Solidario"}