function [x] = hhsolve(Q,R,b)
    // solve Ax=b given QR decomposition by Householder reflections
    // write Ax=b -> (QR)x=b -> Rx=Q^Tb=y, which is then solved by back-substitution
    // input: m x m orthogonal matrix Q, m x n upper-triangular matrix R, m x 1 vector b
    // output: n x 1 solution vector x
    y = Q'*b;
    n = size(R,2);
    x = zeros(n,1); // initialize solution vector
    x(n) = y(n) / R(n,n);
    
    for j = n-1:-1:1
        x(j) = (y(j) - R(j,j+1:n)*x(j+1:n)) / R(j,j);
    end
endfunction
