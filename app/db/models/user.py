from sqlalchemy import Column, String, BigInteger, Boolean, JSON
from sqlalchemy.orm import relationship
from app.db.session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    fullname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    user_details = Column(JSON, nullable=True)
    user_settings = Column(JSON, nullable=True)
    closed = Column(Boolean, nullable=True)

    messages = relationship("Message", back_populates="user")
    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")
