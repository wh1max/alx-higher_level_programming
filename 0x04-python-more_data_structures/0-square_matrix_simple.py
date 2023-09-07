#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    resp = []
    for row in matrix:
        sub_matrix = map(lambda num: num**2, row)
        resp.append(list(sub_matrix))
    return resp
