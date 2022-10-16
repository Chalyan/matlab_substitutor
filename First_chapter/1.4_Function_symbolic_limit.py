import sympy as sp

x = sp.Symbol('x')
f = sp.sin(x)/x
print("Function: {}".format(f)) 
f_limit = sp.limit(f, x, 0)
print("Limit of the function, when x tends to 0: {}".format(f_limit)) 
