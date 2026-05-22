function [x] = gauss(A,b)
    // performs gaussian elimination without partial pivoting
    // input: n x n matrix A and n x 1 vector b
    // output: n x 1 solution vector x
    n = size(b,1);
    
    for i = 1:n-1
        if A(i,i) == 0 then
            error('zero element in pivot position' + string(i));        
        end
        multipliers = A(i+1:n,i) / A(i,i);
        A(i+1:n,i+1:n) = A(i+1:n,i+1:n) - multipliers*A(i,i+1:n); // update submatrix
        b(i+1:n) = b(i+1:n) - multipliers*b(i);
    end
    x = zeros(n,1); // initialize solution vector
    x(n) = b(n) / A(n,n);
    for j = n-1:-1:1
        x(j) = (b(j) - A(j,j+1:n)*x(j+1:n))/ A(j,j);
    end
endfunction
