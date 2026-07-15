clear; clf;

// Define matrices and vector
A = [5, 1; 1, 4];
B = [7, 6.99; 6.99, 7];
b = [46.463; 17.499];

// Exact minima for setting up the grid centers (x = inv(A)*b)
min_A = A \ b;
min_B = B \ b;

// Define evaluation grids
x1_A = linspace(min_A(1)-15, min_A(1)+15, 100);
x2_A = linspace(min_A(2)-15, min_A(2)+15, 100);

// Matrix B needs a wider/narrower window to capture the valley structure
x1_B = linspace(min_B(1)-100, min_B(1)+100, 150);
x2_B = linspace(min_B(2)-100, min_B(2)+100, 150);

// Initialize evaluation matrices
Z_A = zeros(length(x1_A), length(x2_A));
Z_B = zeros(length(x1_B), length(x2_B));

// Compute values for A
for i = 1:length(x1_A)
    for j = 1:length(x2_A)
        v = [x1_A(i); x2_A(j)];
        Z_A(j, i) = 0.5 * v' * A * v - v' * b;
    end
end

// Compute values for B
for i = 1:length(x1_B)
    for j = 1:length(x2_B)
        v = [x1_B(i); x2_B(j)];
        Z_B(j, i) = 0.5 * v' * B * v - v' * b;
    end
end

// --- Plotting ---
clf();

// Plot for Matrix A
subplot(1, 2, 1);
contour(x1_A, x2_A, Z_A, 20, fpf=' ');
plot(min_A(1), min_A(2), "r*"); // Mark the minimum

// Plot for Matrix B
subplot(1, 2, 2);
contour(x1_B, x2_B, Z_B, 20, fpf=' ');
plot(min_B(1), min_B(2), "r*"); // Mark the minimum
