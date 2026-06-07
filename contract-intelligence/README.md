# AI-Powered Contract Intelligence & Risk Scoring

Production-ready starter repository for NLP-driven contract analysis.

## Features
- Contract ingestion for PDF/DOCX workflows
- OCR and entity extraction pipeline scaffolding
- Clause classification and risk scoring modules
- Semantic search foundation with Milvus/Pinecone integration hooks
- FastAPI service + Celery worker architecture
- Dockerized local stack and CI workflows

## Repository Structure
See `DEVELOPMENT_GUIDE.md` for team workflows, branch strategy, and issue mapping.

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.api.main:app --reload
```

## Run Tests and Lint
```bash
pytest
ruff check .
python -m compileall src
```

## Docker
```bash
docker compose up --build
```

## Branches
- `main`: production
- `develop`: integration
- `feature/dataset-cleaning`
- `feature/ocr-pipeline`
- `feature/ner-extraction`
- `feature/clause-risk-scoring`
- `feature/integration-testing`
