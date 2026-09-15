from hardcoded_secret_rule import hardcoded_secret

#Tests for the Hardcoded Secret rule


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


def test_verification_keyboard():
    code="keyboard='hello world'"
    res=password(code)
    assert len(res)==0