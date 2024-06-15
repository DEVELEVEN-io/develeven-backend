from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import users
from app.db.base import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(users.router, prefix="/api/v1")


@app.get("/")
async def read_root():
    return {"Message": "Welcome to DevEleven API!"}
