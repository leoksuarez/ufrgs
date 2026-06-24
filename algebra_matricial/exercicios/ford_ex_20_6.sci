A = [2 2; 1 3];
// extract submatrices from A
D = diag(diag(A));
L = tril(A, -1);
U = triu(A, 1);

// compute iteration matrices for the Jacobi and Gauss-Seidel methods
T_j = -inv(D) * (L + U);
T_gs = -inv(L + D) * U;

// compute spectral radii of the iteration matrices
evalues_j = spec(T_j);
evalues_gs = spec(T_gs);
rho_j = max(abs(evalues_j));
rho_gs = max(abs(evalues_gs));

// let relaxation parameter range from 0.01 to 1.99 in steps of 0.01
omega = 0.01:0.01:1.99;
rho_val = zeros(1, length(omega)); // initialize vector for the spectral radius of SOR iteration matrix
norm2_val = zeros(1, length(omega)); // initialize vector for the 2-norm of SOR iteration matrix

for k = 1:length(omega)
    w = omega(k);
    // construct the matrix from part
    B = [1 - w, -w; w*(2*w - 2)/6, (w^2)/3 - w + 1];
    rho_val(k) = max(abs(spec(B)));  // compute spectral radius of SOR iteration matrix for omega=k
    norm2_val(k) = norm(B, 2);       // compute 2-norm of SOR iteration matrix for omega=k
end

clf();
// plot omega vs rho(B_{SOR})
subplot(2, 1, 1);
plot(omega, rho_val, 'b-');
xgrid();
xlabel('$\omega$', 'fontsize', 4);
ylabel('$\rho(B_{SOR})$', 'fontsize', 4);
title('$\omega \text{ vs }\rho(B_{SOR})$', 'fontsize', 5);

// plot omega vs 2-norm of B_{SOR}
subplot(2, 1, 2);
plot(omega, norm2_val, 'r-');
xgrid();
xlabel('$\omega$', 'fontsize', 4);
ylabel('$\Vert B_{SOR}\Vert_2$', 'fontsize', 4);
title('$\omega \text{ vs 2-Norm of }\Vert B_{SOR}\Vert$', 'fontsize', 5);
