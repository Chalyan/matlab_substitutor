import sympy as sy

x = sy.Symbol("x")
f = sy.cos(x) + 3*x**2 + x**(-1)
integrated = sy.integrate(f, x)
print(integrated)
