from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
from app.api.api_v1.api import api_router
from app.db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando la aplicación y la base de datos...")
    init_db()
    yield
    print("Apagando la aplicación...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Prueba Técnica"}
