from sql_injection_rule import sql_injection

# Tests for the SQL Injection rule


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


def test_without_concatenation():
    code="""
USER_id=3
cursor=('select*from USERS where id = ' , USER_id)"""
    res=sql_injection(code)
    assert len(res)==0


def test_f_string():
    code="""
cursor.execute(f"select*from USERS where id ={USER_id}")
"""
    res=sql_injection(code)
    assert len(res)==1
