# modelo de usuario
# Importar las librerías necesarias
# Importar la base de datos
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database import Base 

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)