#!/usr/bin/python3

""" class that inherits from list """


class MyList(list):
    def print_sorted(self):
        copy = sorted(self)
        print(copy)
