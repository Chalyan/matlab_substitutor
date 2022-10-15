import numpy as np

def isConvergent(A: np.array):
    diag = np.diag(np.abs(A)) 
    off_diag = np.sum(np.abs(A), axis=1) - diag 
    return np.all(diag > off_diag)

# A•x = y
A = np.array([[7, 0, 0], 
              [-2, -8, 5], 
              [3, 5, 10]])

y = np.array([14, 5, -8])

if isConvergent(A):
    x1 = float(input("Please input initial value of the first variable: "))
    x2 = float(input("Please input initial value of the second variable: "))
    x3 = float(input("Please input initial value of the third variable: "))
    epsilion = float(input("Please input the value of error: "))
    x_old = np.array([x1, x2, x3])
    k = 1
    while k>0:
        
        x1 = (y[0]-A[0][1]*x2-A[0][2]*x3)/A[0][0]
        x2 = (y[1]-A[1][0]*x1-A[1][2]*x3)/A[1][1]
        x3 = (y[2]-A[2][0]*x1-A[2][1]*x2)/A[2][2]    
        x = np.array([x1, x2, x3])
        if np.sqrt(np.dot(x-x_old, x-x_old)) < epsilion:
            print("Found solution in ", k, " iterations, and the solutions are: \n", x)
            break
        
        x_old = x
        k+=1
    
else:
    print("Matrix is not diagonally dominant")
