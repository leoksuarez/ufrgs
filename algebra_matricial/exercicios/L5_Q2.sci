clf(); clc(); clear

crt = [2 1.90 1.85 2.06 1.95]';
vlt = [4.95 5.05 5.10 4.92 5.02]';
V = vander(crt, 2);

b = V' * vlt;
a = V' * V \ b;
res = abs(a(2));

ii = linspace(1.80, 2.10);

plot(crt, vlt, 'o');
plot(ii, a(2) * ii + a(1), 'r-');

res_legend = msprintf('R = %.3f', res);

xlabel('Corrente', 'fontsize', 4);
ylabel('Tensão', 'fontsize', 4);
title('Ajuste por mínimos quadrados', 'fontsize', 5);
legend(['dados'; res_legend], 'fontsize', 4)
