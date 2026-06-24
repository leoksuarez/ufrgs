function R = icholesky(A)
    // compute the incomplete Cholesky factorization of a symmetric positive definite matrix
    // input: symmetric positive definite matrix A
    // output: upper-triangular matrix R
    [m, n] = size(A);
    if n ~= m then
        error('Input matrix must be square');
    end
    R = zeros(n,n); // initialize R
    for i = 1:n // go through matrix rows
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
            R(i,i) = sqrt(tmp); // compute diagonal elements
        end
        for j = i+1:n // go through (n-i) matrix columns
            // only update nonzero sparsity pattern
            if A(j,i) ~= 0            
                sum_product = 0;
                for k = 1:i-1
                    sum_product = sum_product + R(k,i)*R(k,j);
                end
                R(i,j) = (A(i,j) - sum_product) / R(i,i); // compute off-diagonal elements
        end
    end
endfunction
