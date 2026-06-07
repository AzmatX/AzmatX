from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "AI-Powered Contract Intelligence & Risk Scoring"
    api_prefix: str = "/api/v1"
    environment: str = "development"

    celery_broker_url: str = "redis://redis:6379/0"
    celery_result_backend: str = "redis://redis:6379/1"

    vector_db_provider: str = "milvus"
    milvus_host: str = "milvus"
    milvus_port: int = 19530
    pinecone_api_key: str = ""
    pinecone_index_name: str = "contracts"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
