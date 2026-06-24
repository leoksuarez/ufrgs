clear; clc();
// dados A e b abaixo, encontre a solucao do problema de minimos quadrados Ax=b
A = [1 1; 2 3; 0 1];
b = [0 5 1]';

// item a. encontrar x usando pseudoinversa (ou inversa generalizada de Moore-Penrose)
x_pinv = inv(A' * A) * A' * b; // dado que 3>=2 e A tem posto 2

// item b. encontrar x usando as equacoes normais
R_chol = chol(A' * A);
y_chol = R_chol' \ (A' * b);
x_chol = R_chol \ y_chol;

// item c. encontrar x usando a decomposicao QR
[Q, R] = qr(A);
x_qr = R \ (Q' * b);

// item d. encontrar x usando a decomposicao em valores singulares (SVD)
[U, S, V] = svd(A);
y_svd = S \ (U' * b);
x_svd = V * y_svd;

// item e. computar o numero de condicionamento da matriz A
cond_A = norm(A, 2) * norm(pinv(A), 2);
