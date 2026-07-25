from fastapi import FastAPI

from src.modules.health.router import router as health_router


def register_routes(app: FastAPI) -> None:
    """
    Register application routes.
    """

    app.include_router(health_router)