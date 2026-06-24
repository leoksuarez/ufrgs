x = [0 1 2 3 4 5 6 7 8 9]';
y = [1 2.9 6.8 12 20.5 30.9 42.9 51.5 73 90.5]';

A1 = vander(x, 1); 
A2 = vander(x, 2);
A3 = vander(x, 3);
A4 = vander(x, 4);

x1 = A1 \ y;
x2 = A2 \ y;
x3 = A3 \ y;
x4 = A4 \ y;

p1 = poly(x1, "x", "coeff");
p2 = poly(x2, "x", "coeff");
p3 = poly(x3, "x", "coeff");
p4 = poly(x4, "x", "coeff");

x_p = linspace(0, 10, 100);
y_p1 = polyval(p1, x_p);
y_p2 = polyval(p2, x_p);
y_p3 = polyval(p3, x_p);
y_p4 = polyval(p4, x_p);
Y = [y_p1', y_p2', y_p3', y_p4'];

clf();
plot(x', y', 'ko');
plot(x_p, Y, 'thickness', 2);
title("Ajuste por Mínimos Quadrados", 'fontsize', 5);
xlabel("$x$", 'fontsize', 4);
ylabel("$y$", 'fontsize', 4);
legend(['dados', 'grau 1', 'grau 2', 'grau 3', 'grau 4']);
xgrid(color('gray'));
