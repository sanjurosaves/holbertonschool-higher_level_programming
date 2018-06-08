#!/usr/bin/python3
""" creates Rectangle class, inheriting from Base """

from models.base import Base

class Rectangle(Base):
    """ Rectangle inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiate rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """ getter for width """
            return self.__width

        @width.setter
        def width(self, value):
            """ setter for width """
            self.__width = value

        @property
        def height(self):
            """ getter for height """
            return self.__height

        @height.setter
        def height(self, value):
            """ setter for height """
            self.__height = value

        @property
        def x(self):
            """ getter for x """
            return self.__x

        @x.setter
        def x(self, value):
            """ setter for x """
            self.__x = x

        @property
        def y(self):
            """ getter for y """
            return self.__y

        @y.setter
        def y(self, value):
            """ setter for y """
            self.__y = y
