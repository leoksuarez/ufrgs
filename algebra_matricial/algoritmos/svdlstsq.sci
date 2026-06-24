function [x,r] = svdlstsq(A,b)
    // solve the least-squares problem using reduced SVD
    // input: m x n matrix A of full rank and m x 1 column vector b
    // output: solution to the least-squares problem Ax=b and the residual
    [U,S,V] = svd(A);
    [m,n] = size(A);
    c = U'*b;
    
    // solve Sy=c
    for i = 1:n
        y(i) = c(i) / S(i,i); 
    end
    
    // solve x=Vy
    x = V*y;
    
    // compute the residual b-Ax
    r = b - A*x;
endfunction
