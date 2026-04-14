import numpy as np

def euler_melhorado_sistema(f, u0, t0, tf, h):
    """
    improved euler's method (or Heun's method) to approximate solution vector u(t) of a system of ODEs

    input:
        f: derivative of u(t) wrt time
        u0: initial condition (vector)
        t0: start of time interval
        tf: end of time interval
        h: step size
    output:
        t: ndarray (tf-t0)/h
        u: ndarray (u(t_n))
    """
    n = int(tf-t0/h)
    t = np.linspace(t0, tf, n+1) # initialize time vector with n+1 elements (or n subintervals)
    u0 = np.array(u0) # initial conditions vector
    m = u0.size # number of dependent variables
    u = np.zeros((len(t), m)) # one column for each function
    u[0] = u0

    for k in range(0, len(t) - 1):
        k1 = f(t[k], u[k]) # f must be an m x 1 array
        k2 = f(t[k+1], u[k] + h * k1)
        u[k+1] = u[k] + (h/2) * (k1 + k2)
    return t, u