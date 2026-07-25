from fastapi import APIRouter
from src.core.responses import success_response
from src.modules.health.service import HealthService
router = APIRouter(
    prefix="/api/v1",
    tags=["Health"],
)

health_service = HealthService()

@router.get(
    "/health",
    summary="Health Check",
)
async def health():
    database_status = await health_service.check_database()

    return success_response(
        data={
            "status": "healthy",
            "application": "Agentic Finance Platform",
            "version": "0.1.0",
            "database": database_status,
        }
    )