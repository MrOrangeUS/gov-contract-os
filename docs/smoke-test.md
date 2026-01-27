# Gov Contract OS — Smoke Test (v1 baseline)

## 1) API Health
- Visit:
  - `GET /health`
- Expected:
  - HTTP 200
  - JSON response indicating service is up

## 2) Jobs Status Endpoint
- Call:
  - `GET /jobs/status/{taskId}`
- Expected:
  - HTTP 200
  - JSON includes:
    - `task_id`
    - `state` (PENDING / STARTED / SUCCESS / FAILURE)
    - `result` populated only if successful
    - `error` populated only if failed

## 3) UI Pipeline Trigger
- Go to frontend Opportunities page
- Click **Run Pipeline** on an opportunity
- Expected:
  - Toast: “Pipeline started”
  - Button goes into “Running” state (disabled)
  - UI polls status until terminal state
  - On success:
    - Toast success
    - Button becomes disabled (Completed)
    - If `webViewLink` exists: “View Compliance XLSX” appears and opens Google Drive link

## Notes (v1)
- Tasks are stubbed intentionally.
- “SUCCESS” confirms wiring + queue + status propagation, not real parsing/export.
