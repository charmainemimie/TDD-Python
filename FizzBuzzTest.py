import pytest


# Test1
# start by writing a failing test(fizzbuzz fct doesn't exist
# def test_canCallFizzBuzz():
#     FizzBuzz(1)

# write a passing test
# production code
def fizzBuzz(value):
    if isMultiple(value, 5):
        if isMultiple(value, 3):
            return "FizzBuzz"
    if isMultiple(value, 3):
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)


# utility fct1
def isMultiple(value, mod):
    return (value % mod) == 0


# utility fct2 to be used for some tests
def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal


# def test_canCallFizzBuzz():
#     fizzBuzz(1)
#
#
# # Test2
# # start by writing a failing test
# # passing test achieved by returning "1" in fizzbuzz fct
# def test_returns1With1Passed():
#     retVal = fizzBuzz(1)
#     assert retVal == "1"
#
#
# # Test3
# # start by writing a failing test
# # passing test achieved by generalizing the returned value into a string in fizzbuzz fct
# def test_returns2With2Passed():
#     retVal = fizzBuzz(2)
#     assert retVal == "2"


# using utility fct
# test 1
def test_returns1With1Passed():
    checkFizzBuzz(1, "1")


# test 2
def test_returns2With2Passed():
    checkFizzBuzz(2, "2")


# test 3
def test_returnsFizzWith3Passed():
    checkFizzBuzz(3, "Fizz")

# test 4
def test_returnsBuzzWith5Passed():
    checkFizzBuzz(5, "Buzz")

# test 5
def test_returnsFizzWith6Passed():
    checkFizzBuzz(6, "Fizz")

# test 6
def test_returnsBuzzWith10Passed():
    checkFizzBuzz(10, "Buzz")

# test 7
def test_returnsFizzBuzzWith15Passed():
    checkFizzBuzz(15, "FizzBuzz")
