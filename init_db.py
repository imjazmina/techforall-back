from sqlalchemy.orm import Session
from models import User, Base 
from database import engine
from utils import get_password_hash

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

def init_db():
    session = Session(bind=engine)
    try:
        # Verificar si ya existe un usuario admin
        admin_email = "admin@admin.com"
        existing_admin = session.query(User).filter(User.email == admin_email).first()

        if not existing_admin:
            hashed_password = get_password_hash("admin1234")
            new_admin = User(
                email=admin_email,
                password=hashed_password,
                username="admin",
                is_admin=True,
                is_active=True
            )
            session.add(new_admin)
            session.commit()
            print("Usuario admin creado correctamente.")# enviar mensaje de exito al front
        else:
            print("El usuario admin ya existe.")# si el usuario ya existe, no deberia hacer nada
    finally:
        session.close()# porque cierrar la sesion al final, aunque haya un error

if __name__ == "__main__":
    init_db()
