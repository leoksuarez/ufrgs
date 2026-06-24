A1 = [4 -1 0; -1 4 -1; 0 -1 4];
A2 = [-1 0 0; 0 -1 0; 0 0 -1];
A = [A1 A2; A2 A1];
b = [1 0 0 0 0 0]';
x0 = [0 0 0 0 0 0]';
tol = 10^-6;
maxiter = 100;
omega = 1.1;

// solve Ax=b with Jacobi, Gauss-Seidel, and SOR methods
[x_j, k_j, relresid_j] = jacobi(A, b, x0, tol, maxiter)
[x_g, k_g, relresid_g] = gauss_seidel(A, b, x0, tol, maxiter)
[x_sor, k_sor, relresid_sor] = sor(A, b, x0, omega, tol, maxiter)
