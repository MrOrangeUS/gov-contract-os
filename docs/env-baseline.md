# Gov Contract OS — ENV Baseline (names only)

This document lists **environment variable names only** for the v1 baseline.
Do **not** store secrets in this repo.

## API (Render Web Service)
- APP_ENV
- SUPABASE_URL
- SUPABASE_SERVICE_ROLE_KEY
- REDIS_URL
- JOBS_API_KEY
- SAM_API_KEY (optional in v1, stubbed pipeline)
- GOOGLE_APPLICATION_CREDENTIALS_JSON (optional in v1, Drive export stubbed)
- GDRIVE_ROOT_FOLDER_ID (optional in v1)

## Worker (Render Background Worker)
- APP_ENV
- SUPABASE_URL
- SUPABASE_SERVICE_ROLE_KEY
- REDIS_URL
- SAM_API_KEY (optional in v1)
- GOOGLE_APPLICATION_CREDENTIALS_JSON (optional in v1)
- GDRIVE_ROOT_FOLDER_ID (optional in v1)

## Frontend (Vercel)
- API_BASE_URL (server-side only; used by Next.js route handlers)
- JOBS_API_KEY (server-side only; used by Next.js route handlers)

Notes:
- Frontend must never expose secrets to the browser.
- Use Render “Environment” + Vercel “Environment Variables” UI to manage secrets.
