#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    num_rows = len(matrix)
    num_colm = len(matrix[0])
    for r in range(0, num_rows):
        for c in range(0, num_colm):
            if c == num_colm - 1:
                print('{:d}'.format(matrix([r][c])), end = '')
            else:
                print('{:d}'.format(matrix([r][c])), end = ' ')
        print()
