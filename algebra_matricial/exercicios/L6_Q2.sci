clear; clc(); clf();

// load data
x = [-1.5 -1 -1.9 0 0.5 1 1.3 1.95]';
y = [1 1.6 1.5 -1.4 -1.3 -1.6 -1.8 1.9]';
z = [1 1.4 -0.3 6.4 7.3 8.6 9.4 7]';

// plot scatter points
scatter3d(x, y, z, 70, '*');

// solve least-squares problem Ax=b where A is the matrix [x y 1], x is the vector of the coefficients of the plane equation z=ax+by+c and b is the z vector
m = length(x);
A = [x y ones(m, 1)];
coef = pinv(A) * z;

// load xy domain and compute the least-squares plane solution
xx = linspace(-2, 2, 30);
yy = linspace(-2, 2, 30);
[X, Y] = meshgrid(xx, yy)
Z = coef(1) * X + coef(2) * Y + coef(3);

mesh(X, Y, Z);
title('Least-squares plane fitting', 'fontsize', 5);
