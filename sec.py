from numpy import fabs

def solve(f, a, b, eps):
    A, B = f(a), f(b)
    c = (a * B - b * A) / (B - A)
    C = f(c)
    i = 0
    while True:
        i += 1
        if A * C < 0:
            B, b = C, c
        else:
            A, a = C, c
        if fabs(f(c)) < eps:
            return c, C, i
        c = (a * B - b * A) / (B - A)
        C = f(c)