from subprocess_shell_rule import subprocess_shell

#Tests for the Subprocess Shell rule


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


def test_shell_defTrue():
    code="""
subprocess.run('ls',shell=user_shell)
"""
    res=subprocess_shell(code)
    assert len(res)==0


def test_without_cmd_shell():
    code="""
subprocess.run("USER")
"""
    res=subprocess_shell(code)
    assert len(res)==0


def test_subprocess_call():
    code="""
subprocess.call('ls',shell=True)
"""
    res=subprocess_shell(code)
    assert len(res)==1


def test_shell_false():
    code="""
subprocess.call('ls',shell=False)
"""
    res=subprocess_shell(code)
    assert len(res)==0


def test_subprocess_alias():
    code="""
import subprocess as sp
sp.call('ls',shell=True)
"""
    res=subprocess_shell(code)
    assert len(res)==1


def test_from_import():
    code="""
from subprocess import run
run('ls',shell=True)
"""
    res=subprocess_shell(code)
    assert len(res)==1

