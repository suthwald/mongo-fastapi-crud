from fastapi import FastAPI
from app.routes.item_routes import router as item_router
from app.logging_config import setup_logging

setup_logging()

app = FastAPI(
    title="My FastAPI Application",
    description="A sample FastAPI application with MongoDB, Pydantic, and more.",
    version="1.0.0"
)

app.include_router(item_router, prefix="/api/v1")