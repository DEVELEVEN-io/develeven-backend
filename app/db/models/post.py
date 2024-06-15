from sqlalchemy import Column, BigInteger, Text, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.session import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("user.id"), nullable=False)
    content = Column(Text, nullable=False)
    created = Column(TIMESTAMP, nullable=False)
    deleted = Column(Boolean, nullable=True)

    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
