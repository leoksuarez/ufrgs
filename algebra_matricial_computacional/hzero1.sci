function [A,u] = hzero1(A)
    // zero out all elements below a_11 in matrix A by a Householder reflection H_u
    // input: m x n matrix A
    // output: m x n matrix A implicitly premultiplied by H_u and Householder vector u that defines the hyperplane about which x is reflected
    
    x = A(:,1);
    colmax = max(abs(x));
    x = x/colmax; // normalize x to minimize cancellation errors
    colnorm = norm(x,2);
    u = x;
    
    // construct Householder vector u
    if u(1) >= 0 then
        u(1) = u(1) + colnorm;
    else
        u(1) = u(1) - colnorm; 
    end
    
    // implicitly form H_uA
    unorm = norm(u,2);
    if unorm ~= 0 then
        beta = 2/(unorm^2);
    else
        beta = 0;
    end
    A = A - (beta*u)*(u'*A);
endfunction
