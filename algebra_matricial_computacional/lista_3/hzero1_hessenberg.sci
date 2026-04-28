function [A,u] = hzero1_hessenberg(A)
    // zero out the subdiagonal element in matrix A by a Householder reflection H_u
    // input: 2 x 2 matrix A
    // output: 2 x 2 matrix A implicitly premultiplied by H_u and Householder vector u that defines the hyperplane about which x is reflected
    
    x = A(1:2,1);
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
