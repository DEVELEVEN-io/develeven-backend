from sqlalchemy import Column, BigInteger, Text, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.session import Base


class Comment(Base):
    __tablename__ = "comment"

    id = Column(BigInteger, primary_key=True, index=True)
    post_id = Column(BigInteger, ForeignKey("post.id"), nullable=False)
    user_id = Column(BigInteger, ForeignKey("user.id"), nullable=False)
    content = Column(Text, nullable=False)
    created = Column(TIMESTAMP, nullable=False)
    deleted = Column(Boolean, nullable=True)

    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
