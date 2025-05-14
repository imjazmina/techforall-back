from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import UserCreate, UserOut
from crud import get_user_by_username, create_user

router = APIRouter()

@router.post("/registro", response_model=UserOut)
def registrar_usuario(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Nombre de usuario ya registrado")
    nuevo_usuario = create_user(db, user.username, user.password, user.email)
    return nuevo_usuario
