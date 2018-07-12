import numpy as np


# data for 200NC battery

# y = np.array([103,
#     # 120,
#     # 132,
#     # 139.6,
#     # 145.5,
#     # 158.4,
#     # 168,
#     178,
#     # 181.4,
#     # 189.6,
#     200])
#
# x = np.array([1,
#     # 2,
#     # 3,
#     # 4,
#     # 5,
#     # 8,
#     # 12,
#     20,
#     # 24,
#     # 48,
#     100])

def create_training_set(x):
    """
    Setup training data for a squre root function. Returns X matrix
    """
    func = ''
    if x.max() <100:
        x2 = np.sqrt(x)
        func = 'sqrt'
    else:
        x2 = np.reciprocal(x)# np.sqrt(x)
        func = 'recip'
    X = np.column_stack([np.ones(len(x)), x, x2])

    return (X, func)



def normal_equation(X, y):
    """
    Apply normal equation to find best fit line for training data. Returns Thetas.
    """

    return np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

def predict(x, theta, func):
    """
    predict outcome for x vector input from theta parameters
    """
    if func == 'sqrt':
        z = np.array([1, x, np.sqrt(x)])#, np.sqrt(c_rate), ])

    elif func == 'recip':
        z = np.array([1, x, np.reciprocal(x)])#, np.sqrt(c_rate), np.sqrt(x)])

    return sum(z*theta)

def predict_from_regression(input, output, predict_value):
    """
    High error possible with low resolution and high spread between points.
    With low max c rate values (ie. > c rate == 100) prediction begins to overshoot.
    * perform check to
    """
    training_set, function = create_training_set(input)
    theta = normal_equation(training_set, output)
    prediction = predict(predict_value, theta, function)
    return prediction
# c_rate = 40
#
# print(predict_from_regression(x, y, c_rate))
#
# z = np.array([1, c_rate, np.sqrt(c_rate)])#, np.sqrt(c_rate), np.reciprocal(c_rate)])
#
# x2 = np.sqrt(x)
# X = np.column_stack([np.ones(len(x)), x, x2])
# norEqu = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y) # returns theta parameters
# norm_predictions = sum((X*norEqu).T)
#
# # A = np.column_stack([x2, x, np.ones(len(x))]) #x2
# # a = np.linalg.lstsq(A, y)
# def make_predicitions(x, a):
#     y_predicitions = []
#     for input in x:
#         y_predicitions.append(round(sum(np.array([np.sqrt(input),input, 1])* a[0])))
#     return y_predicitions
# # y_values = make_predicitions(x, a)
#
# # print('Theta least squared:', a[0])
# print("Theta normal equation:", norEqu)
# print('Known output (y):', y)
# print("Normal Equation - y:", np.rint(norm_predictions)-y)
# # print(np.array(y_values)-y)
# print(sum(z*norEqu))
