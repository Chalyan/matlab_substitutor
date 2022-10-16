import sympy as sp

x = sp.Symbol('x')
f = x**5
df = sp.diff(f)
d2f = sp.diff(df)
d3f = sp.diff(d2f)
y = 1
print("The function and its derivatves.")
print("Main function: ", f, ", and its value at point x=2: ", f.subs(x, y))
print("First derivative: ", df, ", and its value at point x=2: ", df.subs(x, y))
print("Second derivative: ", d2f, ", and its value at point x=2: ", d2f.subs(x, y))
print("Third derivative: ", d3f, ", and its value at point x=2: ", d3f.subs(x, y))
