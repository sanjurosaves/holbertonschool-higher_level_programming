#!/usr/bin/python3

""" class rectangle that inherits from BaseGeometry class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting BaseGeometry"""
    def __init__(self, width, height):
        """instantiate Rectangle class with BaseGeometry integer validators"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
