import numpy as np
from binary import solve as binsolve
from sec import solve as ssolve
from time import time

def getf(msg):
    return eval("lambda x : " + input(msg))

def main():
    f = getf('Enter f(x) = ')
    a, b, eps = tuple(map(float, input('Enter a, b, e: ').split()))
    start = time()
    dot1, val1, i1 = binsolve(f, a, b, eps)
    t1 = time()
    dot2, val2, i2 = ssolve(f, a, b, eps)
    t2 = time()
    print(f"""
Binary res
\tf({dot1}) = {val1}

\tIter = {i1}

\ttime = {t1 - start}

Secant res

\tf({dot2}) = {val2}

\tIter = {i2}

\ttime = {t2 - t1}
    """)

if __name__ == "__main__":
    main()