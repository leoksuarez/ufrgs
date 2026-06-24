function [x, k, relresid] = sor(A, b, x0, omega, tol, maxiter)
    // solve Ax=b using sucessive over-relaxation method
    // input: matrix A, rhs b, initial guess x0, over-relaxation parameter omega, tolerance tol, 
    // maximum number of iterations maxiter
    // output: approximate solution x, number of iterations k, relative residual relresid
    n = length(b);
    x = x0;
    k = 1;
    while k <= maxiter
       for i = 1:n
           s = A(i, 1:n) * x - A(i, i) * x(i);
           x(i) = (1 - omega) * x(i) + (omega / A(i,i)) * (b(i) - s);
       end
       relresid = norm(x - x0, %inf)/norm(x, %inf)
       if relresid < tol then
            return
        end
        x0 = x;
        k = k + 1;
    end
    disp('maximum number of iterations exceeded');
endfunction
