function [Q, R] = givensqr(A)
    // compute the QR decomposition of a matrix using Givens rotations
    // input: m x n matrix A
    // output: m x m orthogonal matrix Q and m x n upper-triangular matrix R
    
    [m, n] = size(A);
    Q = eye(m, m); // initialize Q = I
    
    for i = 1:min(m-1, n)
        for j = i+1:m // run down column i
            [c, s] = givensparms(A(i, i),A(j, i)); // get parameters required to perform Givens rotation
            // implicitly multiply A and Q by Givens matrix
            A = givensmul(A, i, j, c, s);
            Q = givensmul(Q, i, j, c, s);
        end
    end
    R = A;
    Q = Q';
endfunction
