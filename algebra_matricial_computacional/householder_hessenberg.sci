function [R] = householder_hessenberg(A)
    // triangularize upper Hessenberg matrix A using Householder reflections
    // input: n x n upper Hessenberg matrix A
    // output: n x n upper-triangular matrix R
    R = A;
    [m,n] = size(A);
    
    for i = 1:n-1
        [R(i:i+1,i:n),u] = hzero1_hessenberg(R(i:i+1,i:n));
    end
endfunction
