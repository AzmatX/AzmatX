from src.utils.config import settings


def vector_backend_info() -> dict[str, str]:
    return {"provider": settings.vector_db_provider, "status": "configured"}
