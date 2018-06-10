#!/usr/bin/python3
""" creates Square class, inheriting from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class is inherited from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ instantiate square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        self.width = value
        self.height = value

    def __str__(self):
        """override __str__ method to return customized string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """ updates the class by assigning attributes """
        if args is not None and len(args) > 0:
            i = 0
            attributes = ["id", "size", "x", "y"]
            for arg in args:
                setattr(self, attributes[i], args[i])
                i += 1
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return dict representation of a square """
        sq_dict = {}
        keys = ["id", "size", "x", "y"]
        for key in keys:
            sq_dict[key] = getattr(self, key)
        return sq_dict
