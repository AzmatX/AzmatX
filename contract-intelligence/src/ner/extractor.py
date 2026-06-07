from typing import Any


def extract_entities(text: str) -> list[dict[str, Any]]:
    if not text.strip():
        return []
    return [{"text": "Sample Entity", "label": "ORG", "start": 0, "end": 13}]
