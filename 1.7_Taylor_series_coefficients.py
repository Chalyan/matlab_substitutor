import sympy as sp

x = sp.Symbol("x")
function = sp.cos(x)
x0 = float(input("Please input the point, around which the Taylor series will be generated: "))
coefficient_list = []
for i in range(0,6):
    coefficient = sp.diff(function, x, i).subs(x, x0)/sp.factorial(i)
    coefficient_list.append(coefficient)

print(coefficient_list)
