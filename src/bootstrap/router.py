from fastapi import FastAPI

from src.presentation.api.router import router as api_router


def register_routes(app: FastAPI) -> None:
    app.include_router(api_router)