import sympy as sy

def f(x):
    return x**2
  
x = sy.Symbol("x")
print(sy.integrate(f(x), (x, 1, 2)))
