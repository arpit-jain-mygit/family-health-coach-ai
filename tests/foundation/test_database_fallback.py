from pathlib import Path
import importlib
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "apps" / "api"))


def test_database_session_falls_back_to_sqlite_when_postgres_is_unavailable() -> None:
    session_module = importlib.import_module("app.db.session")
    assert session_module.engine.url.drivername == "sqlite"
    assert str(session_module.engine.url).endswith("family_health_local.db")


if __name__ == "__main__":
    test_database_session_falls_back_to_sqlite_when_postgres_is_unavailable()
    print("Database fallback checks passed.")
