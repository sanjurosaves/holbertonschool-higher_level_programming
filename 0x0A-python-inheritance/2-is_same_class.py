#!/usr/bin/python3

"""checks if an object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object
        a_class: class
    Return:
        True: if it is an instance of the given class
        False: not an instance of the given class
    """
    return (type(obj) == a_class)
