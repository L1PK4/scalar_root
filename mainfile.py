import numpy as np
from sec import solve

def main():
    o = int(input("Enter num of example: "))
    with open("data.txt", 'rt') as f:
        for _ in range(5 * (o - 1)):
            f.readline()
        f.readline()
        s = f.readline()
        func = lambda x : eval(s)
        a = float(f.readline())
        b = float(f.readline())
        e = float(f.readline())

    x, y, iter = solve(func, a, b, e)
    print(f"Solution:\nx = {x}\nf(x) = {y}\niter = {iter}")
        

if __name__ == "__main__":
    main()