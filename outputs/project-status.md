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
| Code implementation | Planned | No application code has been scaffolded yet; build locally first. |
| GitHub sync | Done | Repository is connected and pushed to GitHub. |
| Deployment | Deferred | Develop locally now; migrate to Vercel/Render or similar after the MVP is stable. |

## Module Status

| Module | Phase | Status | Current Notes |
|---|---|---|---|
| 1. Foundation | Phase 1 | Planned | Angular + Bootstrap frontend and FastAPI backend are selected. |
| 2. Authentication | Phase 1 | Planned | Google OAuth only, with FastAPI JWT session tokens. |
| 3. Family Management | Phase 1 | Planned | Family is the tenant boundary. |
| 4. Member Management | Phase 1 | Planned | Supports profile, health info, goals, and preferences. |
| 5. AI Provider Layer | Phase 1 | Planned | Provider abstraction covers OpenAI, Gemini, and Anthropic. |
| 6. Memory System | Phase 1/2 | Planned | Basic memory first, `pgvector` RAG later. |
| 7. Chat | Phase 1 | Planned | WhatsApp-style Angular UI with persisted conversation history. |
| 8. Food Logging | Phase 2 | Planned | Manual and natural-language logging first. |
| 9. Meal Planning | Phase 2 | Planned | Personalized vegetarian/Jain/vegan meal plans. |
| 10. Daily Dashboard | Phase 2 | Planned | Daily calories, protein, water, exercise, steps, trends, and scores. |
| 11. Progress Tracking | Phase 2 | Planned | Health marker trends and goal progress. |
| 12. Reports and PDF Generation | Phase 3 | Planned | Daily, weekly, monthly, family reports, and PDFs. |
| 13. Family Leaderboard | Phase 3 | Planned | Adherence, improvement, activity, and consistency rankings. |
| 14. Reminders | Phase 3/4 | Planned | Meal, water, walking, and medication reminders. |
| 15. Photo and Voice Logging | Phase 4 | Planned | Photo upload, voice input, transcription, and multimodal meal review. |
| 16. Security, Audit, and Compliance | Cross-cutting | Planned | Tenant dependencies, audit logs, rate limits, and privacy controls. |
| 17. Testing and CI/CD | Cross-cutting | Planned | Angular tests, pytest, Alembic checks, E2E, and GitHub Actions. |

## Next Recommended Work

1. Scaffold the monorepo.
2. Create the Angular app with Bootstrap and PWA support.
3. Create the FastAPI app with health check, config, logging, Pydantic schemas, SQLAlchemy/SQLModel, and Alembic.
4. Add local Docker Compose setup for PostgreSQL, Redis, and optional local S3-compatible storage.
5. Add local `.env` templates for web and API.
6. Implement Google OAuth and JWT session handling locally.

## Sync Checklist

Before each commit:

- Update `family-health-coach-ai-blueprint.md` for architecture, API, database, stack, or phase changes.
- Update `module-wise-development-plan.md` for module scope, tasks, dependencies, or status changes.
- Update this file for current decisions and module status changes.
- Commit and push the documentation changes with the implementation changes.
