from urllib.parse import urlencode

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import RedirectResponse

from app.api.deps import CurrentUserId
from app.core.config import get_settings
from app.schemas.auth import CurrentUserResponse, LogoutResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


def get_auth_service() -> AuthService:
    return AuthService()


@router.get("/google")
def start_google_login(
    auth_service: AuthService = Depends(get_auth_service),
) -> RedirectResponse:
    settings = get_settings()
    if not settings.google_client_id.strip() or not settings.google_client_secret.strip():
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                "Google OAuth is not configured locally. Set GOOGLE_CLIENT_ID "
                "and GOOGLE_CLIENT_SECRET in apps/api/.env, then restart FastAPI. "
                "Authorized redirect URI: "
                f"{settings.google_redirect_uri}"
            ),
        )

    return RedirectResponse(auth_service.google_authorization_url())


@router.get("/google/callback")
def complete_google_login(
    code: str = Query(...),
    auth_service: AuthService = Depends(get_auth_service),
) -> RedirectResponse:
    token = auth_service.complete_google_callback(code)
    settings = get_settings()
    callback_url = f"{settings.frontend_app_url}/auth/callback?{urlencode({'token': token})}"
    return RedirectResponse(callback_url)


@router.get("/me", response_model=CurrentUserResponse)
def get_me(current_user_id: CurrentUserId) -> CurrentUserResponse:
    return CurrentUserResponse(user_id=current_user_id)


@router.post("/logout", response_model=LogoutResponse)
def logout() -> LogoutResponse:
    return LogoutResponse(status="ok")
