from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text()


def assert_file(path: str) -> None:
    assert (ROOT / path).is_file(), f"Missing file: {path}"


def assert_dir(path: str) -> None:
    assert (ROOT / path).is_dir(), f"Missing directory: {path}"


def test_fastapi_foundation_files() -> None:
    for path in [
        "apps/api/pyproject.toml",
        "apps/api/app/main.py",
        "apps/api/app/core/config.py",
        "apps/api/app/api/v1/health.py",
        "apps/api/app/db/base.py",
        "apps/api/app/db/session.py",
        "apps/api/app/db/init.py",
        "apps/api/alembic.ini",
        "apps/api/alembic/env.py",
    ]:
        assert_file(path)

    pyproject = read("apps/api/pyproject.toml")
    for dependency in ["fastapi", "sqlalchemy", "alembic", "pydantic-settings", "uvicorn"]:
        assert dependency in pyproject
    assert "setuptools.build_meta" in pyproject


def test_health_route_is_declared() -> None:
    main = read("apps/api/app/main.py")
    health = read("apps/api/app/api/v1/health.py")
    assert "FastAPI" in main
    assert 'prefix="/api/v1"' in main
    assert '@router.get("/health")' in health
    assert '{"status": "ok"}' in health


def test_database_foundation_models_exist() -> None:
    for path in [
        "apps/api/app/models/user.py",
        "apps/api/app/models/family.py",
        "apps/api/app/models/member.py",
    ]:
        assert_file(path)

    assert "class User" in read("apps/api/app/models/user.py")
    assert "class Family" in read("apps/api/app/models/family.py")
    assert "class FamilyMembership" in read("apps/api/app/models/family.py")
    assert "class FamilyMember" in read("apps/api/app/models/member.py")


def test_angular_foundation_files() -> None:
    for path in [
        "apps/web/package.json",
        "apps/web/angular.json",
        "apps/web/tsconfig.json",
        "apps/web/src/main.ts",
        "apps/web/src/app/app.config.ts",
        "apps/web/src/app/app.routes.ts",
        "apps/web/src/styles/styles.scss",
        "apps/web/src/environments/environment.ts",
        "apps/web/src/manifest.webmanifest",
        "apps/web/vercel.json",
    ]:
        assert_file(path)

    package_json = read("apps/web/package.json")
    for dependency in ["@angular/core", "@angular/router", "@angular/forms", "bootstrap"]:
        assert dependency in package_json


def test_angular_core_structure_exists() -> None:
    for path in [
        "apps/web/src/app/core/api",
        "apps/web/src/app/core/auth",
        "apps/web/src/app/core/guards",
        "apps/web/src/app/core/interceptors",
        "apps/web/src/app/core/services",
        "apps/web/src/app/shared/components",
        "apps/web/src/app/features/auth/login",
        "apps/web/src/app/features/dashboard",
    ]:
        assert_dir(path)

    assert "authGuard" in read("apps/web/src/app/core/guards/auth.guard.ts")
    assert "authInterceptor" in read("apps/web/src/app/core/interceptors/auth.interceptor.ts")
    assert "apiBaseUrl" in read("apps/web/src/environments/environment.ts")
    assert "http://127.0.0.1:8000" in read("apps/web/src/environments/environment.ts")


def test_local_development_configuration() -> None:
    assert_file("docker-compose.yml")
    assert_file(".env.example")
    assert_file("apps/api/.env.example")

    compose = read("docker-compose.yml")
    for service in ["postgres", "redis", "minio"]:
        assert service in compose

    env_example = read(".env.example")
    for key in ["DATABASE_URL", "REDIS_URL", "JWT_SECRET", "GOOGLE_CLIENT_ID"]:
        assert key in env_example

    api_config = read("apps/api/app/core/config.py")
    assert 'Path(__file__).resolve().parents[2] / ".env"' in api_config
    main = read("apps/api/app/main.py")
    assert "CORSMiddleware" in main
    assert "allow_origins" in main
    assert "initialize_database" in main


if __name__ == "__main__":
    test_fastapi_foundation_files()
    test_health_route_is_declared()
    test_database_foundation_models_exist()
    test_angular_foundation_files()
    test_angular_core_structure_exists()
    test_local_development_configuration()
    print("Module 1 foundation scaffold checks passed.")
