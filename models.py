from sqlalchemy import Column, Integer, String, ForeignKey, boolean
from database import db 

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    is_active = Column(boolean, default=True)
    is_admin = Column(boolean, default=False)