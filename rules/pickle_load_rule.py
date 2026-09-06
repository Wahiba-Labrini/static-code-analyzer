import ast
def pickle_load(source_code:str):
    issue=[]
    tree=ast.parse(source_code)
    for node in ast.walk(tree):
        if isinstance(node,ast.Call):
            if isinstance(node.func,ast.Attribute):
                if node.func.attr=="load":
                    issue.append({
                        "line":node.lineno,
                        "rule_id":"pickle-load",
                        "severity":"High",
                        "message":f"Variable {node.func.attr} contains pickle load"   
                    })
    return issue
                    

if __name__ == "__main__" :
    code="""
import pickle
data=pickle.load(file)
"""
    pickle_load(code)