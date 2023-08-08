import pytest
import math
from CalculatorPlus import *

def test_add():
    assert add(-2, 0) == -2
    assert add(-2, -2) == -4
    assert add(2, 2) == 4
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(2, 5) == -3
    assert subtract(5, 5) == -0
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(0, 2) == 0
    assert multiply(2, 3) == 6
    assert multiply(2, -3) == -6
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(10.0, 2.0) == 5.0

def test_division_by_zero():
    with pytest.raises(ValueError):  #this statement is used to test for errors, when the divide() function is called with a denominator of 0.
        divide(10, 0)

def test_square_root():
        assert square_root(16) == 4.0
        assert square_root(25.0) == 5.0
        assert square_root(0) == 0.0

def test_square_root_negative_number():
    with pytest.raises(ValueError):
        square_root(-16)






