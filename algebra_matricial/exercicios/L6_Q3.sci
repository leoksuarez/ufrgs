clear; clc();

A = [1 -1 3; 8 8 1; 4 6 -12; 6 -9 0; 3 4 4];
b = [1 3 -1 6 15]';

// item a. usando as eqs normais
R_chol = chol(A' * A);
y_chol = R_chol' \ (A' * b);
x_chol = R_chol \ y_chol;

// item b. usando qr
[Q, R] = qr(A);
x_qr = R \ (Q' * b);

// item c. usando svd
[U, S, V] = svd(A);
y_svd = S \ (U' * b);
x_svd = V * y_svd;
