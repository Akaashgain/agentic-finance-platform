from typing import Any
from fastapi.responses import JSONResponse

def success_response(
    data: Any = None,
    message: str = "Success",
):
    return JSONResponse(
        content={
            "success": True,
            "message": message,
            "data": data,
        }
    )