def extract_keywords(requirement):
    keywords = []
    if "shutdown" in requirement:
        keywords.append(requirement)
    if "恢复" in requirement:
        keywords.append(requirement)
    if "BGP" in requirement:
        keywords.append(requirement)
    return keywords

def evaluate_code(code,requirement):
    score = 0
    details = {}

    matched = []
    keywords = extract_keywords(requirement)
    for keyword in keywords:
        if keyword.lower() in code.lower():
            matched.append(keyword)
    if len(keywords) > 0:
        coverage_score = int(
            len(matched) / len(keywords) * 40
        )
    score += coverage_score
    details["coverage"] = {
        "score": coverage_score,
        "matched": matched,
    }

    if "assert" in code:
        score += 20
        details["assert"] = "PASS"
    else:
        details["assert"] = "FAIL"

    if "try" in code:
        score += 20
        details["exception"] = "PASS"
    else:
        details["exception"] = "FAIL"

    if "#" in code or "log" in code.lower():
        score += 20
        details["style"] = "PASS"
    else:
        details["style"] = "FAIL"

    return {
        "score": score,
        "details": details
    }