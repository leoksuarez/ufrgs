function [x, r, iter] = precg(A, b, x0, tol, maxiter)
    // solve Ax=b using the incomplete Cholesky preconditioned conjugate gradient method
    // input: SPD matrix A, rhs b, initial guess x0, tolerance tol, and max number of iterations maxiter
    // output: approximate solution x, norm of the residual r, and numer of iterations iter
    R = icholesky(A); // compute incomplete Cholesky decomposition of A
    // zero off-diagonal elements in A are kept as zero in R, preserving sparsity pattern
    x = x0;
    r = b - A * x;
    z = cholsolve(R, r); // compute the preconditioned residual (R^T R)z = r or Mz = r or z = M^-1 r
    p = z;
    i = 0;
    while (norm(r, 2) >= tol) & (i < maxiter)
        alpha = (z' * r) / (p' * A * p); // compute step length on the direction of p_i
        x = x + alpha * p;
        r_new = r - alpha * A * p;
        z_new = cholsolve(R, r_new); // compute new preconditioned residual
        beta_new = (r_new' * z_new) / (r' * z); // compute the coefficient of the last direction p_i
        p = z_new + beta_new * p;
        r = r_new; // update residual
        z = z_new; // update preconditioned residual
        i = i + 1;
    end
    r = norm(r, 2); iter = i;
    if iter >= maxiter then
        iter = -1;
    end
endfunction
