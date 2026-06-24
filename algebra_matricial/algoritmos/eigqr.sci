function E = eigqr(A, tol, maxiter)
    // Hessenberg QR iteration for computing all eigenvalues of a real matrix whose eigenvalues have distinct magnitudes
    // input: real matrix A, tolerance tol, and max number of iterations maxiter
    // output: vector containing eigenvalues E
    // if the desired tolerance is not achieved for any particular eigenvalue, a warning message is printed and computation continues for the remaining eigenvalues
    
    H = hhess(A); // transform A into Hessenberg matrix H using Householder reflections
    [n, n] = size(A);
    
    for k = n:-1:2
        iter = 0;
        while norm(H(k, k-1), 2) >= tol * (norm(H(k-1, k-1), 2) + norm(H(k, k), 2))
            iter = iter + 1;
            if iter > maxiter
                disp('Failure of convergence');
                disp('Current eigenvalue approximation', H(k, k));
                break
            end
            [Q, R] = givenshessqr(H(1:k, 1:k));
            H(1:k, 1:k) = R * Q;
        end
        H(k, k-1) = 0
    end
    E = diag(H);
endfunction
