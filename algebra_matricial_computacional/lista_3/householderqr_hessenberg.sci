function [R] = householderqr_hessenberg(A)
    // triangularize Hessenberg matrix A using Householder reflections
    // input: n x n Hessenberg matrix A
    // output: n x n upper-triangular matrix R
    R = A;
    [n,n] = size(A)
    
    for i = 1:n-1
        [R(i:i+1,i:n),u] = hzero1_hessenberg(R(i:i+1,i:n));
    end
endfunction
