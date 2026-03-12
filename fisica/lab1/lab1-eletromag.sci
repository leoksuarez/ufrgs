// Dados experimentais
V = [0.119; 1.68; 2.64; 3.30; 4.33; 5.18; 6.09; 6.99; 7.99; 8.94]; // Tensão (V)
I = [0.110; 1.72; 2.72; 3.39; 4.45; 5.37; 6.30; 7.24; 8.29; 9.29]; // Corrente (mA)

// Número de pontos
n = length(V);

// Cálculo das incertezas para tensão (V)
delta_V = zeros(n, 1);
for i = 1:n
    if V(i) < 0.4 then
        delta_V(i) = sqrt((0.016*V(i))^2 + (0.0001)^2);
    elseif V(i) < 4 then
        delta_V(i) = sqrt((0.008*V(i))^2 + (0.001)^2);
    elseif V(i) < 40 then
        delta_V(i) = sqrt((0.008*V(i))^2 + (0.01)^2);
    elseif V(i) < 400 then
        delta_V(i) = sqrt((0.008*V(i))^2 + (0.1)^2);
    else
        delta_V(i) = sqrt((0.01*V(i))^2 + (1)^2);
    end
end

// Cálculo das incertezas para corrente (mA)
delta_I = zeros(n, 1);
for i = 1:n
    if I(i) < 0.4 then
        delta_I(i) = sqrt((0.01*I(i))^2 + (0.0001)^2);
    elseif I(i) < 4 then
        delta_I(i) = sqrt((0.01*I(i))^2 + (0.001)^2);
    elseif I(i) < 40 then
        delta_I(i) = sqrt((0.01*I(i))^2 + (0.01)^2);
    elseif I(i) < 400 then
        delta_I(i) = sqrt((0.01*I(i))^2 + (0.1)^2);
    else
        delta_I(i) = sqrt((0.012*I(i))^2 + (1)^2);
    end
end

// Tabela de dados
printf("+---------------------------------------+\n");
printf("|     Tabela 1: Dados Experimentais     |\n");
printf("+---------+---------+---------+---------+\n");
printf("|  V (V)  |  ΔV (V) | I (mA)  | ΔI (mA) |\n");
printf("+---------+---------+---------+---------+\n");
for i = 1:n
    printf("| %6.3f  | %6.4f  | %6.3f  | %6.4f  |\n", V(i), delta_V(i), I(i), delta_I(i));
end
printf("+---------+---------+---------+---------+\n\n");

// Ajuste Linear Ponderado
w = 1 ./ (delta_V.^2);  // Pesos = 1/(ΔV)²
W = sum(w);
sum_I = sum(w .* I);
sum_V = sum(w .* V);
sum_I2 = sum(w .* I.^2);
sum_IV = sum(w .* I .* V);

// Coeficientes da reta (V = a*I + b)
delta = W * sum_I2 - sum_I^2;
a = (W * sum_IV - sum_I * sum_V) / delta;  // Declividade (R)
b = (sum_I2 * sum_V - sum_I * sum_IV) / delta;  // Intercepto

// Incertezas nos coeficientes
delta_a = sqrt(W / delta);  // Incerteza em a
delta_b = sqrt(sum_I2 / delta);  // Incerteza em b

// Cálculo de R² (coeficiente de determinação)
V_medio = mean(V);
SST = sum(w .* (V - V_medio).^2);  // Soma total dos quadrados
SSR = sum(w .* (V - (a*I + b)).^2);  // Soma dos quadrados dos resíduos
R2 = 1 - SSR/SST;  // Coeficiente de determinação

// Resistência e incerteza
R = a;  // kΩ (pois I está em mA e V em V)
delta_R = delta_a;

// Gráfico V x I com ajuste linear
scf(0);
clf(0);

// Dados experimentais com barras de erro e marcadores
plot(I, V, "bo");  // Bolinhas azuis
errbar(I, V, delta_V, delta_V);  // Barras de erro em V
errbar(I, V, delta_I, delta_I);  // Barras de erro em I

// Linha de ajuste
I_linha = linspace(0, max(I), 100);
V_linha = a * I_linha + b;
plot(I_linha, V_linha, "r-", "LineWidth", 2);

// Legenda
legend(["Dados Experimentais"; "Ajuste Linear"], "in_upper_left");

// Rótulos e título
xlabel("Corrente I (mA)", "fontsize", 3);
ylabel("Tensão V (V)", "fontsize", 3);
title("Gráfico V x I - Lei de Ohm", "fontsize", 4);

// Exibir equação e R² no gráfico
txt_eq = msprintf("V = (%.4f ± %.4f) I + (%.4f ± %.4f)", a, delta_a, b, delta_b);
xstring(5, 2, txt_eq);
txt_R2 = msprintf("R² = %.6f", R2);
xstring(5, 1, txt_R2);
txt_res = msprintf("R = %.4f ± %.4f kΩ", R, delta_R);
xstring(5, 0, txt_res);

// Grade
gca().grid = [1, 1];

// Exportar gráfico
xs2png(gcf(), "grafico_VxI_Lei_de_Ohm.png");

// Resultados
printf("Resultados do Ajuste Linear:\n");
printf("----------------------------------------\n");
printf("Declividade (a = R)  = %.4f ± %.4f kΩ\n", a, delta_a);
printf("Intercepto (b)       = %.4f ± %.4f V\n", b, delta_b);
printf("Coeficiente R²       = %.6f\n", R2);
printf("Resistência (R)      = %.4f ± %.4f kΩ\n", R, delta_R);
printf("----------------------------------------\n");
