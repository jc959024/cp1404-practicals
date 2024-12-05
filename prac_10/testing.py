"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) > length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # The test below should pass now that the function is fixed
    assert repeat_string("hi", 2) == "hi hi"

    # Assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # Test Car's fuel property with a test function
    def test_car_fuel():
        car_with_fuel = Car(fuel=10)
        assert car_with_fuel.fuel == 10, "Initial fuel not set correctly."
        car_without_fuel = Car()
        assert car_without_fuel.fuel == 0, "Default fuel should be 0."

    test_car_fuel()
    print("All tests passed.")


run_tests()

# Uncomment the following line to run doctests
doctest.testmod()


# Fixing the is_long_word function
def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


# Write and test a function to format a phrase as a sentence
def format_phrase(words):
    if words[0].islower():
        words = words[0].upper() + words[1:]
    if words[-1] != ".":
        words += "."
    return words


# Testing the format_phrase function
assert format_phrase('hello') == 'Hello.'
assert format_phrase('It is an ex parrot.') == 'It is an ex parrot.'
assert format_phrase('Cars work.') == 'Cars work.'
