import ast
def eval_exac(source_code:str):
    tree=ast.parse(source_code)
    for node in ast.walk(tree):
        if isinstance(node,ast.Call):
            if isinstance(node.func,ast.Name):
                print(node.func.id)

if __name__=="__main__":
    code='''
x=eval(1+1)
y=exec("print(1)")
'''

eval_exac(code)
        


        
