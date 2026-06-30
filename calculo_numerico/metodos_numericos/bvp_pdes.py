
def poisson_sor(n, m, x_bounds, y_bounds, f, boundary, omega=1.0, tol=1e-5, maxiter=100):
    """
    Solves the 2D Poisson equation using finite differences and the Successive Over-Relaxation (SOR) method.

    Parameters
    ----------
    n : int
        Number of subintervals in the x-direction.
    m : int
        Number of subintervals in the y-direction.
    x_bounds : np.array
        An array defining the bounds of the x-axis.
    y_bounds : np.array
        An array defining the bounds of the y-axis.
    f : function
        A function that takes two arguments (x, y) and returns the value of f(x, y).
    boundary : dict
        A dictionary specifying the boundary conditions with keys 'left', 'right', 'top', 'bottom' and corresponding values for each boundary.
    tol : float, optional
        The tolerance for convergence. Default is 1e-5.
    maxiter : int, optional
        The maximum number of iterations. Default is 2000.

    Returns
    -------
    w : 2D numpy array
        The solution to the Poisson equation on the grid defined by x_bounds and y_bounds.
    """
    import numpy as np

    # grid setup
    x_min, x_max = x_bounds[0], x_bounds[1]
    y_min, y_max = y_bounds[0], y_bounds[1]
    
    h = (x_max - x_min) / n
    k = (y_max - y_min) / m

    # create grid points
    x = np.linspace(x_min, x_max, n + 1)
    y = np.linspace(y_min, y_max, m + 1)

    # precompute constants for the SOR update
    lambda_sq = (h / k) ** 2
    mu = 2 * (1 + lambda_sq)

    # initialize solution array
    w = np.zeros((n + 1, m + 1))

    # apply boundary conditions
    w[0, :] = boundary['left']
    w[-1, :] = boundary['right']
    w[:, 0] = boundary['bottom']
    w[:, -1] = boundary['top']

    # pre-evaluate f on the grid
    f_values = np.zeros((n + 1, m + 1))
    for i in range(n + 1):
        for j in range(m + 1):
            f_values[i, j] = f(x[i], y[j])

    # SOR iteration
    for it in range(maxiter):
        max_diff = 0.0
        # sweep left to right, top to bottom
        for j in range(m - 1, 0, -1):
            for i in range(1, n):
                old_value = w[i, j] # store old value for convergence check
                
                # standard 5-point stencil
                source = - (h**2) * f_values[i, j]
                neighbors = w[i + 1, j] + w[i - 1, j] + lambda_sq * (w[i, j + 1] + w[i, j - 1])
                w[i, j] = (1 - omega) * w[i, j] + omega * (source + neighbors) / mu

                # compute the infinity norm of the error for convergence check
                diff = abs(w[i, j] - old_value)
                if diff > max_diff:
                    max_diff = diff
        # check for convergence on the current iteration
        if max_diff < tol:
            print(f'Converged after {it + 1} iterations with max difference {max_diff:.2e}.')
            break
    else:
        print(f'Failed to converge after {maxiter} iterations with max difference {max_diff:.2e}.')

    return w

def heat_backward_sor(m, N, x_bounds, t_bounds, alpha, boundary, initial, omega=1.0, tol=1e-5, maxiter=100):
    """
    Solves the 1D heat equation using the backward-difference method and Successive Over-Relaxation (SOR) for the resulting linear system at each time step.

    Parameters
    ----------
    m : int
        Number of subintervals in the spatial direction.
    N : int
        Number of subintervals in the time direction.
    x_bounds : np.array
        An array defining the bounds of the spatial axis.
    t_bounds : np.array
        An array defining the bounds of the time axis.
    alpha : float
        The thermal diffusivity.
    boundary : dict
        A dictionary specifying the boundary conditions with keys 'left', 'right' and corresponding values for each boundary.
    initial : function
        A function that takes one argument (x) and returns the initial temperature distribution.
    tol : float, optional
        The tolerance for convergence. Default is 1e-5.
    maxiter : int, optional
        The maximum number of iterations. Default is 100.

    Returns
    -------
    w : 2D numpy array
        The solution to the heat equation on the grid defined by x_bounds and t_bounds.
    """
    import numpy as np

    # grid setup
    x_min, x_max = x_bounds[0], x_bounds[1]
    t_min, t_max = t_bounds[0], t_bounds[1]
    h = (x_max - x_min) / m
    k = (t_max - t_min) / N

    # create grid points
    x = np.linspace(x_min, x_max, m + 1)
    t = np.linspace(t_min, t_max, N + 1)

    # precompute constant for the SOR update
    lmbda = alpha**2 * k / h**2

    # initialize solution array
    w = np.zeros((m + 1, N + 1))

    # apply initial condition
    for i in range(m + 1):
        w[i, 0] = initial(x[i])

    # apply boundary conditions
    w[0, :] = boundary['left']
    w[-1, :] = boundary['right']

    # SOR iteration for each time step
    for j in range(1, N):
        # solve the linear system for time step j using SOR
        for it in range(maxiter):
            max_diff = 0.0
            for i in range(1, m):
                old_value = w[i, j] # store old value for convergence check
                
                # backward difference in time and central difference in space
                rhs = w[i, j - 1]
                neighbors = lmbda * (w[i + 1, j] + w[i - 1, j])
                w[i, j] = (1 - omega) * w[i, j] + omega * (rhs + neighbors) / (1 + 2 * lmbda)

                # compute the infinity norm of the error for convergence check
                diff = abs(w[i, j] - old_value)
                if diff > max_diff:
                    max_diff = diff
            # check for convergence on the current iteration
            if max_diff < tol:
                print(f'Time step {j}: Converged after {it + 1} iterations with max difference {max_diff:.2e}.')
                break
        else:
            print(f'Time step {j}: Failed to converge after {maxiter} iterations with max difference {max_diff:.2e}.')
    return w

def heat_backward_crout(m, N, x_bounds, t_bounds, alpha, boundary, initial):
    """
    Solves the 1D heat equation using the backward-difference method and Crout's method for LU decomposition to solve the resulting linear system at each time step.

    Parameters
    ----------
    m : int
        Number of subintervals in the spatial direction.
    N : int
        Number of subintervals in the time direction.
    x_bounds : np.array
        An array defining the bounds of the spatial axis.
    t_bounds : np.array
        An array defining the bounds of the time axis.
    alpha : float
        The thermal diffusivity.
    boundary : dict
        A dictionary specifying the boundary conditions with keys 'left', 'right' and corresponding values for each boundary.
    initial : function
        A function that takes one argument (x) and returns the initial temperature distribution.

    Returns
    -------
    w : 1D numpy array
        The solution to the heat equation on the grid defined by x_bounds and t_bounds.
    """
    import numpy as np

    # grid setup
    x_min, x_max = x_bounds[0], x_bounds[1]
    t_min, t_max = t_bounds[0], t_bounds[1]
    h = (x_max - x_min) / m
    k = (t_max - t_min) / N

    # create grid points
    x = np.linspace(x_min, x_max, m + 1)
    t = np.linspace(t_min, t_max, N + 1)

    # precompute constant for the Crout update
    lmbda = alpha**2 * k / h**2

    # initialize solution array
    w = np.zeros(m + 1)
    w[0] = boundary['left'][0]
    w[-1] = boundary['right'][0]
    w[1:-1] = initial(x[1:-1]) # apply initial condition to interior points

    # initialize the tridiagonal matrix coefficients for the linear system at each time step
    d = np.full(m - 1, 1 + 2 * lmbda) # diagonal
    c = np.full(m - 1, -lmbda) # sub-diagonal
    e = np.full(m - 1, -lmbda) # super-diagonal
    
    # perform LU decomposition once since the matrix is constant for all time steps
    # l_c (sub-diagonal of L) is just c, and u_d (diagonal of U) is all 1's for Crout's method
    l_d = np.zeros(m - 1) # diagonal of L
    u_e = np.zeros(m - 1) # super-diagonal of U

    # compute L and U elements for the tridiagonal matrix
    l_d[0] = d[0]
    u_e[0] = e[0] / l_d[0]

    for i in range(1, m - 1):
        l_d[i] = d[i] - c[i - 1] * u_e[i - 1] # diagonal of L
        u_e[i] = e[i] / l_d[i] # super-diagonal of U
    
    l_d[-1] = d[-1] - c[-2] * u_e[-2] # last diagonal of L

    # time-stepping loop
    for j in range(1, N + 1):
        # set up the right-hand side for the linear system at time step j
        b = np.copy(w[1:-1]) # interior points from previous time step
        b[0] += lmbda * w[0] # add contribution from left boundary
        b[-1] += lmbda * w[-1] # add contribution from right boundary

        z = np.zeros(m - 1) # right-hand side for the linear system at time step j excluding boundaries
        z[0] = b[0] / l_d[0] # first element of z after forward substitution

        for i in range(1, m - 1):
            z[i] = (b[i] - c[i - 1] * z[i - 1]) / l_d[i] # forward substitution for z
        
        # solve Uw = z by back substitution
        w[m - 1] = z[m - 2] # w_m-1 is the last element of w before the right boundary
        for i in range(m - 3, -1, -1):
            w[i + 1] = z[i] - u_e[i] * w[i + 2] # back substitution for w

    return w

def heat_cn_crout(m, N, x_bounds, t_bounds, alpha, boundary, initial):
    """
    Solves the 1D heat equation using the Crank-Nicholson method and Crout's method for LU decomposition to solve the resulting linear system at each time step.

    Parameters
    ----------
    m : int
        Number of subintervals in the spatial direction.
    N : int
        Number of subintervals in the time direction.
    x_bounds : np.array
        An array defining the bounds of the spatial axis.
    t_bounds : np.array
        An array defining the bounds of the time axis.
    alpha : float
        The thermal diffusivity.
    boundary : dict
        A dictionary specifying the boundary conditions with keys 'left', 'right' and corresponding values for each boundary.
    initial : function
        A function that takes one argument (x) and returns the initial temperature distribution.

    Returns
    -------
    w : 1D numpy array
        The solution to the heat equation on the grid defined by x_bounds and t_bounds.
    """
    import numpy as np

    # grid setup
    x_min, x_max = x_bounds[0], x_bounds[1]
    t_min, t_max = t_bounds[0], t_bounds[1]

    h = (x_max - x_min) / m
    k = (t_max - t_min) / N

    # create grid points
    x = np.linspace(x_min, x_max, m + 1)
    t = np.linspace(t_min, t_max, N + 1)

    # precompute constant for the Crout update
    lmbda = alpha**2 * k / (h**2)

    # initialize solution array
    w = np.zeros(m + 1)
    w[0] = boundary['left'][0]
    w[-1] = boundary['right'][0]
    w[1:-1] = initial(x[1:-1]) # apply initial condition to interior points

    # initialize the tridiagonal matrix coefficients for the linear system at each time step
    d = np.full(m - 1, 1 + lmbda) # diagonal
    c = np.full(m - 1, -lmbda / 2) # sub-diagonal
    e = np.full(m - 1, -lmbda / 2) # super-diagonal

    # perform LU decomposition once since the matrix is constant for all time steps
    l_d = np.zeros(m - 1) # diagonal of L
    u_e = np.zeros(m - 1) # super-diagonal of U

    l_d[0] = d[0]
    u_e[0] = e[0] / l_d[0]

    for i in range(1, m - 1):
        l_d[i] = d[i] - c[i - 1] * u_e[i - 1] # diagonal of L
        u_e[i] = e[i] / l_d[i] # super-diagonal of U

    l_d[-1] = d[-1] - c[-2] * u_e[-2] # last diagonal of L

    # time-stepping loop
    for j in range(1, N + 1):
        # set up the right-hand side for the linear system at time step j
        b = np.copy(w[1:-1]) # interior points from previous time step
        b[0] += (lmbda / 2) * w[0] # add contribution from left boundary
        b[-1] += (lmbda / 2) * w[-1] # add contribution from right boundary

        z = np.zeros(m - 1) # right-hand side for the linear system at time step j
        z[0] = (b[0] + (1 - lmbda / 2) * b[1] + (lmbda / 2) * b[2]) / l_d[0] # first element of z after forward substitution

        for i in range(1, m - 1):
            z[i] = ((1 - lmbda) * b[i] + (lmbda / 2) * (b[i - 1] + b[i + 1]) + z[i - 1]) / l_d[i] # forward substitution for z
        
        # solve Uw = z by back substitution
        w[m - 1] = z[m - 2] # w_m-1 is the last element of w before the right boundary
        for i in range(m - 3, -1, -1):
            w[i + 1] = z[i] - u_e[i] * w[i + 2] # back substitution for w

    return w

def wave(m, N, x_bounds, t_bounds, alpha, boundary, initial):
    """
    Solves the 1D wave equation using finite differences.

    Parameters
    ----------
    m : int
        Number of subintervals in the spatial direction.
    N : int
        Number of subintervals in the time direction.
    x_bounds : np.array
        An array defining the bounds of the spatial axis.
    t_bounds : np.array
        An array defining the bounds of the time axis.
    alpha : float
        The wave speed.
    boundary : dict
        A dictionary specifying the boundary conditions with keys 'left', 'right' and corresponding values for each boundary.
    initial : dict
        A dictionary specifying the initial conditions with keys 'u0' and 'u1' for the initial displacement and initial velocity, respectively.

    Returns
    -------
    w : 2D numpy array
        The solution to the wave equation on the grid defined by x_bounds and t_bounds.
    """
    import numpy as np

    # grid setup
    x_min, x_max = x_bounds[0], x_bounds[1]
    t_min, t_max = t_bounds[0], t_bounds[1]
    h = (x_max - x_min) / m
    k = (t_max - t_min) / N

    # create grid points
    x = np.linspace(x_min, x_max, m + 1)
    t = np.linspace(t_min, t_max, N + 1)

    # precompute constant for the update
    lmbda = (alpha * k / h)

    # initialize solution array
    w = np.zeros((m + 1, N + 1))

    # apply initial condition
    for i in range(m + 1):
        w[i, 0] = initial['u0'](x[i])

    # apply boundary conditions at all time steps
    w[0, :] = boundary['left']
    w[-1, :] = boundary['right']

    # compute the first time step using the initial derivative
    for i in range(1, m):
        w[i, 1] = (1 - lmbda**2) * w[i, 0] + (lmbda**2 / 2) * (w[i + 1, 0] + w[i - 1, 0]) + k * initial['u1'](x[i])

    # time-stepping loop for subsequent time steps
    for j in range(1, N):
        for i in range(1, m):
            w[i, j + 1] = (2 * (1 - lmbda**2) * w[i, j] + lmbda**2 * (w[i + 1, j] + w[i - 1, j]) - w[i, j - 1])

    return w