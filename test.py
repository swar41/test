# test_calculator.py
from saw import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 2) == -1
    assert subtract(-1, -1) == 0
