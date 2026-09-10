import ast
def subprocess_shell(source_code:str):
    issue=[]
    tree=ast.parse(source_code)
    for node in ast.walk(tree):
        if isinstance(node,ast.Call):
            func_name=None
            
            if isinstance(node.func,ast.Attribute):  
                func_name=node.func.attr
            elif isinstance(node.func,ast.Name):  
                func_name=node.func.id

            if func_name  in ['run','call','Popen','check_output'] :
                    for key in  node.keywords:
                        if key.arg=="shell":
                            if isinstance(key.value,ast.Constant):
                                if key.value.value==True:
                                    issue.append({
                                        "line":node.lineno,
                                        "rule_id":"subprocess-shell",
                                        "severity":"High",
                                        "message":f"Subprocess.{func_name}() Called with shell=True: risk of command injection"   
                                    })
    return issue
                    

if __name__== "__main__":
    code='subprocess.run("ls",shell=True)'
    subprocess_shell(code)

