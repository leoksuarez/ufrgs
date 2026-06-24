function [Q, R] = givenshessqr(A)
    // compute QR decomposition of Hessenberg matrix using Givens rotations to zero out subdiagonal elements
    // input: Hessenberg matrix A
    // output: orthogonal matrix Q and upper triangular matrix R
    
    [n, n] = size(A);
    Q = eye(n,n); // initialize Q = I
    
    for i = 1:n-1
        [c, s] = givensparms(A(i, i), A(i+1, i)); // get parameters required to perform Givens rotation
        // implicitly multiply A and Q by Givens matrix
        A = givensmul(A, i, i+1, c, s);
        Q = givensmul(Q, i, i+1, c, s);
    end
    R = A;
    Q = Q';    
endfunction
