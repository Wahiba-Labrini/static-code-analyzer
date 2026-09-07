import ast
def eval_exec(source_code:str):
    issue=[]
    tree=ast.parse(source_code)
    for node in ast.walk(tree):
        if isinstance(node,ast.Call):
            if isinstance(node.func,ast.Name):
                if node.func.id in ['eval','exec']:
                    issue.append({
                        "line":node.lineno,
                        "rule_id":"eval-exec",
                        "severity":"High",
                        "message":f"Dangerous use of  {node.func.id}():risk of arbitrary code execution"
                    })
    return issue

if __name__=="__main__":
    code='''
x=eval(1+1)
y=exec("print(1)")
'''
    eval_exec(code)
        


        
