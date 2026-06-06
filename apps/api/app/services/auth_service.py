from urllib.parse import urlencode

from app.core.config import get_settings
from app.core.security import create_access_token


class AuthService:
    def google_authorization_url(self) -> str:
        settings = get_settings()
        query = urlencode(
            {
                "client_id": settings.google_client_id,
                "redirect_uri": "http://localhost:8000/api/v1/auth/google/callback",
                "response_type": "code",
                "scope": "openid email profile",
                "access_type": "offline",
                "prompt": "consent",
            }
        )
        return f"https://accounts.google.com/o/oauth2/v2/auth?{query}"

    def complete_google_callback(self, code: str) -> str:
        # Module 2 keeps this local-first. Token exchange and user persistence are
        # wired here later when Google credentials are available.
        local_subject = f"google:{code}"
        return create_access_token(local_subject)
