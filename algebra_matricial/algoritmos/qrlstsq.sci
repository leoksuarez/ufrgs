function [x, r] = qrlstsq(A,b)
    // solve the least-squares problem using (reduced) QR decomposition
    // input: m x n matrix A of full rank and m x 1 column vector b
    // output: solution to the least-squares problem Ax=b and the residual
    [Q,R] = qr(A); // compute the reduced QR decomposition of A
    [m,n] = size(A);
    c = Q'*b;
    
    // solve the upper-triangular system Rx=c by back substitution
    x = zeros(n,1);
    x(n) = c(n) / R(n,n);
    for j = n-1:-1:1
        x(j) = (c(j) - R(j,j+1:n)*x(j+1:n)) / R(j,j);
    end
    
    // compute the residual r = b-Ax
    r = b - A*x;
endfunction
