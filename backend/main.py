from fastapi import FastAPI,UploadFile,File
from pydantic import BaseModel
from rules.eval_exec_rule import eval_exec 
from rules.password_rule import password
from rules.pickle_load_rule import pickle_load
from rules.sql_injection_rule import sql_injection
from rules.subprocess_shell_rule import subprocess_shell
from backend.models import Report,Issue,session
from backend.scoring import calculate_score






app=FastAPI()

@app.get("/")
def check_status():
    return{"message":"Good Status"}



rules_info=[
    {"rule_id":"eval-exec","name":"Eval/Exec detection ","description":"detects dangerous use of eval() and exec()"},
    {"rule_id":"hardcoded-secret","name":"Hardcoded Secrets ","description":"detects passwords written directly in code"},
    {"rule_id":"subprocess-shell","name":"Subprocess Shell ","description":"detects subprocess calls with shell=True"},
    {"rule_id":"sql-injection","name":"SQL Injection ","description":"detects SQL queries built via string concatenation"},
    {"rule_id":"pickle-load","name":"Pickle Deserialisation ","description":"detects use of pckle.load()"}
]

@app.get("/rules")
def get_rules():
    return rules_info



@app.post("/analyzer")
async def upload_file(file:UploadFile = File(...)):
    if  not file.filename.endswith('.py'):
        return{'File should be a python file'}

    content= await file.read()
    source_code=content.decode('utf-8')

    all_issue=[]
    all_issue+=eval_exec(source_code)
    all_issue+=password(source_code) 
    all_issue+=subprocess_shell(source_code) 
    all_issue+=sql_injection(source_code) 
    all_issue+=pickle_load(source_code) 

    score=calculate_score(all_issue)

   
    report=Report(filename=file.filename,
                total_issue=len(all_issue),score=score)

    for issue in all_issue:
        new_issue=Issue (rule_id=issue.get("rule_id") ,
                        line= issue.get("line") ,
                        severity=issue.get("severity") ,
                         message=issue.get("message") 
            )
        report.issue.append(new_issue)

    session.add(report)
    session.commit()

    return {
            'filename':file.filename,
            'total_issue':len(all_issue),
            'issue':all_issue,
            'message':"File Uploaded successfuly"
        }



