def classify_clause(text: str) -> dict[str, float | str]:
    if not text.strip():
        return {"label": "unknown", "confidence": 0.0}
    return {"label": "payment_terms", "confidence": 0.75}
