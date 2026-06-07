# Development Guide

## Branch Strategy
- `main` (production)
- `develop` (integration)
- `feature/dataset-cleaning`
- `feature/ocr-pipeline`
- `feature/ner-extraction`
- `feature/clause-risk-scoring`
- `feature/integration-testing`

Create branches locally:
```bash
git branch develop
git branch feature/dataset-cleaning
git branch feature/ocr-pipeline
git branch feature/ner-extraction
git branch feature/clause-risk-scoring
git branch feature/integration-testing
```

## Team Ownership
- Ahmad → Dataset processing & cleaning
- Sahasra → OCR pipeline
- Sandeep → NER extraction
- Azmat → Clause classification, risk scoring, integration

## GitHub Issues Backlog
Recommended issue titles:
1. Dataset Parsing
2. OCR Pipeline
3. NER Model
4. Clause Classification
5. Risk Scoring
6. Vector Database
7. FastAPI Backend
8. Celery Tasks
9. Dockerization
10. Testing & Documentation

## Branch Protection Recommendations
Apply on `main`:
- Disable direct pushes
- Require pull requests
- Require at least 1 approval
- Require CI checks to pass

## Daily Commit Message Suggestions
- Ahmad:
  - `feat(data): add raw contract parser`
  - `chore(data): normalize metadata fields`
- Sahasra:
  - `feat(ocr): add pdf text extraction flow`
  - `fix(ocr): improve scan preprocessing`
- Sandeep:
  - `feat(ner): add legal entity labels`
  - `test(ner): add extraction regression cases`
- Azmat:
  - `feat(classifier): add clause taxonomy baseline`
  - `feat(risk): add weighted risk scoring engine`
  - `feat(integration): wire classifier and risk APIs`

## MLOps Standards for This Repo
- Keep datasets versioned by metadata and checksum.
- Use reproducible preprocessing and model config files.
- Track model inputs/outputs for evaluation reproducibility.
- Gate merges with CI lint/test/build checks.
- Use containerized services for local parity with deployment.
