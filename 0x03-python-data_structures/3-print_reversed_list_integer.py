#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list != None:
        my_list.reverse()
        for x in my_list:
            print('{}'.format(x))
