from main import compare_int
from random import randint

def test_compare_int():
    x=randint(0,100)
    assert compare_int(x,x-1) == 1
    assert compare_int(x,x) == 0
    assert compare_int(x,x+1) == -1