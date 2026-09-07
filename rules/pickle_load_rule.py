import ast
def pickle_load(source_code:str):
    issue=[]
    tree=ast.parse(source_code)
    for node in ast.walk(tree):
        if isinstance(node,ast.Call):
            func_name=None
            
            if isinstance(node.func,ast.Attribute):
                func_name=node.func.attr
            elif isinstance(node.func,ast.Name):
                func_name=node.func.id

            if func_name=="load":
                     issue.append({
                        "line":node.lineno,
                        "rule_id":"pickle-load",
                        "severity":"High",
                        "message":f"Use of pickle.load(): risk of code execution during deserialization"   
                    })
    return issue
                    

if __name__ == "__main__" :
    code="""
import pickle
data=pickle.load(file)
"""
    pickle_load(code)