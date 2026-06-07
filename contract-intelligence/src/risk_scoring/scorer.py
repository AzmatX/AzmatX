def score_contract_risk(clause_labels: list[str]) -> dict[str, float | str]:
    if not clause_labels:
        return {"risk_level": "low", "score": 0.1}

    risk_keywords = {"termination", "liability", "indemnity", "penalty"}
    hits = sum(1 for label in clause_labels if label.lower() in risk_keywords)
    score = min(1.0, hits / max(1, len(clause_labels)))

    if score >= 0.7:
        level = "high"
    elif score >= 0.3:
        level = "medium"
    else:
        level = "low"

    return {"risk_level": level, "score": round(score, 2)}
