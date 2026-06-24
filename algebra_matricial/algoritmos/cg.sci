function [x, r, iter]= cg(A, b, x0, tol, maxiter)
    // solve Ax=b using the conjugate gradient method for a positive definite matrix A
    // input: matrix A, rhs b, initial approximation x0, tolerance tol, and max number of iterations maxiter
    // output: approximate solution x, norm of the residual, and number of iterations iter
    x = x0;
    r = b - A * x;
    p = r;
    i = 0;
    while (norm(r, 2) >= tol) & (i < maxiter)
        alpha = (r' * r) / (p' * A * p); // compute step length alpha_i along the direction vector p_i
        x = x + alpha * p; // compute x_(i+1) = x_i + alpha_i * p_i
        r_new = r - alpha * A * p; // compute the residual r_(i+1) = r_i - alpha_i * A * p_i
        beta_new = (r_new' * r_new) / (r' * r); // compute the coefficient c_(i, i+1) of the last direction p_i
        p = r_new + beta_new * p; // update direction vector p_(i+1) = r_(i+1) + beta_(i+1) * p_i
        r = r_new;
        i = i + 1;
    end
    r = norm(r, 2); iter = i;
    if iter >= maxiter then
        iter = -1;
    end
endfunction
