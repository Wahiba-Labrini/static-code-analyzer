import ast
def sql_injection(source_code:str):
    issue=[]
    tree=ast.parse(source_code)
    for node in ast.walk(tree):
        if isinstance(node,ast.Call):
            if isinstance(node.func,ast.Attribute):
                if node.func.attr=="execute":
                    if len(node.args)>0:
                        if isinstance(node.args[0],(ast.BinOp,ast.JoinedStr)):
                            issue.append({
                                "line":node.lineno,
                                "rule_id":"💉 sql-injection",
                                "severity":"High",
                                "message":f"SQL query built using string concatenation : risk of SQL injection"   
                            })
    return issue


if __name__=="__main__":
    code="""
USER_id=3
cursor.execute("select*from USERS where id = " + USER_id)
"""
    sql_injection(code)
            