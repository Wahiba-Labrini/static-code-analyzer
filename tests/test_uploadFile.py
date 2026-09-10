from rules.eval_exec_rule import eval_exec
from backend.models import Report,Issue,session

def test_uploadFile():
    code='x=eval("1+1")'
    all_issue=eval_exec(code)
    print(all_issue)
    print("------------------------------------------")
    report=Report(filename="test_uploadFile.py",total_issue=len(all_issue))
    for issue in all_issue:
        print(issue)
        new_issue=Issue(
                    rule_id=issue.get("rule_id"),
                    line=issue.get("line"),
                    severity=issue.get("severity"),
                    message=issue.get("message")
        )
        report.issue.append(new_issue)
    session.add(report)
    session.commit()
    print("SAVED")