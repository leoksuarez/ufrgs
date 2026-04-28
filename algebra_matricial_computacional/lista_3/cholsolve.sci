function [x] = cholsolve(R, b)
    // solve Ax=b for positive definite matrix A given rhs b
    // input: n x n positive matrix A, n x 1 vector b
    // output: n x 1 solution vector x
    [n,m] = size(R);
    
    // solve R'y=b by forward substitution
    y = zeros(n,1);
    y(1) = b(1) / R'(1,1);
    for i = 2:n
        y(i) = (b(i) - R'(i,1:i-1) * y(1:i-1)) / R'(i,i);
    end
    
    // solve Rx=y by back substitution
    x = zeros(n,1);
    x(n) = y(n) / R(n,n);
    for k = n-1:-1:1
        x(k) = (y(k) - R(k,k+1:n) * x(k+1:n)) / R(k,k);
    end
endfunction
