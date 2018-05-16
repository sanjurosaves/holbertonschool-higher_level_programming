#!/usr/bin/python3

"""checks if an object is exactly an instance of the specified class,
or if the object is an instance of a class that was inherited from
the specified class"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object
        a_class: class
    Return:
        True: if it is an instance or inheritor of the given class
        False: not an instance of the given class
    """
    return isinstance(obj, a_class)
