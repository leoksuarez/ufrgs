clear;
// define linear system Ax=b
A = [5, 1; 1, 4];
b = [1 1]';

// ============================
// 3D paraboloid plot
// ============================

// create coordinate grid for 3D plot
x3D = linspace(-3, 3, 100);
y3D = linspace(-3, 3, 100);
[X3D, Y3D] = meshgrid(x3D, y3D);
Z3D = (5/2)*X3D.^2 + 2*Y3D.^2 + X3D.*Y3D - X3D - Y3D;

// plot elliptic paraboloid
scf(0); clf();
surf(x3D, y3D, Z3D);
f = gcf(); 
f.color_map = jet(64);

// ============================
// 2D gradient field plot
// ============================
scf(1); clf();
f2 = gcf();
f2.color_map = jet(64);

// create coordinate grid for 2D vector field
x2D = linspace(-3, 3, 15);
y2D = linspace(-3, 3, 15);
[X2D, Y2D] = meshgrid(x2D, y2D);
Z2D = (5/2)*X2D.^2 + 2*Y2D.^2 + X2D.*Y2D - X2D - Y2D;

// compute the gradient of the quadratic function
[gx, gy] = gradient(Z2D);

// plot contour lines
levels = linspace(0.2, 16, 14);
contour2d(x2D, y2D, Z2D, levels);

// plot vector field
champ(x2D, y2D, -gx', -gy');

gca().data_bounds = [-3, -3; 3, 3];
gca().isoview = "on";
