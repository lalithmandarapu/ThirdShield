def assess_risk(content):
    keywords = ['breach', 'malware', 'unauthorized', 'phishing', 'leak', 'compliance']
    score = sum(word in content.lower() for word in keywords) * 10
    return min(score, 100)

def get_risk_details(score):
    if score < 30:
        return {
            "level": "Low",
            "description": "Minimal risk identified. Mostly secure data with little to no sensitive info.",
            "prevention": "Continue monitoring and ensure regular vendor audits."
        }
    elif 30 <= score < 70:
        return {
            "level": "Medium",
            "description": "Moderate risk. Data may contain some potentially exploitable information.",
            "prevention": "Enforce stronger vendor agreements and apply regular access controls."
        }
    else:
        return {
            "level": "High",
            "description": "Critical risk. Vendor document includes sensitive or security-threatening data.",
            "prevention": "Immediately review vendor operations, restrict data sharing, and conduct risk audits."
        }
