import numpy as np

def bisection(f, a, b, tol, nmax):
    i = 0
    while (i <= nmax):
        p = (b+a) / 2
        if f(p) == 0 or np.abs((b-a) / 2) < tol:
            return p, i
        elif np.sign(f(a)) * np.sign(f(p)) < 0:
            b = p
        else:
            a = p
        i += 1
    raise NameError('maximum number of iterations exceeded')
