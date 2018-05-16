#!/usr/bin/python3

"""creates empty class BaseGeometry"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """ raises exception for unimplemented area function """
        raise Exception("area() is not implemented")
