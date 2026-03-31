function [x] = lusolve(L,U,P,b)
    // solve linear system given LU decomposition
    // Input: lower-triangular matrix L, upper-triangular matrix U, permutation matrix P, and vector b
    // Output: solution vector x
    n = size(b,1);
    
    b = P*b; // perform same row exchanges from LU factorization in the vector b
    // solve Ly = b
    y = zeros(n,1); //initialize vector y
    y(1) = b(1);
    for i = 2:n
        y(i) = (b(i) - L(i,1:i-1)*y(1:i-1)) / L(i,i); // perform forward substitution
    end
    // solve Ux = y
    x = zeros(n,1); // initialize solution vector x
    x(n) = y(n) / U(n,n);
    for k = n-1:-1:1
        x(k) = (y(k) - U(k,k+1:n)*x(k+1:n)) / U(k,k); // perform back substitution
    end
endfunction
