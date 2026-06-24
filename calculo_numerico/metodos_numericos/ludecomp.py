# %%
def crout(A):
    """
    Compute LU decomposition of a square matrix A using Crout's method.

    Parameters
    ----------
    A : 2D numpy array
        The input square matrix to decompose.

    Returns
    -------
    L : 2D numpy array
        The lower triangular matrix.

    U : 2D numpy array
        The upper triangular matrix with unit diagonal.
    """
    import numpy as np
    A = np.array(A, dtype=float)
    n = A.shape[0]
    L = np.zeros_like(A)
    U = np.eye(n)

    for i in range(n):
        # compute L elements for row i (columns j <= i)
        for j in range(i + 1):
            L[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(j))

        # compute U elements for row i (columns j > i)
        for j in range(i + 1, n):
            U[i, j] = (A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))) / L[i, i] 

    return L, U
# %%
def crout_tridiagonal(d, c, e, b):
    """
    Solve tridiagonal system Ax=b using Crout's method for LU decomposition.

    Parameters
    ----------
    d : 1D numpy array
        The diagonal elements of the tridiagonal matrix.

    c : 1D numpy array
        The sub-diagonal elements of the tridiagonal matrix.

    e : 1D numpy array
        The super-diagonal elements of the tridiagonal matrix.

    b : 1D numpy array
        The right-hand side vector.

    Returns
    -------
    x : 1D numpy array
        The solution vector.
    """
    import numpy as np
    d = np.array(d, dtype=float)
    c = np.array(c, dtype=float)
    e = np.array(e, dtype=float)
    b = np.array(b, dtype=float)
    n = len(d)

    # initialize 1D arrays for L and U elements
    # notice l_c (sub-diagonal of L) is just c, and u_d (diagonal of U) is all 1's
    l_d = np.zeros(n) # diagonal of L
    u_e = np.zeros(n-1) # super-diagonal of U
    z = np.zeros(n)
    
    # set up and solve Lz = b by forward substitution
    l_d[0] = d[0]
    u_e[0] = e[0] / l_d[0]
    z[0] = b[0] / l_d[0]

    # compute L and U elements for rows 1 to n-1
    for i in range(1, n - 1):
        l_d[i] = d[i] - c[i-1] * u_e[i-1] # diagonal of L
        u_e[i] = e[i] / l_d[i] # super-diagonal of U
        z[i] = (b[i] - c[i-1] * z[i-1]) / l_d[i] # forward substitution for z

    l_d[n-1] = d[n-1] - c[n-2] * u_e[n-2] # last diagonal of L
    z[n-1] = (b[n-1] - c[n-2] * z[n-2]) / l_d[n-1] # forward substitution for last element of z

    # solve Ux = z by back substitution
    x = np.zeros(n)
    x[-1] = z[-1] # last element of x
    for i in range(n-2, -1, -1):
        x[i] = z[i] - u_e[i] * x[i+1] # back substitution for x

    return x