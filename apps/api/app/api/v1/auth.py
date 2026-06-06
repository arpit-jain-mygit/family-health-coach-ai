from fastapi import APIRouter, Depends, Query
from fastapi.responses import RedirectResponse

from app.api.deps import CurrentUserId
from app.schemas.auth import CurrentUserResponse, LogoutResponse, TokenResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


def get_auth_service() -> AuthService:
    return AuthService()


@router.get("/google")
def start_google_login(
    auth_service: AuthService = Depends(get_auth_service),
) -> RedirectResponse:
    return RedirectResponse(auth_service.google_authorization_url())


@router.get("/google/callback", response_model=TokenResponse)
def complete_google_login(
    code: str = Query(...),
    auth_service: AuthService = Depends(get_auth_service),
) -> TokenResponse:
    return TokenResponse(access_token=auth_service.complete_google_callback(code))


@router.get("/me", response_model=CurrentUserResponse)
def get_me(current_user_id: CurrentUserId) -> CurrentUserResponse:
    return CurrentUserResponse(user_id=current_user_id)


@router.post("/logout", response_model=LogoutResponse)
def logout() -> LogoutResponse:
    return LogoutResponse(status="ok")
