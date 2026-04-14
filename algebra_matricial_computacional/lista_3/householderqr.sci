function [Q,R] = householderqr(A)
    // compute the QR decomposition of matrix A using Householder reflections
    // input: m x n matrix A
    // output: m x m matrix Q and m x n upper-triangular matrix R such that A=QR
    R = A;
    [m,n] = size(A)
    Q = eye(m,m);
    k = min(m-1,n);
    
    for i = 1:k
        [R(i:m,i:n),u] = hzero1(R(i:m,i:n));
        Q(1:m,i:m) = Q(1:m,i:m) - (2/norm(u,2)^2)*(Q(1:m,i:m)*u)*u';
    end
endfunction
