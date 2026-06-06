# Personal Runbook

## Google OAuth Local Setup

When the login page shows Google OAuth blocked or `client_id` is missing, set up Google Cloud like this:

1. Open **Google Cloud Console** and select the project.
2. Go to **Google Auth Platform**.
3. Open **Settings** only if you need general app config, but the actual OAuth client is under **Clients**.
4. If the page says Google Auth Platform is not configured, click **Get started**.
5. Complete the consent screen setup:
   - App name: `Family Health Coach AI`
   - User support email: your Google account
   - Developer contact email: your Google account
6. Choose **External** if you want to sign in with your own Gmail during development.
7. Add your Google account under **Test users** while the app is in testing mode.
8. Return to **Clients**.
9. Click **Create client**.
10. Choose **Web application**.
11. Name it something like `Family Health Coach AI Local`.
12. Add this authorized redirect URI exactly:
    ```text
    http://localhost:8000/api/v1/auth/google/callback
    ```
13. Create the client and copy:
    - **Client ID** -> `GOOGLE_CLIENT_ID`
    - **Client secret** -> `GOOGLE_CLIENT_SECRET`
14. Put the values into `apps/api/.env`.
15. Restart FastAPI.
16. Try the login flow again from `http://127.0.0.1:4200/login`.

## Local OAuth Notes

- The app forces Google account selection with `prompt=select_account consent`.
- If Google still shows `Access blocked`, the usual cause is missing or incorrect OAuth credentials.
- If the browser lands on a local `503` response, it means `GOOGLE_CLIENT_ID` or `GOOGLE_CLIENT_SECRET` is still unset in `apps/api/.env`.
