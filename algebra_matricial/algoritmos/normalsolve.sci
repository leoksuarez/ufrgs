function [x, r, iter] = normalsolve(A, b, x0, tol, maxiter)
    // solve Ax=b using the normal equations and the conjugate gradient method
    // A^TA is symmetric, if A has full rank then A^TA is positive definite, if A is well conditioned and it is
    // easy to compute A^T then we can apply CG to the normal equations A^TAx = A^Tb
    // input: matrix A, rhs b, initial guess x0, tolerance tol, and max number of iterations maxiter
    // output: approximate solution x, norm of the residual r, and number of iterations iter
    [x, r, iter] = cg(A'*A, A'*b, x0, tol, maxiter);
endfunction
