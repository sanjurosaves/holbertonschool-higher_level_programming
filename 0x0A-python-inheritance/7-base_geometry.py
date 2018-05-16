#!/usr/bin/python3

"""creates empty class BaseGeometry"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """ raises exception for unimplemented area function """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
