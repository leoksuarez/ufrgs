function [R] = cholesky(A)
    // performs Cholesky factorization of a positive definite matrix A
    // if the algorithm fails, A is not positive definite
    // input: n x n matrix A
    // output: error message with empty matrix or upper-triangular matrix R such that A=R'R
    [n, m] = size(A);
    if n ~= m then
        error('Input matrix must be square');
    end
    
    R = zeros(n,n); // initialize R
    
    for i = 1:n // traverse matrix rows
        sum_squares = 0;
        for k = 1:i-1
            sum_squares = sum_squares + R(k,i)^2;
        end
        tmp = A(i,i) - sum_squares;
        if tmp <= 0 then
            disp('Input matrix is not positive definite');
            R = []; // return empty matrix
            return
        else
            R(i,i) = sqrt(tmp);
        end
        for j = i+1:n // traverse (n-i) matrix columns
            sum_product = 0;
            for k = 1:i-1
                sum_product = sum_product + R(k,i)*R(k,j);
            end
            R(i,j) = (A(i,j) - sum_product) / R(i,i);
        end
    end
endfunction
