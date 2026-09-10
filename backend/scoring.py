rules_weiths={
        "eval-exec":20,
        "pickle-load":18,
        "sql-injection":15,
        "subprocess-shell":15,
        "hardcoded-secret":10,    
    }
def calculate_score(all_issue):
    score=100
    for issue in all_issue:
        rule_id=issue.get("rule_id")
        weight=rules_weiths.get(rule_id,5)
        print(rule_id,weight)
        score -= weight
    return max(score,0)


