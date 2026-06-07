from fastapi import FastAPI

from src.utils.config import settings

app = FastAPI(title=settings.project_name)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok", "environment": settings.environment}


@app.get("/")
def root() -> dict[str, str]:
    return {"message": settings.project_name}
