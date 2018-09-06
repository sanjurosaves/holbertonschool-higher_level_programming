#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for e in l:
            if e is not l[len(l) - 1]:
                print('{:d}'.format(e), end=" ")
            else:
                print('{:d}'.format(e), end="")
        print()
