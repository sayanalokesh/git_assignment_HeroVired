# Test cases for the CalculatorPlus program

This file contains test cases for the CalculatorPlus module. The module provides functions for performing basic mathematical operations, such as addition, subtraction, multiplication, division, and square root.

## Test cases for the add() function

The add() function takes two numbers as input and returns their sum. The following test cases verify that the add() function works correctly:

* `assert add(-2, 0) == -2`
* `assert add(-2, -2) == -4`
* `assert add(2, 2) == 4`
* `assert add(0, 0) == 0`

## Test cases for the subtract() function

The subtract() function takes two numbers as input and returns their difference. The following test cases verify that the subtract() function works correctly:

* `assert subtract(2, 3) == -1`
* `assert subtract(2, 5) == -3`
* `assert subtract(5, 5) == -0`
* `assert subtract(5, 3) == 2`

## Test cases for the multiply() function

The multiply() function takes two numbers as input and returns their product. The following test cases verify that the multiply() function works correctly:

* `assert multiply(0, 2) == 0`
* `assert multiply(2, 3) == 6`
* `assert multiply(2, -3) == -6`
* `assert multiply(-2, -3) == 6`

## Test cases for the divide() function

The divide() function takes two numbers as input and returns their quotient. The following test cases verify that the divide() function works correctly:

* `assert divide(10, 2) == 5`
* `assert divide(-10, 2) == -5`
* `assert divide(10.0, 2.0) == 5.0`

## Test cases for the division by zero error

The divide() function raises a ValueError exception if the denominator is 0. The following test case verifies that the divide() function raises the ValueError exception correctly:

```python
def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


## Test cases for the division by zero error

The square_root() function takes a number as input and returns its square root. The following test cases verify that the square_root() function works correctly:

* `assert square_root(16) == 4.0`
* `assert square_root(25.0) == 5.0`
* `assert square_root(0) == 0.0`

## Test cases for the square root of negative number error

The square_root() function raises a ValueError exception if the number is negative. The following test case verifies that the square_root() function raises the ValueError exception correctly:

python
def test_square_root_negative_number():
    with pytest.raises(ValueError):
        square_root(-16)


The above are just a few examples of test cases that can be used to verify the functionality of the CalculatorPlus program. By writing test cases, you can help to ensure that the module works correctly and that it is free of errors.