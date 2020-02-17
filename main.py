from splines import quadratic_spline, cubic_spline
import matplotlib.pyplot as plt
from fun import find_col
import xlsxwriter as xl
import numpy as np


# Given points
x = np.array([2.20, 1.70, 1.28, 0.66, 0.00, -0.60, -1.04, -1.20])
y = np.array([0.00, 0.50, 0.88, 1.14, 1.20, 1.04, 0.60, 0.00])
x = np.flip(x)
y = np.flip(y)

# Quadratic spline calculation
constants = quadratic_spline(x, y)

# Quadratic spline plotting
points = 100
for function in range(len(x) - 1):
    x_low = x[function]
    x_high = x[function + 1]
    interval = (x_high - x_low) / points
    x_spline = np.arange(x_low, x_high + interval, interval)
    af, bf, cf = ['a' + str(function + 1), 'b' + str(function + 1), 'c' + str(function + 1)]
    a, b, c = find_col(af, 2), find_col(bf, 2), find_col(cf, 2)
    y_spline = constants[a] + constants[b] * x_spline + constants[c] * x_spline ** 2
    plt.plot(x_spline, y_spline, color='red')
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic spline')
plt.show()

# Quadratic spline constants output
file_out = xl.Workbook("Output.xlsx")
sheet_out = file_out.add_worksheet()
row = 1
col = 0
for col, data in enumerate(constants):
    sheet_out.write(row, col, data)

# Cubic spline calculation
constants = cubic_spline(x, y)

# Cubic spline plotting
points = 100
for function in range(len(x) - 1):
    x_low = x[function]
    x_high = x[function + 1]
    interval = (x_high - x_low) / points
    x_spline = np.arange(x_low, x_high + interval, interval)
    af, bf, cf, df = ['a' + str(function + 1), 'b' + str(function + 1), 'c' + str(function + 1), 'd' + str(function + 1)]
    a, b, c, d = find_col(af, 3), find_col(bf, 3), find_col(cf, 3), find_col(df, 3)
    y_spline = constants[a] + constants[b] * x_spline + constants[c] * x_spline ** 2 + constants[d] * x_spline ** 3
    plt.plot(x_spline, y_spline, color='red')
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic spline')
plt.show()

# Cubic spline constants output
sheet_out2 = file_out.add_worksheet('2')
row = 1
col = 0
for col, data in enumerate(constants):
    sheet_out2.write(row, col, data)
file_out.close()
