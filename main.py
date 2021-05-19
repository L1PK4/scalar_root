import numpy as np
from binary import solve

def getf(msg):
    return eval("lambda x : " + input(msg))

def main():
    f = getf('Enter f(x) = ')
    a, b, eps = tuple(map(float, input('Enter a, b: ').split()))
    dot, val = solve(f, a, b, eps)
    print(f"f({dot}) = {val}")

if __name__ == "__main__":
    main()