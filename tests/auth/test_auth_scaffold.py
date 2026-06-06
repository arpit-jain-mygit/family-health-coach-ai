from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text()


def assert_file(path: str) -> None:
    assert (ROOT / path).is_file(), f"Missing file: {path}"


def test_fastapi_auth_files_exist() -> None:
    for path in [
        "apps/api/app/api/v1/auth.py",
        "apps/api/app/services/auth_service.py",
        "apps/api/app/schemas/auth.py",
        "apps/api/app/core/security.py",
        "apps/api/app/api/deps.py",
    ]:
        assert_file(path)


def test_fastapi_auth_routes_are_declared() -> None:
    auth_router = read("apps/api/app/api/v1/auth.py")
    for route in [
        '@router.get("/google")',
        '@router.get("/google/callback"',
        '@router.get("/me"',
        '@router.post("/logout"',
    ]:
        assert route in auth_router
    assert "RedirectResponse" in auth_router
    assert "TokenResponse" in auth_router
    assert "CurrentUserResponse" in auth_router


def test_auth_service_and_jwt_helpers_exist() -> None:
    service = read("apps/api/app/services/auth_service.py")
    security = read("apps/api/app/core/security.py")
    deps = read("apps/api/app/api/deps.py")
    assert "google_authorization_url" in service
    assert "complete_google_callback" in service
    assert "accounts.google.com" in service
    assert "create_access_token" in security
    assert "decode_access_token" in security
    assert "HTTPBearer" in deps
    assert "decode_access_token" in deps


def test_auth_router_is_registered() -> None:
    main = read("apps/api/app/main.py")
    assert "auth_router" in main
    assert "app.include_router(auth_router, prefix=\"/api/v1\")" in main


def test_angular_auth_callback_exists() -> None:
    for path in [
        "apps/web/src/app/features/auth/callback/auth-callback.component.ts",
        "apps/web/src/app/features/auth/callback/auth-callback.component.html",
        "apps/web/src/app/features/auth/callback/auth-callback.component.scss",
    ]:
        assert_file(path)
    routes = read("apps/web/src/app/app.routes.ts")
    callback = read("apps/web/src/app/features/auth/callback/auth-callback.component.ts")
    assert "auth/callback" in routes
    assert "AuthCallbackComponent" in routes
    assert "storeToken" in callback
    assert "navigateByUrl('/')" in callback
    assert "navigateByUrl('/login')" in callback


def test_angular_auth_guard_interceptor_and_service_are_wired() -> None:
    auth_service = read("apps/web/src/app/core/services/auth.service.ts")
    guard = read("apps/web/src/app/core/guards/auth.guard.ts")
    interceptor = read("apps/web/src/app/core/interceptors/auth.interceptor.ts")
    app_config = read("apps/web/src/app/app.config.ts")
    assert "loginWithGoogle" in auth_service
    assert "storeToken" in auth_service
    assert "isAuthenticated" in auth_service
    assert "authGuard" in guard
    assert "family_health_token" in interceptor
    assert "Authorization" in interceptor
    assert "withInterceptors([authInterceptor])" in app_config


if __name__ == "__main__":
    test_fastapi_auth_files_exist()
    test_fastapi_auth_routes_are_declared()
    test_auth_service_and_jwt_helpers_exist()
    test_auth_router_is_registered()
    test_angular_auth_callback_exists()
    test_angular_auth_guard_interceptor_and_service_are_wired()
    print("Module 2 authentication scaffold checks passed.")
