from eval_exec_rule import eval_exec

# Tests for the Eval Exec  rule

def test_eval():
    code='x=eval(1+1)'
    res=eval_exec(code)
    assert len(res)==1


def test_no_evalExec():
    code='x=1+1'
    res=eval_exec(code)
    assert len(res)==0


def test_exec():
    code='x=exec("print(1)")'
    res=eval_exec(code)
    assert len(res)==1