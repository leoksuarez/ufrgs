clear; clc();

A = [1 4 10; -2 6 -6; 5 -7 23; 3 3 21];
b = [1 12 -1 2]';

// a. using qr
[Q, R] = qr(A);
try 
    x_qr = R \ (Q' * b);
catch
    disp("A does not have full rank.")
end

// b. using svd
[U, S, V] = svd(A);

s = diag(S);
m = size(A, 1);
r = rank(A);

// compute least-squares solution with smallest 2-norm
x_LS = 0
for i = 1:r
    x_LS = x_LS + (U(:, i)' * b / s(i)) * V(:, i);
end

r_LS = 0
for i = r+1:m
    r_LS = r_LS + (U(:, i)' * b)^2;
end
