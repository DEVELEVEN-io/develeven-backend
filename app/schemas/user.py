from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    fullname: str
    email: str
    password: str
