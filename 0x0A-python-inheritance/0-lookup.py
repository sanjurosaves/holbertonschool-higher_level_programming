#!/usr/bin/python3

"""Lookup module: returns list of avail attributes and methods of an object"""


def lookup(obj):
    """
    Args:
        obj: passed object to lookup
    """
    return dir(obj)
