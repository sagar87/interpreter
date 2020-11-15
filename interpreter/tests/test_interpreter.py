import pytest
from interpreter import Interpreter


def test_single_digit_addition():
    i0 = Interpreter("1+1")
    assert i0.expr() == 2


def test_multiple_digit_addition():
    i0 = Interpreter("14+1")
    assert i0.expr() == 15
    i1 = Interpreter("1+14")
    assert i1.expr() == 15


def test_whitespace():
    i0 = Interpreter("14 +1")
    assert i0.expr() == 15
    i1 = Interpreter("14 + 1")
    assert i1.expr() == 15
    i2 = Interpreter("14 + 1 ")
    assert i2.expr() == 15


def test_subtraction():
    i0 = Interpreter("1-1")
    assert i0.expr() == 0
    i1 = Interpreter("123-1")
    assert i1.expr() == 122
    i2 = Interpreter("123-23")
    assert i2.expr() == 100


def test_multiply():
    i0 = Interpreter("1*1")
    assert i0.expr() == 1
    i1 = Interpreter("2*2")
    assert i1.expr() == 4
    i2 = Interpreter("3*3")
    assert i2.expr() == 9
    i0 = Interpreter("1/1")
    assert i0.expr() == 1
    i1 = Interpreter("8/2")
    assert i1.expr() == 4
    i2 = Interpreter("9/3")
    assert i2.expr() == 3


def test_multiply_and_addition():
    i0 = Interpreter("1*1 + 3")
    assert i0.expr() == 4
    i1 = Interpreter("7-1*5")
    assert i1.expr() == 2

def test_complex_expressions():
    i0 = Interpreter("7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)")
    assert i0.expr() == 10