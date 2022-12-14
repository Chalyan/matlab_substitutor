import numpy as np


def isConvergent(matrix: np.matrix):
    diag = np.abs(matrix.diagonal())
    off_diag = np.sum(np.abs(matrix), axis=1).flatten() - diag

    return np.all(diag > off_diag)


def read_inputs():
    x1 = float(input("Please input initial value of the first variable: "))
    x2 = float(input("Please input initial value of the second variable: "))
    x3 = float(input("Please input initial value of the third variable: "))
    epsilion = float(input("Please input the value of error: "))

    return (x1, x2, x3, epsilion)


def calculate_solutions(old_xs, epsilion, k, y, A, _x1, _x2, _x3):
    x1 = (y[0] - A.item(0, 1) * _x2 - A.item(0, 2) * _x3) / A.item(0, 0)
    x2 = (y[1] - A.item(1, 0) * _x1 - A.item(1, 2) * _x3) / A.item(1, 1)
    x3 = (y[2] - A.item(2, 0) * _x1 - A.item(2, 1) * _x2) / A.item(2, 2)

    x = np.array([x1, x2, x3])

    if np.sqrt(np.dot(x - old_xs, x - old_xs)) < epsilion:
        print(
            f"Found solution in {k} iterations, and the solutions are: \n {x}")
    else:
        calculate_solutions(x, epsilion, k + 1, y, A, x1, x2, x3)


bound_variables = np.matrix([[7, 0, 0],
                             [-2, -8, 5],
                             [3, 5, 10]])

free_members = np.array([14, 5, -8])

if isConvergent(bound_variables):
    (x1, x2, x3, epsilion) = read_inputs()
    initial_xs = np.array([x1, x2, x3])

    calculate_solutions(initial_xs, epsilion, 1,
                        free_members, bound_variables, x1, x2, x3)
else:
    print("Matrix is not diagonally dominant")
