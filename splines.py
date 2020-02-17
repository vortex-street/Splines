from fun import gauss_jordan, find_col, row_swap
import numpy as np


def quadratic_spline(x, y):
    n = len(x) - 1
    row = 0
    A = np.zeros([3 * n, 3 * n])
    b = np.zeros([3 * n, 1])

    def fill_A(col, value):
        A[row, find_col(col, 2)] = value
        return A

    # Function value at interior knots must equal the function value found using the quadratic function
    for i in np.arange(1, n):
        ai, bi, ci = ['a' + str(i), 'b' + str(i), 'c' + str(i)]
        A = fill_A(ai, 1)
        A = fill_A(bi, x[i])
        A = fill_A(ci, x[i] ** 2)
        b[row, 0] = y[i]
        row += 1
        ai, bi, ci = ['a' + str(i + 1), 'b' + str(i + 1), 'c' + str(i + 1)]
        A = fill_A(ai, 1)
        A = fill_A(bi, x[i])
        A = fill_A(ci, x[i] ** 2)
        b[row, 0] = y[i]
        row += 1

    # First and last functions must pass through the endpoints
    a1, b1, c1 = ['a' + str(1), 'b' + str(1), 'c' + str(1)]
    A = fill_A(a1, 1)
    A = fill_A(b1, x[0])
    A = fill_A(c1, x[0] ** 2)
    b[row, 0] = y[0]
    row += 1
    an, bn, cn = ['a' + str(n), 'b' + str(n), 'c' + str(n)]
    A = fill_A(an, 1)
    A = fill_A(bn, x[n])
    A = fill_A(cn, x[n] ** 2)
    b[row, 0] = y[n]
    row += 1

    # Slope at interior knots must be continuous
    for i in range(1, n):
        bi, ci = ['b' + str(i), 'c' + str(i)]
        A = fill_A(bi, 1)
        A = fill_A(ci, 2 * x[i])
        bi, ci = ['b' + str(i + 1), 'c' + str(i + 1)]
        A = fill_A(bi, -1)
        A = fill_A(ci, -2 * x[i])
        row += 1

    # Last spline is linear
    fill_A(cn, 1)

    C = np.hstack([A, b])
    C = row_swap(C)
    x = gauss_jordan(C)
    return x


def cubic_spline(x, y):
    n = len(x) - 1
    row = 0
    A = np.zeros([4 * n, 4 * n])
    b = np.zeros([4 * n, 1])

    def fill_A(col, value):
        A[row, find_col(col, 3)] = value
        return A

    # Function value at interior knots must equal the function value found using the quadratic function
    for i in np.arange(1, n):
        ai, bi, ci, di = ['a' + str(i), 'b' + str(i), 'c' + str(i), 'd' + str(i)]
        A = fill_A(ai, 1)
        A = fill_A(bi, x[i])
        A = fill_A(ci, x[i] ** 2)
        A = fill_A(di, x[i] ** 3)
        b[row, 0] = y[i]
        row += 1
        ai, bi, ci, di = ['a' + str(i + 1), 'b' + str(i + 1), 'c' + str(i + 1), 'd' + str(i + 1)]
        A = fill_A(ai, 1)
        A = fill_A(bi, x[i])
        A = fill_A(ci, x[i] ** 2)
        A = fill_A(di, x[i] ** 3)
        b[row, 0] = y[i]
        row += 1

    # First and last functions must pass through the endpoints
    a1, b1, c1, d1 = ['a' + str(1), 'b' + str(1), 'c' + str(1), 'd' + str(1)]
    A = fill_A(a1, 1)
    A = fill_A(b1, x[0])
    A = fill_A(c1, x[0] ** 2)
    A = fill_A(d1, x[0] ** 3)
    b[row, 0] = y[0]
    row += 1
    an, bn, cn, dn = ['a' + str(n), 'b' + str(n), 'c' + str(n), 'd' + str(n)]
    A = fill_A(an, 1)
    A = fill_A(bn, x[n])
    A = fill_A(cn, x[n] ** 2)
    A = fill_A(dn, x[n] ** 3)
    b[row, 0] = y[n]
    row += 1

    # Slope at interior knots must be continuous
    for i in range(1, n):
        bi, ci, di = ['b' + str(i), 'c' + str(i), 'd' + str(i)]
        A = fill_A(bi, 1)
        A = fill_A(ci, 2 * x[i])
        A = fill_A(di, 3 * x[i] ** 2)
        bi, ci, di = ['b' + str(i + 1), 'c' + str(i + 1), 'd' + str(i + 1)]
        A = fill_A(bi, -1)
        A = fill_A(ci, -2 * x[i])
        A = fill_A(di, -3 * x[i] ** 2)
        row += 1

    # Second derivative at interior knots must be continuous
    for i in range(1, n):
        ci, di = ['c' + str(i), 'd' + str(i)]
        A = fill_A(ci, 2)
        A = fill_A(di, 6 * x[i])
        ci, di = ['c' + str(i + 1), 'd' + str(i + 1)]
        A = fill_A(ci, -2)
        A = fill_A(di, -6 * x[i])
        row += 1

    # First and last splines are quadratic
    fill_A(d1, 1)
    row += 1
    fill_A(dn, 1)

    C = np.hstack([A, b])
    C = row_swap(C)
    x = gauss_jordan(C)
    return x
