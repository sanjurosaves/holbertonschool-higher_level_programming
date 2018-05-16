#!/usr/bin/python3

"""checks if the object is an instance of a class that was inherited from
the specified class"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object
        a_class: class
    Return:
        True: if it is an inheritor of the given class
        False: not an inheritor of the given class
    """
    if type(obj) == a_class:
        return(False)
    return issubclass(type(obj), a_class)
