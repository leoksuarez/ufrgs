function [lambda, x, iter] = smalleig(A, x0, tol, maxiter)
    // use the power method to find the smallest eigenvalue of diagonalizable matrix A (or use the inverse power method to find the dominant eigenvalue of A^-1)
    // input: diagonalizable matrix A, initial approximation x0, desired tolerance tol, and max number of iterations maxiter
    // output: smallest eigenvalue lambda, corresponding eigenvector x, and number of iterations iter
    x0 = x0 / norm(x0, 2); // normalize initial approximation x0
    [L, U, P] = lu(A); // compute LU decomposition of A
    
    for k = 1:maxiter
        x_k = lusolve(L, U, P, x0);
        x_k = x_k / norm(x_k, 2);
        lambda = x_k' * A * x_k;
        err = norm(A * x_k - lambda * x_k, 2);
        if err < tol
            x = x_k;
            iter = k;
            return
        end
        x0 = x_k;
    end
    x = x_k;
    iter = -1;
    return
endfunction
