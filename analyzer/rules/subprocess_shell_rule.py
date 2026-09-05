import ast
def subprocess_shell(source_code:str):
    tree=ast.parse(source_code)
    for node in ast.walk(tree):
        if isinstance(node,ast.Call):
            if isinstance(node.func,ast.Attribute):
                if node.func.attr in ['run','call','Popen','check_output']:
                    for kew in  node.keywords:
                        if kew.arg=="shell":
                            if isinstance(kew.value,ast.Constant):
                                if kew.value.value==True:
                                    print(f"WARNING: contains subprocess with shell=true  at line {node.lineno}")

if __name__== "__main__":
    code='subprocess.run("ls",shell=True)'
    subprocess_shell(code)

