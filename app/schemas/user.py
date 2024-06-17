from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


class UserCreate(BaseModel):
    username: str
    fullname: str
    email: str
    password: str
    user_details: Optional[dict] = None
    user_settings: Optional[dict] = None
