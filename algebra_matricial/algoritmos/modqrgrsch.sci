function [Q,R] = modqrgrsch(A)
    // performs QR decomposition of a matrix using the modified GS procedure
    // input: m x n matrix A
    // output: m x n orthogonal matrix Q, n x n upper-triangular matrix R
    [m,n] = size(A);
    for i = 1:n
        Q(:,i) = A(:,i);
        for j = 1:i-1
            R(j,i) = Q(:,i)' * Q(:,j); // compute coefficient r_{ji} of the projection of v_i onto e_j
            Q(:,i) = Q(:,i) - R(j,i) * Q(:,j); // remove from v_i its projection onto e_j one at a time
            // to obtain a vector u_i that is orthogonal to each e_j
        end
        R(i,i) = norm(Q(:,i),2); // compute coefficient r_{ii}
        Q(:,i) = Q(:,i) / R(i,i); // normalize u_i to obtain unit vector e_i
    end
endfunction
