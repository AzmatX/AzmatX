from celery import Celery

from src.utils.config import settings

celery_app = Celery(
    "contract_intelligence",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
)


@celery_app.task(name="tasks.ping")
def ping() -> str:
    return "pong"
