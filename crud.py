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

# pasa el contexto de la contraseña y se verifica si la contraseña es correcta.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#verifica la contraseña hashada y la contraseña en texto plano.
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#verifica si el usuario existe y si la contraseña es correcta.
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
<<<<<<< HEAD
    # Si el usuario no existe o la contraseña es incorrecta, retorna None
    if not user or not verify_password(password, user.password):
        return None  # Solo retorna None si falla
    return user
=======
    if not user:
        return {"message": "Usuario no encontrado", "status": "error"}
    if not verify_password(password, user.password):
        return {"message": "Contraseña incorrecta", "status": "error"}
    return {
        "message": "Inicio de sesión exitoso",
        "status": "success",
    }
>>>>>>> bfba299a809000a3efe72eb66e33455555c6f807


