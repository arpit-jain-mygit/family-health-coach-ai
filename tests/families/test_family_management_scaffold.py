from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text()


def assert_file(path: str) -> None:
    assert (ROOT / path).is_file(), f"Missing file: {path}"


def test_fastapi_family_files_exist() -> None:
    for path in [
        "apps/api/app/api/v1/families.py",
        "apps/api/app/services/family_service.py",
        "apps/api/app/schemas/family.py",
        "apps/api/app/models/family.py",
    ]:
        assert_file(path)


def test_fastapi_family_routes_are_declared() -> None:
    router = read("apps/api/app/api/v1/families.py")
    for route in [
        '@router.get("", response_model=list[FamilyResponse])',
        '@router.post("", response_model=FamilyResponse',
        '@router.get("/{family_id}", response_model=FamilyResponse)',
        '@router.patch("/{family_id}", response_model=FamilyResponse)',
        '@router.delete("/{family_id}"',
    ]:
        assert route in router
    assert "CurrentUserId" in router
    assert "DatabaseSession" in router


def test_family_service_membership_and_tenant_checks_exist() -> None:
    service = read("apps/api/app/services/family_service.py")
    assert "FAMILY_ADMIN" in service
    assert "create_family" in service
    assert "FamilyMembership" in service
    assert "role=FAMILY_ADMIN" in service
    assert "ensure_user_has_family_access" in service
    assert "HTTP_403_FORBIDDEN" in service
    assert "HTTP_409_CONFLICT" in service
    assert "User already belongs to a family." in service


def test_family_membership_is_single_family_per_user() -> None:
    family_model = read("apps/api/app/models/family.py")
    assert "UniqueConstraint" in family_model
    assert "uq_family_memberships_user_id" in family_model


def test_family_schemas_exist() -> None:
    schemas = read("apps/api/app/schemas/family.py")
    assert "class FamilyCreate" in schemas
    assert "class FamilyUpdate" in schemas
    assert "class FamilyResponse" in schemas
    assert "name: str" in schemas


def test_family_router_is_registered() -> None:
    main = read("apps/api/app/main.py")
    assert "families_router" in main
    assert "app.include_router(families_router, prefix=\"/api/v1\")" in main


def test_angular_family_files_exist() -> None:
    for path in [
        "apps/web/src/app/features/family/create-family/create-family.component.ts",
        "apps/web/src/app/features/family/create-family/create-family.component.html",
        "apps/web/src/app/features/family/family-settings/family-settings.component.ts",
        "apps/web/src/app/features/family/family-settings/family-settings.component.html",
        "apps/web/src/app/shared/components/family-switcher/family-switcher.component.ts",
        "apps/web/src/app/shared/components/family-switcher/family-switcher.component.html",
    ]:
        assert_file(path)


def test_angular_family_routes_and_api_methods_exist() -> None:
    routes = read("apps/web/src/app/app.routes.ts")
    api_service = read("apps/web/src/app/core/api/api.service.ts")
    create_component = read(
        "apps/web/src/app/features/family/create-family/create-family.component.ts"
    )
    assert "families/new" in routes
    assert "families/:familyId/settings" in routes
    for method in ["listFamilies", "createFamily", "getFamily", "updateFamily", "deleteFamily"]:
        assert method in api_service
    assert "ReactiveFormsModule" in create_component
    assert "createFamily" in create_component


if __name__ == "__main__":
    test_fastapi_family_files_exist()
    test_fastapi_family_routes_are_declared()
    test_family_service_membership_and_tenant_checks_exist()
    test_family_schemas_exist()
    test_family_router_is_registered()
    test_angular_family_files_exist()
    test_angular_family_routes_and_api_methods_exist()
    print("Module 3 family management scaffold checks passed.")
