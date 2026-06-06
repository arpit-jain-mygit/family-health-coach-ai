from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Family Health Coach AI API"
    app_version: str = "0.1.0"
    api_host: str = "127.0.0.1"
    api_port: int = 8000
    database_url: str = "postgresql+psycopg://family_health:family_health@localhost:5432/family_health"
    redis_url: str = "redis://localhost:6379/0"
    jwt_secret: str = "change-me-local-only"
    google_client_id: str = ""
    google_client_secret: str = ""
    frontend_app_url: str = "http://localhost:4200"
    s3_endpoint_url: str = "http://localhost:9000"
    s3_access_key_id: str = "family_health"
    s3_secret_access_key: str = "family_health_password"
    s3_bucket: str = "family-health-local"

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parents[2] / ".env"),
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
