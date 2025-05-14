from sqlalchemy.orm import Session
from models import User, db
from database import engine
from utils import get_password_hash

# Crear la tabla en la base de datos si no existen
db.metadata.create_all(bind=engine)

# Función para agregar el usuario admin por defecto
def init_db():
    db = Session(bind=engine)
    try:
        # Verificar si ya existe un usuario admin
        user_admin = db.query(User).filter(User.email == "admin@admin.com").first()
        
        if not user_admin:
            # Crear el usuario admin si no existe
            hashed_password = get_password_hash("admin1234")  # Contraseña predeterminada
            new_user = User(
                email="admin@admin.com",
                password=hashed_password,
                full_name="Administrador",
                is_admin=True
            )
            db.add(new_user)
            db.commit()
            print("Usuario admin creado.")
        else:
            print("El usuario admin ya existe.")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
