import sympy as sy

u = sy.Symbol('u')
v = sy.Symbol('v')

def hyperboloid():
    
    x = 4*(u**2+10)**0.5*sy.cos(v)
    y = 4*(u**2+10)**0.5*sy.sin(v)
    z = 8*u
    sy.plotting.plot3d_parametric_surface(x, y, z, (u, -10, 10), (v, 0, 2*sy.pi))
    

def sphere():
    
    x = 5*sy.cos(u)*sy.sin(v)
    y = 5*sy.sin(u)*sy.sin(v)
    z = 5*sy.cos(v)
    sy.plotting.plot3d_parametric_surface(x, y, z, (u, -sy.pi, sy.pi), (v, 0, 2*sy.pi))

    

def cone():
    x = 5*u*sy.cos(v)
    y = 5*u*sy.sin(v)
    z = -10*(u-10)
    sy.plotting.plot3d_parametric_surface(x, y, z, (u, 0, 10), (v, 0, 2*sy.pi))
    

functions = [hyperboloid, sphere, cone]

for function in functions:
    function()
