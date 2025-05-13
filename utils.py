from passlib.context import CryptContext

# Crear contexto de password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#obtener el hash de la contraseña
def get_password_hash(password: str) -> str:

    return pwd_context.hash(password)

#Verifica si una contraseña proporcionada coincide con el hash almacenado.
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
