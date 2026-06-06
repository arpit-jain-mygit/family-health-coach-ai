# Family Health Coach AI - Project Status

Last updated: 2026-06-06

## Current Decisions

| Area | Decision |
|---|---|
| Frontend | Angular, TypeScript, Bootstrap CSS, Angular PWA |
| Backend | FastAPI, Python |
| Database | PostgreSQL |
| ORM | SQLAlchemy or SQLModel |
| Migrations | Alembic |
| Auth | Google OAuth only, with JWT session tokens |
| Food Preferences | `VEGETARIAN`, `JAIN`, `VEGAN` only |
| AI Providers | OpenAI, Gemini, Anthropic behind a provider abstraction |
| Memory | PostgreSQL first, `pgvector` for RAG when needed |
| Queue | Celery or RQ with Redis |
| Storage | Local filesystem or S3-compatible local storage first; AWS S3-compatible storage later |
| Environment Strategy | Local-first development; move to Vercel/Render-style hosting later |
| Docs Policy | Keep architecture, module plan, and status docs in sync after every change |

## Overall Status

| Workstream | Status | Notes |
|---|---|---|
| Product blueprint | Done | Architecture, data model, API contracts, UI wireframes, and implementation phases are documented. |
| Module-wise plan | Done | Modules, tasks, dependencies, tests, and status tracker are documented. |
| Code implementation | In Progress | Module 3 Family Management is certified; Module 4 Member Management is next. |
| GitHub sync | Done | Repository is connected and pushed to GitHub. |
| Deployment | Deferred | Develop locally now; migrate to Vercel/Render or similar after the MVP is stable. |
| Local UI Preview | Available | Open `outputs/ui-preview/index.html` directly in a browser to inspect the current scaffold screens without installing Angular dependencies. |
| Local API Server | Available | Run `cd apps/api && ../../.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload`; `/api/v1/health` and `/api/v1/auth/google` are verified. Google OAuth requires `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`; when configured it forces account selection with `prompt=select_account consent`. |

## Module Status

| Module | Phase | Status | Certification | Current Notes |
|---|---|---|---|---|
| 1. Foundation | Phase 1 | Certified | Certified | Foundation scaffold implemented; `python3 tests/foundation/test_foundation_scaffold.py` passed. |
| 2. Authentication | Phase 1 | Certified | Certified | Authentication scaffold implemented; `python3 tests/auth/test_auth_scaffold.py` passed. |
| 3. Family Management | Phase 1 | Certified | Certified | Family management scaffold implemented; `python3 tests/families/test_family_management_scaffold.py` passed. |
| 4. Member Management | Phase 1 | Planned | Not certified | Supports profile, health info, goals, and preferences. |
| 5. AI Provider Layer | Phase 1 | Planned | Not certified | Provider abstraction covers OpenAI, Gemini, and Anthropic. |
| 6. Memory System | Phase 1/2 | Planned | Not certified | Basic memory first, `pgvector` RAG later. |
| 7. Chat | Phase 1 | Planned | Not certified | WhatsApp-style Angular UI with persisted conversation history. |
| 8. Food Logging | Phase 2 | Planned | Not certified | Manual and natural-language logging first. |
| 9. Meal Planning | Phase 2 | Planned | Not certified | Personalized vegetarian/Jain/vegan meal plans. |
| 10. Daily Dashboard | Phase 2 | Planned | Not certified | Daily calories, protein, water, exercise, steps, trends, and scores. |
| 11. Progress Tracking | Phase 2 | Planned | Not certified | Health marker trends and goal progress. |
| 12. Reports and PDF Generation | Phase 3 | Planned | Not certified | Daily, weekly, monthly, family reports, and PDFs. |
| 13. Family Leaderboard | Phase 3 | Planned | Not certified | Adherence, improvement, activity, and consistency rankings. |
| 14. Reminders | Phase 3/4 | Planned | Not certified | Meal, water, walking, and medication reminders. |
| 15. Photo and Voice Logging | Phase 4 | Planned | Not certified | Photo upload, voice input, transcription, and multimodal meal review. |
| 16. Security, Audit, and Compliance | Cross-cutting | Planned | Not certified | Tenant dependencies, audit logs, rate limits, and privacy controls. |
| 17. Testing and CI/CD | Cross-cutting | Planned | Not certified | Angular tests, pytest, Alembic checks, E2E, and GitHub Actions. |

## Module Certification Policy

Before starting any module:

- Add or update that module's test cases in `module-wise-development-plan.md`.
- Mark the module `In Progress` in both status tables.

After implementing a module:

- Run the documented module test cases.
- Fix failures before marking the module complete.
- Mark the module `Certified` only after tests pass.
- Add the test command, result, date, and commit SHA to the certification log.
- Commit and push the implementation and documentation updates.

## Next Recommended Work

1. Define Module 4 Member Management test cases before implementation.
2. Implement member service, router, profile schemas, and family tenant checks.
3. Add Angular member list, add member, edit member, and profile shells.
4. Run Module 4 member management tests.
5. Update module status and certification log after tests pass.

## Sync Checklist

Before each commit:

- Update `family-health-coach-ai-blueprint.md` for architecture, API, database, stack, or phase changes.
- Update `module-wise-development-plan.md` for module scope, tasks, dependencies, or status changes.
- Update this file for current decisions and module status changes.
- Before starting a module, document its test cases.
- After finishing a module, run its test cases and update certification status.
- Run the stale-stack scan and fix any outdated stack references before committing:
  `rg -n "N[e]xt\\.js|N[e]xtJS|n[e]xt\\.js|n[e]xtjs|T[a]ilwind|t[a]ilwind|s[h]adcn|A[u]th\\.js|N[e]stJS|P[r]isma|s[c]hema\\.prisma|R[e]act PDF|B[u]llMQ" . -g "!package-lock.json" -g "!node_modules/**"`
- Commit and push the documentation changes with the implementation changes.
