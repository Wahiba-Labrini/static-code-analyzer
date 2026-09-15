from pickle_load_rule import pickle_load

# Tests for the  Pickle Load  Rule


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


def test_from_import():
    code="""
from pickle  import load
data=load(file)"""
    res=pickle_load(code)
    assert len(res)==1
    
    