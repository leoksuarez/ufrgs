clc(); clf(); clear;

x = [0 2 3 5 8 11 12 15]';
y = [50 56 60 72 85 100 110 125]';
V_l = vander(x, 2);

b_l = V_l' * y;
a_l = V_l' * V_l \ b_l;

V_p = vander(x, 3);
b_p = V_p' * y;
a_p = (V_p' * V_p) \ b_p;

xx = linspace(-1, 15);

plot(x, y, 'o');
plot(xx, a_l(2) * xx + a_l(1), 'k-');
plot(xx, a_p(3) * xx.^2 + a_p(2) * xx + a_p(1), 'r-');
xlabel('$x$', 'fontsize', 4);
ylabel('$y$', 'fontsize', 4);
legend(['pontos'; 'ajuste linear'; 'ajuste quadrático']);
title('Ajuste por mínimos quadrados', 'fontsize', 5);
