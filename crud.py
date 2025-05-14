from models import User
from sqlalchemy.orm import Session
from passlib.context import CryptContext

# hasheo de la contraseña y se guarda el usuario.

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, username: str, password: str, email: str):
    hashed_password = pwd_context.hash(password)
    user = User(username=username, password=hashed_password, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
