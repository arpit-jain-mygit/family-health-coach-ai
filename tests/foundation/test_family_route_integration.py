from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "apps" / "api"))

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api import deps
from app.core.security import create_access_token
from app.db import init as db_init
from app.db import session as db_session
from app.main import app
from app.models import Family, FamilyMembership, User


def test_family_list_returns_cors_headers() -> None:
    original_init_engine = db_init.engine
    original_session_engine = db_session.engine
    original_session_local = deps.SessionLocal
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as temp_db:
        db_path = Path(temp_db.name)
    test_engine = create_engine(f"sqlite:///{db_path}")
    test_session_local = sessionmaker(bind=test_engine, autoflush=False, autocommit=False)
    try:
        db_init.engine = test_engine
        db_session.engine = test_engine
        deps.SessionLocal = test_session_local
        db_init.initialize_database()

        db = test_session_local()
        user = User(id="user-1", email="family@example.com", google_id="google-1")
        family = Family(id="family-1", name="The Family", goals=None, preferences=None)
        membership = FamilyMembership(
            id="membership-1",
            family_id="family-1",
            user_id="user-1",
            role="FAMILY_ADMIN",
        )
        db.add_all([user, family, membership])
        db.commit()
        db.close()

        token = create_access_token("user-1")
        with TestClient(app) as client:
            response = client.get(
                "/api/v1/families",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Origin": "http://localhost:4200",
                },
            )

        assert response.status_code == 200
        assert response.headers["access-control-allow-origin"] == "http://localhost:4200"
        assert response.json()[0]["name"] == "The Family"
    finally:
        db_init.engine = original_init_engine
        db_session.engine = original_session_engine
        deps.SessionLocal = original_session_local
        if db_path.exists():
            db_path.unlink()


if __name__ == "__main__":
    test_family_list_returns_cors_headers()
    print("Family route integration checks passed.")
