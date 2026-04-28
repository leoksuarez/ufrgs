function [l,u] = tridiaglu(a,b,c)
    // factor tridiagonal matrix T defined by subdiagonal a, main diagonal b, and superdiagonal c
    // into a product of two bidiagonal matrices L (with 1's on the main diagonal) and U (whose superdiagonal elements are
    // the same as c)
    // input: vectors a, b, c
    // output: subdiagonal l of the left bidiagonal factor and main diagonal u of the right bidiagonal factor
    [n,m] = size(b);
    u(1) = b(1);
    
    for i = 1:n-1
        l(i) = a(i) / u(i);
        u(i+1) = b(i+1) - l(i)*c(i);
    end
endfunction
