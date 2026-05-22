function A = givensmul(A,i,j,c,s)
    // multiplication of m x n matrix A by Givens matrix
    // input: matrix A, indices i and j, Givens parameters c and s
    // output: m x n matrix J(i,j,c,s)A
    
    a = A(i,:);
    b = A(j,:);
    
    A(i,:) = c*a + s*b;
    A(j,:) = -s*a + c*b;
endfunction
