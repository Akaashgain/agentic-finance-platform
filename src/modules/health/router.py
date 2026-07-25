from fastapi import APIRouter
from src.core.responses import success_response
router = APIRouter(
    prefix="/api/v1",
    tags=["Health"],
)

@router.get(
    "/health",
    summary="Health Check",
)
async def health():
    return {
        "status": "healthy",
        "application": "Agentic Finance Platform",
        "version": "0.1.0",
    }