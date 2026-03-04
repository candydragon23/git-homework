import sys
sys.path.append('../src')
from math_demo import (add, add_with_bug, calculate_tax_with_bug)
def test_addition():
    assert add(2, 2) == 4
    print('test basic addition')
def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    print('test basic addition with bugs')
    #assert add_with_bug(6, 7) == 13 # will fail here
def test_addition_duplicated():
    assert add(2, 3) == 2 + 3
    print('test addition duplicated')
def test_addition_overcomplicated():
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == sum(i, j)
            assert add(-i, -j) == sum(-i, -j)
            assert add(-i, j) == sum(-i, j)
            assert add(i, -j) == sum(i, -j)
def test_addition_reasonable():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(6, 7) == 13
    assert add(-6, -7) == -13
    assert add(7, 0) == 7
    print('test addition reasonable')
def test_addition_commutative():
    assert add(-6, 7) == 1
    assert add(7, -6) == 1
    print('test addition commutative')
def test_tax_calculation_pesticised():
    assert calculate_tax_with_bug(1000) == 150
    assert calculate_tax_with_bug(100) == 15
    assert calculate_tax_with_bug(10) == 1.5
    assert calculate_tax_with_bug(1) == 0.15
    assert calculate_tax_with_bug(0) == 0.
    print('test tax calculation pesticised')
def test_tax_calculation():
    assert calculate_tax_with_bug(1000) == 150
    assert calculate_tax_with_bug(100) == 15
    assert calculate_tax_with_bug(10) == 1.5
    assert calculate_tax_with_bug(1) == 0.15
    assert calculate_tax_with_bug(0) == 0.
    print('test tax calculation')
if __name__ == '__main__':
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()
    #test_addition_overcomplicated()
    test_addition_reasonable()
    test_addition_commutative()
    test_tax_calculation_pesticised()
    test_tax_calculation()