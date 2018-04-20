#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = [[e ** 2 for e in row] for row in matrix]
    return squares
