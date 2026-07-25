from sqlalchemy import text
from src.infrastructure.database import AsyncSessionLocal


class HealthService:
    async def check_database(self) -> bool:
        async with AsyncSessionLocal() as session:
            await session.execute(text("SELECT 1"))
            return True