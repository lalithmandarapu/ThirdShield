def assess_risk(text):
    score = 0
    if "encryption" in text.lower():
        score += 10
    if "iso27001" in text.lower():
        score += 20
    if "soc 2" in text.lower():
        score += 20
    if "breach" in text.lower():
        score -= 30
    return score
