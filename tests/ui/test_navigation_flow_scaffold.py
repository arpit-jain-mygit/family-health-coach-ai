from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text()


def assert_file(path: str) -> None:
    assert (ROOT / path).is_file(), f"Missing file: {path}"


def test_mock_navigation_shell_files_exist() -> None:
    for path in [
        "apps/web/src/app/shared/components/app-shell/app-shell.component.ts",
        "apps/web/src/app/shared/components/app-shell/app-shell.component.html",
        "apps/web/src/app/shared/components/app-shell/app-shell.component.scss",
        "apps/web/src/app/shared/components/mock-feature-page/mock-feature-page.component.ts",
        "apps/web/src/app/shared/components/mock-feature-page/mock-feature-page.component.html",
        "apps/web/src/app/shared/components/mock-feature-page/mock-feature-page.component.scss",
        "apps/web/src/app/shared/components/mock-feature-page/mock-feature-page.model.ts",
    ]:
        assert_file(path)


def test_mock_navigation_routes_are_declared() -> None:
    routes = read("apps/web/src/app/app.routes.ts")
    for route in [
        "dashboard",
        "families/new",
        "families/:familyId/settings",
        "members",
        "members/:memberId",
        "chat",
        "food-logs",
        "meal-plans",
        "progress",
        "reports",
        "leaderboard",
        "reminders",
        "admin",
    ]:
        assert route in routes
    assert "AppShellComponent" in routes
    assert "MockFeaturePageComponent" in routes


def test_dashboard_and_shell_link_to_the_mock_flow() -> None:
    dashboard = read("apps/web/src/app/features/dashboard/dashboard.component.html")
    shell = read("apps/web/src/app/shared/components/app-shell/app-shell.component.html")
    routes = read("apps/web/src/app/app.routes.ts")
    shell_ts = read("apps/web/src/app/shared/components/app-shell/app-shell.component.ts")
    for token in [
        '/families/new',
        '/chat',
        '/members',
        '/reports',
        '/dashboard',
    ]:
        assert token in routes or token in shell_ts
    for token in ['routerLink="/families/new"', 'routerLink="/chat"']:
        assert token in dashboard
    assert "routerLinkActive=\"active\"" in shell
    assert "family-switcher" in shell
    assert "Logout" in shell


if __name__ == "__main__":
    test_mock_navigation_shell_files_exist()
    test_mock_navigation_routes_are_declared()
    test_dashboard_and_shell_link_to_the_mock_flow()
    print("Mock navigation flow scaffold checks passed.")
