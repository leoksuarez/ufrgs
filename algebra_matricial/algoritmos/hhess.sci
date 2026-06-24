function [H, P] = hhess(A)
    // transform square matrix A into upper Hessenberg form
    // input: n x n matrix A
    // output: upper Hessenberg matrix H and orthogonal matrix P such that A=PHP^T using Householder reflections
    
    n = size(A, 1);
    H = A;
    P = eye(n, n);
    
    for k = 1:n-2
        // compute vector u and scalar beta required to form Householder matrix that zeros out A(k+1:n,k)
        x = H(k+1:n, k); // consider only the elements below the diagonal
        colmax = max(abs(x)); // get largest element in magnitude in x
        x = x / colmax; // normalize x to minimize overflow errors
        colnorm = norm(x, 2);
        u = x;
        // form Householder vector u
        if u(1) >= 0 then
            u(1) = u(1) + colnorm;
        else
            u(1) = u(1) - colnorm; 
        end
        // compute scalar beta
        unorm = norm(u, 2);
        if unorm ~= 0 then
            bta = 2/(unorm^2);
        else
            bta = 0;
        end        
        
        H(k+1:n, k:n) = H(k+1:n, k:n) - bta * (u * u') * H(k+1:n, k:n); // compute H_k*A_k implicitly
        H(1:n, k+1:n) = H(1:n, k+1:n) - bta * H(1:n, k+1:n) * (u * u'); // compute A_k*H_k' implicitly, remember H_k is symmetric
        P(1:n, k+1:n) = P(1:n, k+1:n) - bta * P(1:n, k+1:n) * (u * u'); // record sequence of Householder reflections
        H(k+2:n, k) = zeros(n-k-1, 1);
    end
endfunction
