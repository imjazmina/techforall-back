from pydantic import BaseModel

#define qué datos se esperan al registrar un usuario.
class UserCreate(BaseModel):
    username: str
    password: str
    email: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    is_admin: bool
    is_active: bool

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str
