x = logspace(0, 18, 2000);
y = (1+1./x).^x;

figure('Name', 'Número de Euler');
semilogx(x, y, '-r');

grid on;
ylim([0, 8]);
