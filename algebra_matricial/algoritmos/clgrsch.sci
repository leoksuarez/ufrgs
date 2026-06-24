function [E] = clgrsch(V)
    // converts a set of linearly independent vectors to a set of orthonormal vectors spanning the same subspace
    // input: m x n matrix V whose columns are the LI vectors to be orthonormalized
    // output: m x n matrix E whose columns are an orthonormal set of vectors that span the same subspace as the columns of V
    [m,n] = size(V);
    for i = 1:n
        sumproj = 0;
        for j = 1:i-1
            sumproj = sumproj + (V(:,i)' * E(:,j)) * E(:,j); // compute sum of projections of v_i onto e_1, e_2, ..., e_{i-1}
        end
        E(:,i) = V(:,i) - sumproj; // compute u_i, orthogonal to e_1, e_2, ..., e_{i-1}, by removing from v_i its 
        // orthogonal projections onto e_1, e_2, ..., e_{i-1}
        E(:,i) = E(:,i) / norm(E(:,i),2); // normalize u_i to obtain unit vector e_i
    end
endfunction
