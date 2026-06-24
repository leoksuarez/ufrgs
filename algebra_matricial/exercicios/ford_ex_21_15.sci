function [x, err, iter] = normalsolve(A, b, x0, tol, maxiter)
    // solve Ax=b using the normal equations and the conjugate gradient method
    // A^TA is symmetric, if A has full rank then A^TA is positive definite, if A is well conditioned and it is
    // easy to compute A^T then we can apply CG to the normal equations A^TAx = A^Tb
    // input: matrix A, rhs b, initial guess x0, tolerance tol, and max number of iterations maxiter
    // output: approximate solution x, norm of the residual r, and number of iterations iter
    A = A'*A;
    b = A'*b;
    [x, flag, err, iter, res] = conjgrad(A, b, method='pcg', x0=x0, tol=tol, maxIter=maxiter);
endfunction

R1 = sprand(1000, 1000, 0.03);
R2 = sprand(1500, 1500, 0.05);
R3 = sprand(2000, 2000, 0.2);

[m1, n1] = size(R1);
[m2, n2] = size(R2);
[m3, n3] = size(R3);

b1 = rand(m1, 1);
b2 = rand(m2, 1);
b3 = rand(m3, 1);

x01 = ones(n1, 1);
x02 = ones(n2, 1);
x03 = ones(n3, 1);

tol = 1e-10;
maxiter = 500;

[x1, err1, iter1] = normalsolve(R1, b1, x01, tol, maxiter);
[x2, err2, iter2] = normalsolve(R2, b2, x02, tol, maxiter);
[x3, err3, iter3] = normalsolve(R3, b3, x03, tol, maxiter);
