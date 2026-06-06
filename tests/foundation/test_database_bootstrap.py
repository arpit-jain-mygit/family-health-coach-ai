from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "apps" / "api"))

from sqlalchemy import create_engine, inspect

from app.db import init as db_init


def test_initialize_database_creates_foundation_tables() -> None:
    original_engine = db_init.engine
    try:
        db_init.engine = create_engine("sqlite:///:memory:")
        db_init.initialize_database()

        inspector = inspect(db_init.engine)
        assert "users" in inspector.get_table_names()
        assert "families" in inspector.get_table_names()
        assert "family_memberships" in inspector.get_table_names()
        assert "family_members" in inspector.get_table_names()
    finally:
        db_init.engine = original_engine


if __name__ == "__main__":
    test_initialize_database_creates_foundation_tables()
    print("Database bootstrap checks passed.")
