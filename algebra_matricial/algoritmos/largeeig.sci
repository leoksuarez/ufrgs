function [lambda, x, iter] = largeeig(A, x0, tol, maxiter)
    // use the power method to find the dominant eigenvalue and the corresponding eigenvector of real diagonalizable matrix A
    // input: diagonalizable matrix A, initial approximation x0, desired tolerance tol, and maximum number of iterations maxiter
    // output: dominant eigenvalue lambda, corresponding eigenvector x, and number of iterations iter
    // if the method does not converge, iter=-1
    x0 = x0 / norm(x0, 2);
    
    for k = 1:maxiter
        x_k = A * x0;
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
