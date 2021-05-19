from numpy import fabs
def solve(func, a, b, eps):
    c = (a + b) / 2
    A = func(a)
    B = func(b)
    C = func(c)
    while True:
        if A * C < 0:
            B, b = C, c
        else:
            A, a = C, c
        if fabs(b - a) < eps:
            return b, B
        c = (a + b) / 2
        C = func(c)
        
