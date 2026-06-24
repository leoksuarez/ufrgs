clc(); clear;
// item a.
A_a = [1 -1 2; 3 0 1; 4 2 -8; 5 2 7];
b_a = [1 -1 3 7]';

if size(A_a, 1) >= size(A_a, 2) then
    if rank(A_a) == size(A_a, 2) then
        x_a = inv(A_a' * A_a) * A_a' * b_a;
        x_a_pinv = pinv(A_a) * b_a;
    else
        x_a_pinv = pinv(A_a) * b_a;
    end
else
    if rank(A_a) == size(A_a, 1) then
        x_a = A_a' * inv(A_a * A_a') * b_a;
        x_a_pinv = pinv(A_a) * b_a;
    else
        x_a_pinv = pinv(A_a) * b_a;
    end
end

// item b.
A_b = [2 3 1; -1 2 3; 3 1 -2; 6 9 3];
b_b = [-1 3 5 0]';

if size(A_b, 1) >= size(A_b, 2) then
    if rank(A_b) == size(A_b, 2) then
        x_b = inv(A_b' * A_b) * A_b' * b_b;
        x_b_pinv = pinv(A_b) * b_b;
    else
        x_b_pinv = pinv(A_b) * b_b;
    end
else
    if rank(A_b) == size(A_b, 1) then
        x_b = A_b' * inv(A_b * A_b') * b_b;
        x_b_pinv = pinv(A_b) * b_b;
    else
        x_b_pinv = pinv(A_b) * b_b;
    end
end

// item c.
A_c = [2 5 6 8; -1 3 7 1; 5 1 6 2];
b_c = [1 -1 10]';

if size(A_c, 1) >= size(A_c, 2) then
    if rank(A_c) == size(A_c, 2) then
        x_c = inv(A_c' * A_c) * A_c' * b_c;
        x_c_pinv = pinv(A_c) * b_c;
    else
        x_c_pinv = pinv(A_c) * b_c;
    end
else
    if rank(A_c) == size(A_c, 1) then
        x_c = A_c' * inv(A_c * A_c') * b_c;
        x_c_pinv = pinv(A_c) * b_c;
    else
        x_c_pinv = pinv(A_c) * b_c;
    end
end

// item d.
A_d = [1 -6 2 -4; 3 -18 6 -12; 9 0 12 0];
b_d = [-2 8 12]';

if size(A_d, 1) >= size(A_d, 2) then
    if rank(A_d) == size(A_d, 2) then
        x_d = inv(A_d' * A_d) * A_d' * b_d;
        x_d_pinv = pinv(A_d) * b_d;
    else
        x_d_pinv = pinv(A_d) * b_d;
    end
else
    if rank(A_d) == size(A_d, 1) then
        x_d = A_d' * inv(A_d * A_d') * b_d;
        x_d_pinv = pinv(A_d) * b_d;
    else
        x_d_pinv = pinv(A_d) * b_d;
    end
end

