function [Q,R] = givensqr(A)
    // compute the QR decomposition of A
    // input: m x n matrix A
    // output: m x n orthogonal matrix Q
    // and m x n upper-triangular matrix R
    [m,n] = size(A);
    Q = eye(m,m); // initialize Q = I
    
    for i = 1:min(m-1,n)
        for j = i+1:m // run through column i
            [c,s] = givensparms(A(i,i),A(j,i));
            A = givensmul(A,i,j,c,s);
            Q = givensmul(Q,i,j,c,s);
        end
    end
    R = A;
    Q = Q';
endfunction
