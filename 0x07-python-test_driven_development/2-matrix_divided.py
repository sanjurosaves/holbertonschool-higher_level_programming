#!/usr/bin/python3
''' module for matrix_divide function '''

def deepcopy(obj):
    if hasattr(obj, '__iter__'):
        return type(obj)(deepcopy(item) for item in obj)
    return obj


def matrix_divided(matrix, div):
    '''
    Args:
        matrix: a list of lists of integers or floats
        div: divisor (non-zero integer or float)
    Returns:
        a new matrix showing the quotient of each element and the div
    '''
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    lens = []
    for e in matrix:
        if not isinstance(e, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        lens.append(len(e))
    for e in matrix:
        for le in e:
            if not isinstance (le, (float, int)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    i = 0
    for l in range(lens[0], lens[len(lens) - 1]):
        if l != lens[i + 1]:
            raise TypeError('Each row of the matrix must have the same size')
        i += 1
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    result = deepcopy(matrix)
    for e in range(len(result)):
        for le in range(len(result[e])):
            result[e][le] = round(result[e][le] / div, 2)
    return result
