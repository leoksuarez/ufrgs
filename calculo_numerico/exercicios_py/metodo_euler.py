# %%
import numpy as np

def euler(f, u0, t0, tf, h):
    """
    euler's method to approximate solution u(t) of an ordinary differential equation du/dt = f(t, u)

    input:
        f: derivative of u(t) wrt time
        u0: initial condition
        t0: start of time interval
        tf: end of time interval
        h: step size
    output:
        t: ndarray (tf-t0)/h
        u: ndarray (u(t_n))
    """
    n = int((tf-t0)/h)
    t = np.linspace(t0, tf, n+1) # create time vector with n+1 elements (or n subintervals)
    u = np.zeros(len(t)) # start solution vector
    u[0] = u0 # set initial condition

    for k in range(0, len(t) - 1):
        u[k+1] = u[k] + h * f(t[k], u[k])
    return t, u
# %%
