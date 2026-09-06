from rules.eval_exec_rule import eval_exec 
from rules.password_rule import password
from rules.pickle_load_rule import pickle_load
from rules.sql_injection_rule import sql_injection
from rules.subprocess_shell_rule import subprocess_shell

#============================== Test rule Eval Exec============================

def test_eval_exec():
    code='x=eval(1+1)'
    res=eval_exec(code)
    assert len(res)==1


def test_no_evalexec():
    code='x=1+1'
    res=eval_exec(code)
    assert len(res)==0


def test2_eval_exec():
    code='x=exec("print(1)")'
    res=eval_exec(code)
    assert len(res)==1

#============================== Test rule Password ============================


def test_password():
    code="password='12345678'"
    res=password(code)
    assert len(res)==1


def test_db_password():
    code="db_password='12345678'"
    res=password(code)
    assert len(res)==1

  
def test_no_password():
    code="x=y+1"
    res=password(code)
    assert len(res)==0


def test_invalid_password():
    code="keyboard='hello world'"
    res=password(code)
    assert len(res)==0
    
#============================== Test rule Subprocess Shell ============================   


def test_subprocess_shell():
    code="subprocess.run('ls',shell=True)"
    res=subprocess_shell(code)
    assert len(res)==1


def test_no_subprocess_shell():
    code="""
print("True")
"""
    res=subprocess_shell(code)
    assert len(res)==0


def test0_subprocess_shell():
    code="""
subprocess.run('ls',shell=user_shell)
"""
    res=subprocess_shell(code)
    assert len(res)==0


def test1_subprocess_shell():
    code="""
subprocess.run("USER")
"""
    res=subprocess_shell(code)
    assert len(res)==0


def test2_subprocess_shell():
    code="""
subprocess.call('ls',shell=True)
"""
    res=subprocess_shell(code)
    assert len(res)==1


def test2_no_subprocess_shell():
    code="""
subprocess.call('ls',shell=False)
"""
    res=subprocess_shell(code)
    assert len(res)==0


def test3_subprocess_shell():
    code="""
import subprocess as sp
sp.call('ls',shell=True)
"""
    res=subprocess_shell(code)
    assert len(res)==1


def test2_invalid_subprocess_shell():
    code="""
from subprocess import run
run('ls',shell=True)
"""
    res=subprocess_shell(code)
    assert len(res)==1

#============================== Test rule SQL Injection ================================


def test_sql_injection():
    code="""
USER_id=3
cursor.execute('select*from USERS where id = ' + USER_id)"""
    res=sql_injection(code)
    assert len(res)==1


def test_no_sql_injection():
    code="""
USER_id=2
cursor.execute(' USER_id')"""
    res=sql_injection(code)
    assert len(res)==0


def test1_sql_injection():
    code="""
USER_id=3
cursor=('select*from USERS where id = ' , USER_id)"""
    res=sql_injection(code)
    assert len(res)==0


def test_invalid_sql_injection():
    code="""
query=('select*from USERS where id ={USER_id})"""
    res=sql_injection(code)
    assert len(res)==1

#============================== Test rule Pickle Load ===================================


def test_pickle_load():
    code="""
import pickle 
data=pickle.load(file)"""
    res=pickle_load(code)
    assert len(res)==1


def test_no_pickle_load():
    code="""
import pickle 
print('file')"""
    res=pickle_load(code)
    assert len(res)==0


def test_pickle_load():
    code="""
from pickle  import load
data=load(file)"""
    res=pickle_load(code)
    assert len(res)==1
    
    