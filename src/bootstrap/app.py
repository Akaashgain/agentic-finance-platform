from fastapi import FastAPI

from src.bootstrap.lifespan import lifespan
from src.bootstrap.router import register_routes
from src.core.config import get_settings
from src.core.logging import configure_logging


def create_application() -> FastAPI:
    settings = get_settings()
    configure_logging(settings.log_level)
    app = FastAPI(title=settings.app_name, version=settings.app_version, lifespan=lifespan)
    register_routes(app)
    return app