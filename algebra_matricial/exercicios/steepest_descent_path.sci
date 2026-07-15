clc; clf;
// 1. Define the paraboloid function f(x,y) = x^2 + 2y^2
function z = f(x,y)
    z = x^2 + 2*y^2;
endfunction

// 2. Define the gradient of the function: grad f(x,y) = [2x, 4y]
function g = grad_f(x,y)
    g = [2*x; 4*y];
endfunction

// 3. Steepest Descent Parameters
x0 = [1.5; 1.0];   // Initial guess
alpha = 0.2;       // Learning rate (step size)
max_iter = 30;     // Maximum iterations
epsilon = 1e-4;    // Convergence tolerance

// Perform Steepest Descent
path_x = x0(1);
path_y = x0(2);
path_z = f(x0(1), x0(2));

x_curr = x0;
for i = 1:max_iter
    g = grad_f(x_curr(1), x_curr(2));
    
    // Check for convergence
    if norm(g) < epsilon then
        break;
    end
    
    // Update rule: x_{k+1} = x_k - alpha * grad_f(x_k)
    x_next = x_curr - alpha * g;
    
    // Store the path
    path_x = [path_x, x_next(1)];
    path_y = [path_y, x_next(2)];
    path_z = [path_z, f(x_next(1), x_next(2))];
    
    x_curr = x_next;
end

// 4. Plotting the Paraboloid
scf(0); // Create figure 1
t = linspace(-2, 2, 50);
[X, Y] = meshgrid(t, t);
Z = f(X, Y);

// Plot 3D surface
subplot(1, 2, 1);
surf(X, Y, Z);
title("Paraboloid and Steepest Descent Path");
xlabel("x"); ylabel("y"); zlabel("z");

// Plot the optimization path on the surface
hold on;
plot3d(path_x, path_y, path_z, ...
    style = 5, ...     // Sets a red line
    flag = [0, 0, 0]); // Plot as curve
hold off;

// 5. Plot Contours and Path
subplot(1, 2, 2);
contour(t, t, f, [0.1, 0.5, 1, 2, 4, 6]);
title("Contour and Descent Path");
xlabel("x"); ylabel("y");

hold on;
plot(path_x, path_y, 'r-o', 'LineWidth', 2);
hold off;
