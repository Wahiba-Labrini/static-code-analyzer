import ast
def password(source_code:str):
    sensitive_words=["password","psswd","key","secret","key_api","secret_key","pwd"]
    tree=ast.parse(source_code)
    for node in ast.walk(tree):
        if isinstance(node,ast.Assign):
            var_name=node.targets[0].id.lower()
            if any(word in var_name for word  in sensitive_words):
                if isinstance(node.value,ast.Constant):
                    print(f"WARNING :variable'{node.targets[0].id}' contains hardcoded secret at line {node.lineno}")
    

if __name__ == "__main__":
    code ='''
password="1234567"
'''

password(code)



