// data points
x = [0.0, 1.0, 1.5, 2.3, 2.5, 4.0, 5.1, 6.0, 6.5, 7.0, 8.1, 9.0, 9.3, 11.0, 11.3, 12.1, 13.1, 14.0, 15.5, 16.0, 17.5, 17.8, 19.0, 20.0]';
y = [0.2, 0.8, 2.5, 2.5, 3.5, 4.3, 3.0, 5.0, 3.5, 2.4, 1.3, 2.0, -0.3, -1.3, -3.0, -4.0, -4.9, -4.0, -5.2, -3.0, -3.5, -1.6, -1.4, -0.1]';

// (1)
plot(x', y', 'ko');

// plotted data suggests adjusting to a polynomial of degree 3
V = vander(x, 4); // build vandermonde matrix for the polynomial
[a, r1] = qrlstsq(V,y) // solve the least-squares problem using QR decomposition
// a is the polynomials coefficients and r1 is the residual y-Va
p = poly(a, "x", "coeff");
x_pol = linspace(0, 20, 100);
y_pol = polyval(p, x_pol);

plot(x_pol, y_pol, '-b', 'thickness', 2);

// (2)
// determine A and B such that the quadratic error function E(A,B) is minimized
// compute partial derivatives of E(A,B) and set them to zero
n = size(x,1); // number of points
i = 1:n;
E_matrix = [n sum(sin(%pi*x(i)/10)); sum(sin(%pi*x(i)/10)) sum(sin(%pi*x(i)/10).^2)]; // coefficient matrix
b_trig = [sum(y(i)) sum(y(i).*sin(%pi*x(i)/10))]'; // independent vector
sol_trig = E_matrix \ b_trig;
A = sol_trig(1); B = sol_trig(2);
y_trig = A + B * sin(%pi*x_pol/10); // compute the values of g(x) given the parameters A, B

plot(x_pol, y_trig, '--r', 'thickness', 2);
title("Ajuste por Mínimos Quadrados", "fontsize", 4);
xlabel("$x$", "fontsize", 4);
ylabel("$f(x)$", "fontsize", 4);
xgrid(color("gray"));
legend(["dados experimentais", "ajuste polinomial", "ajuste trigonométrico"])

// residual comparison
y_trig_data = A + B * sin(%pi*x/10);
r1_sqnorm = sum((polyval(p, x) - y).^2);
r2_sqnorm = sum((y_trig_data - y).^2)
