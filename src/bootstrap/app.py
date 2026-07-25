from fastapi import FastAPI

from src.bootstrap.lifespan import lifespan
from src.bootstrap.router import register_routes
from src.core.config import get_settings


def create_application() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        lifespan=lifespan,
    )

    register_routes(app)

    return app