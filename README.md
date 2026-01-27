# Gov Contract OS

This repository contains the code for **Gov Contract OS**, a platform that ingests government contract opportunities, normalizes and enriches the data, extracts compliance requirements, and assists with proposal generation.  
The system is designed to pull data from federal (SAM.gov) and southeastern state procurement portals, normalize disparate fields into a single schema, parse RFP documents to extract requirements, and generate compliance matrices and document packs for bids.  

## Project Layout

The project is structured as a monorepo containing three main applications:

- **API** (`apps/api`): A FastAPI backend responsible for exposing REST endpoints, enqueuing jobs, and interfacing with Supabase for storage.
- **Worker** (`apps/worker`): A Celery worker that runs background tasks such as ingesting opportunities, downloading attachments, parsing documents, extracting requirements, and exporting compliance matrices.
- **Web** (`apps/web`): A Next.js frontend that provides a user interface for searching opportunities, creating workspaces, running pipelines, and viewing generated artifacts.

See each application's README for additional setup and usage details.

## V1 Baseline — Infra + Pipeline Skeleton

**Status:** v1 baseline is a locked skeleton with end-to-end wiring and callable pipeline.

✅ Done
- Supabase + Redis + Render + Vercel wiring
- Next.js UI: Run Pipeline button + toasts + polling + View Compliance XLSX support
- FastAPI /jobs endpoints for enqueue + status
- Celery worker discovers task names and can execute pipeline calls (tasks stubbed)

⏳ Deferred (intentionally not implemented in v1)
- Live SAM.gov ingestion
- Real PDF parsing + requirement extraction
- Real Compliance XLSX generation + Drive export/permissions
