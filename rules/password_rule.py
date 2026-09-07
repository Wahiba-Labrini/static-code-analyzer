import ast
def password(source_code:str):
    issue=[]
    sensitive_words=["password","psswd","key","secret","key_api","secret_key","pwd"]
    tree=ast.parse(source_code)
    for node in ast.walk(tree):
        if isinstance(node,ast.Assign):
            var_name=node.targets[0].id.lower()
            parts=var_name.split('_')
            if any(word in parts for word  in sensitive_words):
                if isinstance(node.value,ast.Constant):
                    issue.append({
                        "line":node.lineno,
                        "rule_id":"hardcoded secrets",
                        "severity":"High",
                        "message":f" Variabale '{node.targets[0].id}' contains a hardcoded secret"
                    })
    return issue
    

if __name__ == "__main__":
    code ='''
password="1234567"
'''
    password(code)



