# Family Health Coach AI - Module-Wise Development Plan

## Development Sequence

Recommended order:

1. Foundation
2. Authentication
3. Family Management
4. Member Management
5. AI Provider Layer
6. Chat
7. Food Logging
8. Meal Planning
9. Dashboard
10. Progress Tracking
11. Reports and PDFs
12. Leaderboard
13. Reminders
14. Photo and Voice Logging
15. Security, Audit, and Compliance
16. Testing and CI/CD

## Module Status Tracker

Status legend:

- `Planned`: Defined in docs, not started in code.
- `In Progress`: Implementation started.
- `Blocked`: Waiting on a decision, dependency, or access.
- `Certified`: Test cases written, implementation completed, respective tests passed, docs updated, committed, and pushed.

Current status as of 2026-06-06:

| Module | Phase | Status | Certification | Current Notes |
|---|---|---|---|---|
| 1. Foundation | Phase 1 | Planned | Not certified | Angular + Bootstrap frontend and FastAPI backend are selected. |
| 2. Authentication | Phase 1 | Planned | Not certified | Google OAuth only, with FastAPI JWT session tokens. |
| 3. Family Management | Phase 1 | Planned | Not certified | Family is the tenant boundary. |
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

## Module Execution Workflow

For every module:

1. Before implementation starts, add or update that module's test cases in the `Tests` section.
2. Mark the module `In Progress` in this file and `project-status.md`.
3. Implement only the scoped module work.
4. Run the respective module tests.
5. Fix issues until the module test set passes.
6. Update the module status to `Certified`.
7. Add a certification entry with the test command, result, date, and commit SHA.
8. Update all affected docs in the same commit.
9. Commit and push to GitHub.

Certification requires:

- Test cases were defined before implementation.
- Required module tests passed locally.
- Relevant docs and status tables were updated.
- Code and docs were committed.
- Commit was pushed to GitHub.

## Certification Log

| Module | Status | Test Command | Result | Certified On | Commit |
|---|---|---|---|---|---|
| 1. Foundation | Not certified | TBD before module start | Not run | - | - |
| 2. Authentication | Not certified | TBD before module start | Not run | - | - |
| 3. Family Management | Not certified | TBD before module start | Not run | - | - |
| 4. Member Management | Not certified | TBD before module start | Not run | - | - |
| 5. AI Provider Layer | Not certified | TBD before module start | Not run | - | - |
| 6. Memory System | Not certified | TBD before module start | Not run | - | - |
| 7. Chat | Not certified | TBD before module start | Not run | - | - |
| 8. Food Logging | Not certified | TBD before module start | Not run | - | - |
| 9. Meal Planning | Not certified | TBD before module start | Not run | - | - |
| 10. Daily Dashboard | Not certified | TBD before module start | Not run | - | - |
| 11. Progress Tracking | Not certified | TBD before module start | Not run | - | - |
| 12. Reports and PDF Generation | Not certified | TBD before module start | Not run | - | - |
| 13. Family Leaderboard | Not certified | TBD before module start | Not run | - | - |
| 14. Reminders | Not certified | TBD before module start | Not run | - | - |
| 15. Photo and Voice Logging | Not certified | TBD before module start | Not run | - | - |
| 16. Security, Audit, and Compliance | Not certified | TBD before module start | Not run | - | - |
| 17. Testing and CI/CD | Not certified | TBD before module start | Not run | - | - |

## Documentation Sync Rules

- Keep this module status table, `project-status.md`, and the architecture blueprint aligned after every scope or stack change.
- When a module status changes, update both the tracker in this file and the project status document.
- When APIs, data tables, auth, AI providers, or stack choices change, update the architecture blueprint in the same commit.
- Before starting any module, confirm that module's test cases are documented.
- After finishing any module, run the documented tests and update the certification log.
- Before every commit, run a stale-stack scan and fix any outdated references:
  `rg -n "N[e]xt\\.js|N[e]xtJS|n[e]xt\\.js|n[e]xtjs|T[a]ilwind|t[a]ilwind|s[h]adcn|A[u]th\\.js|N[e]stJS|P[r]isma|s[c]hema\\.prisma|R[e]act PDF|B[u]llMQ" .`
- If the scan returns anything, update all affected docs before committing.
- Every documentation update should be committed and pushed after verification.

## UI Implementation Standard

- Build the frontend with Angular and TypeScript.
- Use Bootstrap CSS for layout, spacing, utilities, responsive grids, forms, buttons, navs, tabs, modals, and cards.
- Keep custom CSS in SCSS files and Bootstrap variable overrides.
- Organize screens as Angular feature folders under `src/app/features`.
- Use standalone components and lazy-loaded routes.
- Use Angular Reactive Forms for member profile, meal logging, health metrics, goals, and reminder forms.
- Use Angular `HttpClient` services for API access.
- Use HTTP interceptors for JWT attachment, refresh handling, and API error normalization.
- Use route guards for authenticated routes, family-admin routes, and member/self-access routes.
- Use Angular services and signals for MVP state management.
- Add NgRx only if shared state becomes difficult to reason about.
- Build the app as an Angular PWA with service worker, manifest, install support, and later push notifications.

## Module 1: Foundation

### Goal

Set up the technical base for frontend, backend, database, shared types, environment configuration, and local development.

### Backend Tasks

- Create FastAPI app.
- Add SQLAlchemy or SQLModel.
- Configure PostgreSQL.
- Add Alembic migrations.
- Add shared settings/config module.
- Add local `.env` loading.
- Add request and response validation with Pydantic.
- Add global exception handlers.
- Add structured logging.
- Add health check endpoint.
- Add Docker Compose services for local PostgreSQL, Redis, and optional S3-compatible storage.

### Frontend Tasks

- Create Angular app.
- Configure TypeScript.
- Install Bootstrap CSS.
- Add Bootstrap theme overrides.
- Configure Angular routing.
- Use Angular standalone components.
- Configure lazy-loaded feature routes.
- Add Angular Reactive Forms setup.
- Add `HttpClient` API services.
- Add auth and error HTTP interceptors.
- Add route guards for authenticated pages.
- Add dark mode.
- Add app shell.
- Add mobile-first layout.
- Add shared Angular components for cards, forms, page headers, empty states, loading states, and confirmation dialogs.
- Add Angular PWA manifest and service worker.
- Add local environment configuration for API base URL.

### Database Tasks

- Create initial SQLAlchemy/SQLModel models.
- Add base models: `User`, `Family`, `FamilyMembership`, `FamilyMember`.
- Add Alembic migrations.
- Add local migration workflow for development.

### APIs

- `GET /api/v1/health`

### Tests

- API health check test.
- Angular smoke render test.
- Angular route guard test.
- Angular API service test.
- Database connection test.

### Dependencies

- None. This is the first module.

## Module 2: Authentication

### Goal

Allow users to sign in and out with Google authentication.

### Backend Tasks

- Configure FastAPI Google OAuth flow.
- Add Google OAuth.
- Add JWT/session handling.
- Add auth dependencies.
- Add current-user dependency.

### Frontend Tasks

- Login screen.
- Google login button.
- Authenticated route wrapper.
- Angular auth guard.
- Angular auth interceptor for JWT attachment.
- User menu.
- Logout action.

### Database Tasks

- Finalize `User`.
- Add Google OAuth identity fields and refresh-token or session tables if required by the FastAPI auth implementation.

### APIs

- `POST /auth/logout`
- `GET /auth/google`
- `GET /auth/google/callback`
- `GET /auth/me`

### Tests

- Start Google OAuth login.
- Complete Google OAuth callback.
- Create or update user from Google profile.
- Protect authenticated routes.

### Dependencies

- Module 1.

## Module 3: Family Management

### Goal

Allow authenticated users to create and manage families.

### Backend Tasks

- Create family service.
- Create family router.
- Add family tenant dependency.
- Add family membership service.
- Assign creator as `FAMILY_ADMIN`.

### Frontend Tasks

- Create family screen.
- Family switcher.
- Family settings screen.
- Empty state when user has no family.

### Database Tasks

- `families`
- `family_memberships`
- Add indexes for `familyId` and `userId`.

### APIs

- `GET /families`
- `POST /families`
- `GET /families/:familyId`
- `PATCH /families/:familyId`
- `DELETE /families/:familyId`

### Tests

- User can create family.
- Creator becomes family admin.
- User cannot access unrelated family.

### Dependencies

- Modules 1 and 2.

## Module 4: Member Management

### Goal

Allow family admins to add, edit, and view family members.

### Backend Tasks

- Create member service.
- Add admin-only create/edit/delete.
- Add self-access rules for members.
- Add profile validation.
- Add member health information support.

### Frontend Tasks

- Member list screen.
- Add member form.
- Edit member form.
- Member profile screen.
- Admin/member access states.

### Database Tasks

- `family_members`
- `member_health_metrics`
- `member_goals`

### APIs

- `GET /families/:familyId/members`
- `POST /families/:familyId/members`
- `GET /families/:familyId/members/:memberId`
- `PATCH /families/:familyId/members/:memberId`
- `DELETE /families/:familyId/members/:memberId`
- `POST /families/:familyId/members/:memberId/health-metrics`
- `GET /families/:familyId/members/:memberId/health-metrics`

### Tests

- Admin can add member.
- Member cannot delete another member.
- Member profile stores health markers.
- Cross-family member access is blocked.

### Dependencies

- Module 3.

## Module 5: AI Provider Layer

### Goal

Create a provider-agnostic AI layer for OpenAI, Gemini, and Anthropic.

### Backend Tasks

- Define `LLMProvider` interface.
- Implement `OpenAIProvider`.
- Stub `GeminiProvider`.
- Stub `AnthropicProvider`.
- Add provider factory.
- Add prompt builder service.
- Add structured JSON validation.
- Add AI safety system prompt.

### Frontend Tasks

- No major UI yet.
- Optional provider selector for admin/developer mode.

### Database Tasks

- Store provider name in chat messages, meal plans, and reports.

### APIs

- Internal service module first.
- No public API required at this stage.

### Tests

- Provider factory returns correct provider.
- Prompt builder includes member context.
- Invalid AI JSON is rejected.
- Provider failure returns safe fallback.

### Dependencies

- Modules 1 and 4.

## Module 6: Memory System

### Goal

Store long-term family and member memory for personalization.

### Backend Tasks

- Create memory service.
- Add family memory.
- Add member memory.
- Add conversation memory extraction.
- Add basic keyword retrieval first.
- Add `pgvector` retrieval later.
- Add memory filtering rules.

### Frontend Tasks

- Optional admin view for memory/debug.
- Member preferences UI should feed memory.

### Database Tasks

- `family_memories`
- `member_memories`
- Add embedding column when `pgvector` is enabled.

### APIs

- Internal:
  - `memory.storeFamilyMemory()`
  - `memory.storeMemberMemory()`
  - `memory.retrieveContext()`
  - `memory.extractFromConversation()`

### Tests

- Durable preferences are stored.
- Temporary statements are ignored.
- Retrieval is scoped by family and member.

### Dependencies

- Modules 3, 4, and 5.

## Module 7: Chat

### Goal

Build WhatsApp-style AI chat with retained conversation history.

### Backend Tasks

- Create conversation session service.
- Create chat message service.
- Integrate AI provider.
- Load member profile and memory context.
- Save user and assistant messages.
- Detect meal logging intent.

### Frontend Tasks

- Chat list.
- Chat screen.
- Message bubbles.
- Streaming response UI.
- Attachment button.
- Voice button placeholder.
- Quick action chips.

### Database Tasks

- `conversation_sessions`
- `chat_messages`

### APIs

- `POST /families/:familyId/members/:memberId/chat/sessions`
- `GET /families/:familyId/members/:memberId/chat/sessions`
- `POST /families/:familyId/members/:memberId/chat/sessions/:sessionId/messages`
- `GET /families/:familyId/members/:memberId/chat/sessions/:sessionId/messages`

### Tests

- Chat creates session.
- Chat stores history.
- AI receives member context.
- Member cannot access another member's session.

### Dependencies

- Modules 4, 5, and 6.

## Module 8: Food Logging

### Goal

Allow users to log meals through manual entry and natural language.

### Backend Tasks

- Create food log service.
- Add natural language parser through LLM.
- Estimate calories and protein.
- Save structured food items.
- Allow user correction.
- Update adherence score.

### Frontend Tasks

- Meal logging screen.
- Natural language form.
- Manual entry form.
- Parsed food confirmation card.
- Edit estimated calories/protein.
- Daily food log list.

### Database Tasks

- `food_logs`

### APIs

- `POST /families/:familyId/members/:memberId/food-logs/manual`
- `POST /families/:familyId/members/:memberId/food-logs/natural-language`
- `GET /families/:familyId/members/:memberId/food-logs`
- `PATCH /families/:familyId/members/:memberId/food-logs/:logId`
- `DELETE /families/:familyId/members/:memberId/food-logs/:logId`

### Tests

- "2 rotis and dal" creates structured food log.
- Calories and protein are saved.
- Corrected estimates override AI estimate.
- Dashboard aggregate can read logs.

### Dependencies

- Modules 5, 6, and 7.

## Module 9: Meal Planning

### Goal

Generate personalized meal plans based on member profile, health goals, food preferences, and memory.

### Backend Tasks

- Create meal plan service.
- Add AI meal plan generation.
- Add calorie/protein target calculation.
- Save generated meal plans.
- Allow plan edits.

### Frontend Tasks

- Meal plan screen.
- Generate tomorrow plan action.
- Meal-by-meal view.
- Swap meal placeholder.
- Save and edit plan.

### Database Tasks

- `meal_plans`

### APIs

- `POST /families/:familyId/members/:memberId/meal-plans/generate`
- `GET /families/:familyId/members/:memberId/meal-plans`
- `PATCH /families/:familyId/members/:memberId/meal-plans/:planId`

### Tests

- Meal plan respects vegetarian/Jain/vegan preference.
- Meal plan excludes allergies.
- Meal plan uses health goals.
- Generated plan is persisted.

### Dependencies

- Modules 4, 5, 6, and 8.

## Module 10: Daily Dashboard

### Goal

Show daily calories, protein, water, exercise, steps, trends, and adherence.

### Backend Tasks

- Create dashboard service.
- Aggregate food logs.
- Aggregate health metrics.
- Add water/exercise/steps support.
- Calculate adherence score.
- Return trend data.

### Frontend Tasks

- Dashboard cards.
- Calories card.
- Protein card.
- Water card.
- Exercise card.
- Steps card.
- Weight trend chart.
- Waist trend chart.
- Coach note panel.

### Database Tasks

- Either add separate activity logs or store daily report summary.
- Recommended future tables:
  - `water_logs`
  - `exercise_logs`
  - `step_logs`

### APIs

- `GET /families/:familyId/members/:memberId/dashboard?date=YYYY-MM-DD`

### Tests

- Dashboard totals match food logs.
- Empty day returns zero state.
- Weight trend orders by date.
- Member can view only own dashboard.

### Dependencies

- Modules 4 and 8.

## Module 11: Progress Tracking

### Goal

Track health markers, body measurements, energy, stamina, and goals over time.

### Backend Tasks

- Add goal progress calculation.
- Add health marker trend service.
- Add weight/waist trend service.
- Add energy and stamina score updates.

### Frontend Tasks

- Progress screen.
- Goal cards.
- Health marker charts.
- Weight trend chart.
- Waist trend chart.
- Add metric form.

### Database Tasks

- Uses `member_health_metrics`.
- Uses `member_goals`.

### APIs

- `GET /families/:familyId/members/:memberId/progress`
- `POST /families/:familyId/members/:memberId/goals`
- `PATCH /families/:familyId/members/:memberId/goals/:goalId`

### Tests

- Goal progress is calculated correctly.
- HbA1c/LDL trends render from latest metrics.
- Admin can view all member progress.
- Member can view own progress.

### Dependencies

- Modules 4 and 10.

## Module 12: Reports and PDF Generation

### Goal

Generate daily, weekly, monthly, and family reports with downloadable PDFs.

### Backend Tasks

- Create report service.
- Create report worker.
- Add AI report summaries.
- Add PDF rendering.
- Upload PDFs to S3.
- Generate signed download URLs.

### Frontend Tasks

- Reports screen.
- Generate report buttons.
- Report list.
- PDF download action.
- Report status states.

### Database Tasks

- `daily_reports`
- `weekly_reports`
- `monthly_reports`
- `pdf_reports`

### APIs

- `POST /families/:familyId/members/:memberId/reports/daily/generate`
- `POST /families/:familyId/members/:memberId/reports/weekly/generate`
- `POST /families/:familyId/members/:memberId/reports/monthly/generate`
- `POST /families/:familyId/reports/family/generate`
- `POST /families/:familyId/reports/:reportId/pdf`
- `GET /families/:familyId/reports/:reportId/pdf`

### Tests

- Weekly report summarizes logs and progress.
- Admin can generate family report.
- Member cannot download another member's PDF.
- PDF record is created after generation.

### Dependencies

- Modules 5, 8, 10, and 11.

## Module 13: Family Leaderboard

### Goal

Show family-level rankings for adherence, improvement, activity, and consistency.

### Backend Tasks

- Create leaderboard service.
- Calculate best adherence.
- Calculate most improved.
- Calculate highest activity.
- Calculate most consistent.
- Support daily, weekly, monthly periods.

### Frontend Tasks

- Leaderboard screen.
- Period selector.
- Member ranking cards.
- Admin/member visibility.

### Database Tasks

- Uses logs, reports, health metrics, and activity data.

### APIs

- `GET /families/:familyId/leaderboard?period=weekly`

### Tests

- Leaderboard ranks correctly.
- Ties are handled consistently.
- Only family members are included.

### Dependencies

- Modules 8, 10, and 11.

## Module 14: Reminders

### Goal

Send meal, water, walking, and medication reminders.

### Backend Tasks

- Create reminder service.
- Create reminder worker.
- Add schedule parser.
- Add notification queue.
- Add email reminder first.
- Add PWA push later.

### Frontend Tasks

- Reminder settings screen.
- Create reminder form.
- Enable/disable reminder toggle.
- Reminder list.

### Database Tasks

- `reminders`

### APIs

- `GET /families/:familyId/members/:memberId/reminders`
- `POST /families/:familyId/members/:memberId/reminders`
- `PATCH /families/:familyId/members/:memberId/reminders/:reminderId`
- `DELETE /families/:familyId/members/:memberId/reminders/:reminderId`

### Tests

- Reminder is created.
- Disabled reminder does not send.
- Medication reminders are visible only to permitted users.
- Worker picks due reminders.

### Dependencies

- Modules 4 and 10.

## Module 15: Photo and Voice Logging

### Goal

Enable richer food logging through photo upload and voice input.

### Backend Tasks

- Add S3 upload service.
- Add signed upload URLs.
- Add photo meal review through multimodal LLM.
- Add audio upload.
- Add voice transcription.
- Convert transcript to natural language food log.

### Frontend Tasks

- Photo upload in chat and meal log.
- Camera capture for mobile.
- Voice recording button.
- Upload progress states.
- Review parsed result before saving.

### Database Tasks

- Use `food_logs.photoUrl`.
- Use `food_logs.audioUrl`.

### APIs

- `POST /families/:familyId/members/:memberId/food-logs/photo`
- `POST /families/:familyId/members/:memberId/food-logs/voice`
- `POST /uploads/signed-url`

### Tests

- Photo creates pending food log.
- Voice transcript creates natural language log.
- Upload access is tenant-scoped.
- Large files are rejected.

### Dependencies

- Modules 8 and 12 storage setup.

## Module 16: Security, Audit, and Compliance

### Goal

Protect sensitive health data and maintain traceability.

### Backend Tasks

- Add tenant dependencies everywhere.
- Add role/permission dependencies.
- Add audit logging.
- Add rate limiting.
- Add request size limits.
- Add sensitive log redaction.
- Add secure headers.
- Add signed S3 URLs.

### Frontend Tasks

- Consent/disclaimer screens.
- Privacy settings.
- Report download confirmation.
- Session timeout handling.

### Database Tasks

- `audit_logs`
- Add indexes for audit queries.

### APIs

- `GET /families/:familyId/audit-logs`

### Tests

- Cross-tenant access blocked.
- Admin-only routes reject members.
- Report download creates audit log.
- Sensitive fields are not logged.

### Dependencies

- Should begin in Module 2 and continue through all modules.

## Module 17: Testing and CI/CD

### Goal

Ensure reliable delivery through automated checks.

### Tasks

- Add unit tests.
- Add integration tests.
- Add E2E tests.
- Add linting.
- Add type checking.
- Add Alembic migration check.
- Add GitHub Actions CI.
- Keep deployment pipeline deferred until local MVP is stable.
- Document later hosting path for Vercel-style web hosting and Render-style FastAPI hosting.

### Required Test Groups

- Auth tests.
- Family/member permission tests.
- AI provider tests.
- Food logging tests.
- Dashboard aggregate tests.
- Report generation tests.
- PDF download permission tests.

### Dependencies

- Starts in Module 1 and continues throughout development.

## Suggested Team Allocation

### Frontend Developer

- App shell
- Auth screens
- Dashboard
- Chat
- Meal logging
- Progress
- Reports
- Admin screens

### Backend Developer

- FastAPI routers and services
- SQLAlchemy/SQLModel models
- Auth integration
- Tenant dependencies
- APIs
- Workers
- PDF generation

### AI Engineer

- LLM provider abstraction
- Prompt design
- Meal review
- Meal planning
- Report generation
- Memory extraction
- RAG retrieval

### QA Engineer

- Test plans
- E2E tests
- Permission testing
- Mobile testing
- Regression testing

### DevOps Engineer

- CI/CD
- Database provisioning
- Redis
- S3
- Secrets
- Monitoring

## Suggested Sprint Plan

### Sprint 1

- Foundation
- Authentication
- Family creation
- Member CRUD

### Sprint 2

- AI provider layer
- Memory v1
- Chat UI
- Chat persistence

### Sprint 3

- Natural language food logging
- Manual food logging
- Daily dashboard

### Sprint 4

- Meal planning
- Progress tracking
- Health metric trends

### Sprint 5

- Reports
- PDF generation
- Family report

### Sprint 6

- Leaderboard
- Reminders
- Security hardening

### Sprint 7

- Photo logging
- Voice logging
- Advanced analytics

## MVP Scope

For the first production MVP, build:

- Authentication
- Family management
- Member management
- AI chat
- Natural language meal logging
- Daily dashboard
- Meal planning
- Basic weekly report
- PDF download
- Tenant security

Defer:

- Voice logging
- Photo logging
- Advanced analytics
- GraphQL
- Complex reminder channels
