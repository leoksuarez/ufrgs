function [x,r,iter] = steepestdescent(A,b,x0,tol,maxiter)
    // solve Ax=b using the steepest descent method for a symmetric positive matrix A
    // the method is based on finding x such that a quadratic function phi is minimum and Ax=b
    // input: matrix A, rhs b, initial guess x0, error tolerance tol, and maximum number of iterations maxiter
    // output: approximate solution x, norm of the residual r, and number of iterations
    // if the method does not converge then iter=-1
    x = x0;
    r = b - A*x0;
    i = 0;
    while (norm(r,2) >= tol) & (i <= maxiter)
        alpha = (r' * r) / (r' * A * r); // compute how much we move along the line given by
        // the direction vector
        x = x + alpha * r; // compute x_(i+1) = x_i + alpha_i * r_i
        r = b - A * x; // compute residual vector b-Ax_i
        i = i + 1;
    end
    r = norm(r,2); iter = i;
    if iter >= maxiter then
        iter = -1;
    end
endfunction
