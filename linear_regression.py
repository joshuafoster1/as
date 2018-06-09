
# import matplotlib.pyplot as plt
import numpy as np
# y = b0 + x1*b1 + x2*b2
# x2 = sqr(x1)

# data for 200NC battery

y = np.array([103,
    120,
    132,
    139.6,
    145.5,
    158.4,
    168,
    178,
    181.4,
    189.6,
    200])

x = np.array([1,
    2,
    3,
    4,
    5,
    8,
    12,
    20,
    24,
    48,
    100])
#x2 = np.sqrt(x)
x = np.reciprocal(x)

A = np.column_stack([x2, x, np.ones(len(x))]) #x2
X = np.column_stack([np.ones(len(x)), x, x2])
norEqu = (np.linalg.inv(X.T.dot(X))).dot(X.T).dot(y)

a = np.linalg.lstsq(A, y)
def make_predicitions(x, a):
    y_predicitions = []
    for input in x:
        y_predicitions.append(round(sum(np.array([np.sqrt(input),input, 1])* a[0])))
    return y_predicitions
# y_values = make_predicitions(x, a)

norm_predictions = sum((X*norEqu).T)
print(a[0])
# print(y_values)
print(y)
print(norm_predictions-y)
# print(np.array(y_values)-y)
