#!/usr/bin/python3

"""Defines an integer addition function."""

def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise typeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
