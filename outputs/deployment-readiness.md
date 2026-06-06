# Deployment Readiness

Use this when we move beyond local development and put the UI on Vercel and the API on Render.

## Target Layout

- Frontend: Angular app on Vercel
- Backend: FastAPI app on Render
- Database: Render Postgres
- Queue: Render Redis
- File storage: Google Cloud Storage
- Auth: Google OAuth with JWT session tokens

## Must-Have Decisions

1. The frontend must know the public API URL at build time.
2. The backend must know the public frontend URL for the auth callback.
3. Google OAuth must use the deployed callback URI, not the local one.
4. CORS must allow the deployed frontend origin.
5. Preview environments need either a staging backend or a fixed preview domain, because preview URLs can change.

## Frontend On Vercel

1. Create a Vercel project for `apps/web`.
2. Use the Angular build output from `apps/web`.
3. Keep the production API base URL pointed at the deployed Render API.
4. If the Angular router returns 404s on refresh, add a SPA rewrite so the browser always lands on `index.html` first.
5. Set the production custom domain in Vercel once the deployment is stable.
6. For preview deployments, make sure the API base URL and backend CORS policy point at the matching preview origin or a staging frontend domain.

### Frontend build note

Angular reads the API base URL at build time in this repo, so before the first Vercel deploy we need one of these:

- update `apps/web/src/environments/environment.prod.ts` with the Render API URL, or
- add a runtime config file that the app fetches on startup

Without that step, the deployed UI will not know where to send API requests.

## Backend On Render

1. Create a Render web service for `apps/api`.
2. Set the root directory to `apps/api` if the service is created from the repo.
3. Build command: `pip install .`
4. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Make sure the service binds to `0.0.0.0` and uses Render’s `PORT` value.
6. Set the production environment variables in Render.
7. Confirm the service health endpoint returns `{"status":"ok"}`.

### Backend environment variables

Set these in Render for production:

- `DATABASE_URL` -> Render Postgres connection string
- `REDIS_URL` -> Render Redis connection string
- `JWT_SECRET` -> strong production secret
- `GOOGLE_CLIENT_ID` -> Google OAuth client ID
- `GOOGLE_CLIENT_SECRET` -> Google OAuth client secret
- `GOOGLE_REDIRECT_URI` -> deployed API callback, for example `https://<your-render-api>/api/v1/auth/google/callback`
- `FRONTEND_APP_URL` -> deployed Vercel URL, for example `https://<your-app>.vercel.app`
- `GCP_PROJECT_ID` -> Google Cloud project ID
- `GCS_BUCKET_NAME` -> Google Cloud Storage bucket name
- `GCP_SERVICE_ACCOUNT_JSON` -> service account JSON as a secret string

## Google OAuth

1. Add the Render callback URL in Google Cloud OAuth settings.
2. Add the Vercel frontend URL as the allowed frontend callback target in the backend.
3. Keep the local callback URI only for development.
4. If you use preview deployments, either add the preview origin explicitly or route previews through a fixed staging URL.

## CORS And Routing

1. The backend CORS allowlist must include the deployed Vercel origin.
2. The frontend must send requests to the Render API URL.
3. Angular client routes like `/login`, `/auth/callback`, `/families/new`, and `/chat` must resolve correctly on refresh.
4. If route refreshes 404 on Vercel, add a rewrite for the SPA shell.

## Data And Background Services

1. Provision Render Postgres before production traffic.
2. Provision Render Redis before reminders, queues, or report jobs go live.
3. Connect the API to Google Cloud Storage before enabling photo uploads and PDF exports in production.
4. Prefer real migrations for production traffic. The local schema bootstrap is useful for development, but production should move to Alembic migrations as soon as the migration files exist.

## Security And Ops

1. Use a strong, unique `JWT_SECRET`.
2. Keep secrets out of Git and only set them in Vercel and Render environments.
3. Turn on HTTPS/custom domains after the first successful deploy.
4. Use logs from Vercel build output and Render service logs to debug deploy failures.
5. Keep a production-only environment checklist for CORS, OAuth callback URI, frontend URL, database, Redis, and storage.

## Deployment Checklist

- [ ] Angular build points at the deployed Render API.
- [ ] SPA routes resolve on Vercel refresh.
- [ ] Render API starts with `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
- [ ] Render env vars are set.
- [ ] Google OAuth callback URI is updated for production.
- [ ] Vercel origin is allowed by backend CORS.
- [ ] Postgres is provisioned and connected.
- [ ] Redis is provisioned and connected.
- [ ] Google Cloud Storage bucket is provisioned and connected.
- [ ] Health endpoint returns ok in production.
- [ ] Auth login and callback work from the deployed frontend.
