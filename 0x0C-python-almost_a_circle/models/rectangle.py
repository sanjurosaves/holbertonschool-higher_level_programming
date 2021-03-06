#!/usr/bin/python3
""" creates Rectangle class, inheriting from Base """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class is inherited from Base """

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns rectangle area"""
        return (self.__height * self.__width)

    def display(self):
        """prints rectangle instance to stdout with hash symbols"""
        if (self.__y != 0):
            for z in range(0, self.__y):
                print()
        for x in range(0, self.__height):
            if (self.__x != 0):
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """override __str__ method to return customized string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args is not None and len(args) > 0:
            i = 0
            attributes = ["id", "width", "height", "x", "y"]
            for arg in args:
                setattr(self, attributes[i], args[i])
                i += 1
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return dictionary representation of rectangle """
        rect_dict = {}
        keys = ["id", "width", "height", "x", "y"]
        for key in keys:
            rect_dict[key] = getattr(self, key)
        return rect_dict
