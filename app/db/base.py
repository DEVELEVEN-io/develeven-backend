from .session import Base, engine
from app.db.models import (
    user,
    message,
    comment,
    post,
)  # Import models to ensure they are registered


def init_db():
    Base.metadata.create_all(bind=engine)
