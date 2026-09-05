import ast
def pickle_load(source_code:str):
    tree=ast.parse(source_code)
    for node in ast.walk(tree):
        if isinstance(node,ast.Call):
            if isinstance(node.func,ast.Attribute):
                if node.func.attr=="load":
                    print(f"WARNING:contains pickle.load at line {node.lineno}")


if __name__ == "__main__" :
    code="""
import pickle
data=pickle.load(file)
"""

pickle_load(code)