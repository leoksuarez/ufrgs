function [x,k,relresid] = gauss_seidel(A,b,x0,tol,maxiter)
    // solve Ax=b using Gauss-Seidel iterative method
    // input: matrix A, rhs b, initial guess x0, tolerance tol, maximum number of iterations maxiter
    // output: approximate solution x and number of iterations k, relative residual relresid
    n = length(b);
    x = x0;
    k = 1;
    while k <= maxiter
        for i = 1:n
            s = A(i, 1:n) * x - A(i, i) * x(i); // update sum of terms using the latest computed values
            x(i) = (b(i) - s) / A(i,i);
        end
        relresid = norm(x - x0, %inf)/norm(x, %inf);
        if relresid < tol then
            return
        end
        x0 = x;
        k = k + 1;
    end
    disp('maximum number of iterations exceeded');
endfunction
