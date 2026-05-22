function [E] = modgrsch(V)
    // modified GS to convert a set of linearly independent vectors to a set of orthonormal vectors spanning the same subspace
    // instead of removing all projections at once, we remove one projection at a time to reduce rounding errors
    // input: m x n matrix V whose columns are the LI vectors to be orthonormalized
    // output: m x n matrix E whose columns are an orthonormal set of vectors that span the same subspace as the columns of V
    [m,n] = size(V);
    for i = 1:n
        E(:,i) = V(:,i);
        for j = 1:i-1
            E(:,i) = E(:,i) - (E(:,i)' * E(:,j)) * E(:,j); // remove from v_i its projection onto e_j one at a time
            // to obtain a vector u_i that is orthogonal to each e_j
        end
        E(:,i) = E(:,i) / norm(E(:,i),2); // normalize u_i to obtain unit vector e_i
    end
endfunction
