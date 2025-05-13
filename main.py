from fastapi import FastAPI
from models import User
from database import engine, Base

app = FastAPI()

# Crea las tablas
Base.metadata.create_all(bind=engine)
