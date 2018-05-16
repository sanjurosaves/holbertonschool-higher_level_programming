#!/usr/bin/python3

""" class Square that inherits from BaseGeometry class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting rectangle"""
    def __init__(self, size):
        """instantiate Square class with Rectangle integer validators"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return area of square"""
        return self.__size ** 2

    def __str__(self):
        """return string representation to print"""
        return "[Square] {}/{}".format(self.__size, self.__size)
