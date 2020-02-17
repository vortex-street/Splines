import random as rd
import numpy as np


def gauss_jordan(c):
    c_old = c.copy()
    n = c.shape[0]
    for k in range(n):
        for j in range(k, n + 1):
            c[k, j] = c_old[k, j] / c_old[k, k]
        for j in range(k, n + 1):
            for i in range(n):
                if i == k:
                    c[i, j] = c[i, j]
                else:
                    c[i, j] = c_old[i, j] - c_old[i, k] * c[k, j]
        c_old = c.copy()
    x = c[:, n]
    return x


def row_swap(c):
    n = np.shape(c)[0]
    while 0 in np.diag(c):
        for diagonal in range(n):
            col = c[:, diagonal]
            nonz = np.nonzero(col)
            length = np.shape(nonz)[1]
            if c[diagonal, diagonal] == 0:
                row1 = rd.choice(nonz)[rd.randint(0, length - 1)]
                row2 = diagonal
                c[[row1, row2]] = c[[row2, row1]]
    return c


def find_col(constant, poly):
    if constant[0] == 'a':
        col = (poly + 1) * int(constant[-1]) - (poly + 1)
    elif constant[0] == 'b':
        col = (poly + 1) * int(constant[-1]) - poly
    elif constant[0] == 'c':
        col = (poly + 1) * int(constant[-1]) - (poly - 1)
    elif constant[0] == 'd':
        col = (poly + 1) * int(constant[-1]) - (poly - 2)
    return col
