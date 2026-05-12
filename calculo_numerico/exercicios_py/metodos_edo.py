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

def heun(f, u0, t0, tf, h):
    """
    improved euler's method (or Heun's method) to approximate solution u(t) of an ordinary differential equation du/dt = f(t, u)

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
        k1 = f(t[k], u[k])
        k2 = f(t[k+1], u[k] + h * k1)
        u[k+1] = u[k] + (h/2) * (k1 + k2)
    return t, u

def rk4(f, u0, t0, tf, h):
    """
    classic Runge-Kutta method to approximate solution u(t) of an ordinary differential equation du/dt = f(t, u)

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
        k1 = f(t[k], u[k])
        k2 = f(t[k] + h/2, u[k] + (h/2) * k1)
        k3 = f(t[k] + h/2, u[k] + (h/2) * k2)
        k4 = f(t[k+1], u[k] + h * k3)
        u[k+1] = u[k] + (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return t, u