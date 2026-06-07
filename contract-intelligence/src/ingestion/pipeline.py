from pathlib import Path


def ingest_contract(file_path: str) -> dict[str, str]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Contract file not found: {file_path}")
    return {"file_name": path.name, "status": "ingested"}
