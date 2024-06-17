from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate
import bcrypt


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username,
        fullname=user.fullname,
        email=user.email,
        password=hashed_password,
        user_details=user.user_details,
        user_settings=user.user_settings,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")
