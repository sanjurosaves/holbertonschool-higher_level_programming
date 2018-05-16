#!/usr/bin/python3

""" class Square that inherits from BaseGeometry class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting rectangle"""
    def __init__(self, size):
        """instantiate Square class with Rectangle integer validators"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
