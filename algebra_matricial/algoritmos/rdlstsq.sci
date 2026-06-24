function [x, res]= rdlstsq(A,b)
    // compute the minimum norm solution to the linear least-squares problem Ax=b using SVD
    // input: m x n matrix A and m x 1 vector b
    // output: solution vector x and the residual
    [m,n] = size(A)
    [U,S,V] = svd(A);
    sigma = diag(S);
    // compute the rank of A
    tol = max(size(A)) * abs(max(sigma) - nearfloat("pred", max(sigma)));
    r = sum(sigma > tol);
    x = zeros(n,1);
    for i = 1:r
        x = x + ((U(:,i)' * b) / sigma(i)) * V(:,i);
    end
    res = 0;
    for i = r+1:m
        res = res + (b' * U(:,i));
    end
    res = sqrt(res);
endfunction
