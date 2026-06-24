function [x] = trisolve(l,u,c,rhs)
    // solve Tx=b given tridiagonal factorization of T 
    // into unit lower-bidiagonal matrix L and upper-bidiagonal matrix U
    // input: l is the subdiagonal of the lower-diagonal matrix, u is the main diagonal of upper-diagonal matrix
    // output: solution vector x
    [n,m] = size(rhs);
    
    // solve Ly=rhs by forward substitution
    y = zeros(n,1);
    y(1) = rhs(1);
    for i = 2:n
        y(i) = rhs(i) - l(i-1)*y(i-1);
    end
    
    // solve Ux=y by back substitution
    x = zeros(n,1);
    x(n) = y(n) / u(n);
    for j = n-1:-1:1
        x(j) = (y(j) - c(j)*x(j+1)) / u(j);
    end
endfunction
