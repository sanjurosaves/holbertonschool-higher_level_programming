#!/usr/bin/python3
''' module for add_integer function '''


def add_integer(a, b=98):
    '''
    returns the sum of two integers
    Args:
        a (float, int): first integer
        b (float, int): second integer
    Returns:
        sum of two numbers.
    '''
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return (a + b)
