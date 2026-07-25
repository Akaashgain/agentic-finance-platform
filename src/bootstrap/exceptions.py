from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.core.exceptions import ApplicationException


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(ApplicationException)
    async def application_exception_handler(
        request: Request,
        exc: ApplicationException,
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": exc.message,
                "error": {
                    "code": exc.error_code,
                },
            },
        )