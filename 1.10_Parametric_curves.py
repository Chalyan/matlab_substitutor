import sympy as sy

t = sy.Symbol('t')

def spiral():
    
    x = t*sy.cos(t)
    y = t*sy.sin(t)
    
    sy.plotting.plot_parametric(x, y, (t, 0, 10*sy.pi))

def butterfly():

    x = sy.sin(t)*(sy.E**sy.cos(t) - 2*sy.cos(4*t) - sy.sin(t/12)**5)
    y = sy.cos(t)*(sy.E**sy.cos(t) - 2*sy.cos(4*t) - sy.sin(t/12)**5)
    
    sy.plotting.plot_parametric(x, y, (t, 0, 12*sy.pi))

def astroid():

    x = 4*sy.cos(t)**3
    y = 4*sy.sin(t)**3

    sy.plotting.plot_parametric(x, y, (t, 0, 16))

functions = [spiral, butterfly, astroid]

for function in functions:
    function()
