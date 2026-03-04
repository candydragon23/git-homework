import sys
sys.path.append('../src')
from math_demo import (add, add_with_bug)
def test_addition():
    assert add(2, 2) == 4
    print('test basic addition')
def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    print('test basic addition with bugs')
    #assert add_with_bug(6, 7) == 13 # will fail here
def test_addition_duplicated():
    #is it a real good test (relies on abscence of + in add)
    assert add(2, 3) == 2 + 3
    print('test addition duplicated')
if __name__ == '__main__':
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()