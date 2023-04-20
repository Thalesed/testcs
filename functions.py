from math import cos

def f(x):
    if x == 0:
        return None
    return 10/x

def g(x):
    return x**3 + x**2 - x + 1

def h(x):
    return (x**2)/3 - x + 2

def a(x):
    return cos(x)

def j(x):
    if x < -20:
        return -x - 10
    elif x in [-20, 6, 25]:
        return None
    elif x > 6 and x < 25:
        return x**2/10
    else:
        return -(x**2/13) -x + 7

zeta = [(f, 'red'), (g, 'green'), (h, 'blue'), (a, 'yellow'), (j, 'purple')]

