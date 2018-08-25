#!/usr/bin/python3
''' module for print_square method '''


def print_square(size):
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for l in range(size):
        for q in range(size):
            print('#', end='')
        print()
