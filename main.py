from fastapi import FastAPI
from models import User
from database import engine, db

app = FastAPI()

# Crea las tablas
db.metadata.create_all(bind=engine)
