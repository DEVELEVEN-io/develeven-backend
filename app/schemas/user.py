from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


class UserCreate(BaseModel):
    username: str
    fullname: str
    email: str
    password: str
    user_details: Optional[dict] = None
    user_settings: Optional[dict] = None

    @field_validator("username", "fullname", "password")
    def not_empty(cls, value):
        if not value.strip():
            raise ValueError("must not be empty")
        return value

    @field_validator("email")
    def email_not_empty(cls, value):
        if not value.strip():
            raise ValueError("must not be empty")
        return value
