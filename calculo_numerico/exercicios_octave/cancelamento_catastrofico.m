x = logspace(-17, -12, 2000);
num = (1+x)-1;
y = num ./ x;

figure('Name', 'Cancelamento catastrófico');
semilogx(x, y, 'b-');

grid on;
ylim([-0.2, 2.0]);
