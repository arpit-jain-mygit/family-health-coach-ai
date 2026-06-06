from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings

settings = get_settings()


def _build_engine():
    if settings.database_url.startswith("postgresql"):
        primary_engine = create_engine(
            settings.database_url,
            pool_pre_ping=True,
            connect_args={"connect_timeout": 3},
        )
        try:
            with primary_engine.connect():
                pass
            return primary_engine
        except SQLAlchemyError:
            fallback_path = Path(__file__).resolve().parents[2] / "family_health_local.db"
            return create_engine(
                f"sqlite:///{fallback_path}",
                connect_args={"check_same_thread": False},
            )
    return create_engine(settings.database_url, pool_pre_ping=True)


engine = _build_engine()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
