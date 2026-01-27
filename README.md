# Gov Contract OS

This repository contains the code for **Gov Contract OS**, a platform that ingests government contract opportunities, normalizes and enriches the data, extracts compliance requirements, and assists with proposal generation.  
The system is designed to pull data from federal (SAM.gov) and southeastern state procurement portals, normalize disparate fields into a single schema, parse RFP documents to extract requirements, and generate compliance matrices and document packs for bids.  

## Project Layout

The project is structured as a monorepo containing three main applications:

- **API** (`apps/api`): A FastAPI backend responsible for exposing REST endpoints, enqueuing jobs, and interfacing with Supabase for storage.
- **Worker** (`apps/worker`): A Celery worker that runs background tasks such as ingesting opportunities, downloading attachments, parsing documents, extracting requirements, and exporting compliance matrices.
- **Web** (`apps/web`): A Next.js frontend that provides a user interface for searching opportunities, creating workspaces, running pipelines, and viewing generated artifacts.

See each application's README for additional setup and usage details.
