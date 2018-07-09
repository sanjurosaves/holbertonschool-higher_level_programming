#!/usr/bin/python3
""" module for function add_attribute """


def add_attribute(clsname, attr, val):
    """ function to add attribute """
    if hasattr(clsname, '__dict__'):
        setattr(clsname, attr, val)
    else:
        raise TypeError('can\'t add new attribute')
