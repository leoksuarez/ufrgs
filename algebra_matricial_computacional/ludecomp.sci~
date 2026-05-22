function [L,U,P] = ludecomp(A)
    // performs LU decomposition using gaussian elimination with partial pivoting
    // Input: n x n matrix A
    // Output: lower-triangular matrix L, upper-triangular matrix U, and permutation matrix P such that PA=LU
    n = size(A,1);
    U = A;
    L = eye(n,n);
    P = eye(n,n);
    for i = 1:n-1
        [m,k] = max(abs(U(i:n,i))); // get the largest pivot in each column (value m, index k)
        pivot_index = k+i-1;
        //perform row exchanges if current row is not a pivot row 
        if pivot_index ~= i then
            U([i,pivot_index],:) = U([pivot_index,i],:); // exchange rows i and pivot_index in matrix A
            P([i,pivot_index],:) = P([pivot_index,i],:);
            if i > 1 then
                L([i,pivot_index],1:i-1) = L([pivot_index,i],1:i-1); // exchange rows before the current column in matrix L
            end
        end
        multipliers = U(i+1:n,i) / U(i,i);
        U(i+1:n,i+1:n) = U(i+1:n,i+1:n) - multipliers*U(i,i+1:n); // update submatrix
        L([i+1:n],i) = multipliers;
    end
    U = triu(U); 
endfunction
