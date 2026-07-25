import logging
from fastapi import FastAPI, Request
from src.bootstrap.container import ApplicationContainer
from src.bootstrap.lifespan import lifespan
from src.bootstrap.router import register_routes
from src.core.config import get_settings
from src.core.exceptions import ApplicationException
from src.core.logging import setup_logging
from src.core.middleware import register_middlewares
from src.core.responses import error_response


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    # Load application settings
    settings = get_settings()

    # Configure logging
    setup_logging(settings.LOG_LEVEL)

    # Initialize Dependency Injection Container
    container = ApplicationContainer()

    # Create FastAPI application
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="Enterprise Agentic Financial Intelligence Platform",
        lifespan=lifespan,
    )

    # Attach DI container to application
    app.container = container

    # Register middlewares
    register_middlewares(app)

    # Register exception handlers
    @app.exception_handler(ApplicationException)
    async def application_exception_handler(
        request: Request,
        exc: ApplicationException,
    ):
        return error_response(
            message=exc.message,
            status_code=exc.status_code,
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(
        request: Request,
        exc: Exception,
    ):
        logger = logging.getLogger(__name__)
        logger.exception("Unhandled exception occurred", exc_info=exc)

        return error_response(
            message="Internal Server Error",
            status_code=500,
        )

    # Register all API routes
    register_routes(app)

    return app