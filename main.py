from fastapi import FastAPI
from models import User
from database import engine
from init_db import init_db
from routes import users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/usuarios", tags=["usuarios"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la tienda Techforall"}
