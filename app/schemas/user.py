from pydantic import BaseModel


class User(BaseModel):
    username: str
    fullname: str
    email: str
    password: str
    disabled: bool
    closed: bool
