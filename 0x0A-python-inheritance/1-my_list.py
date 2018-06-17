#!/usr/bin/python3
""" class that inherits from list """


class MyList(list):
    """ class to inherit list """
    def print_sorted(self):
        cpy = MyList(self)
        cpy.sort()
        print(cpy)
