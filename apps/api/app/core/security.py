from datetime import datetime, timedelta, timezone

from jose import jwt

from app.core.config import get_settings


def create_access_token(subject: str, expires_minutes: int = 60) -> str:
    settings = get_settings()
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    payload = {"sub": subject, "exp": expires_at}
    return jwt.encode(payload, settings.jwt_secret, algorithm="HS256")
