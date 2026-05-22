function [c,s] = givensparms(x_i,x_j)
    // normalize the entries x_i or x_j to minimize overflow/underflow errors
    // input: x_i and x_j, j>i, of vector x
    // output: Givens parameters c and s for x
    
    if x_j == 0 then
        c = 1;
        s = 0;
    elseif abs(x_j) > abs(x_i) then
        t = x_i/x_j; // make t such that 0<t<1
        s = 1/sqrt(1+t^2);
        c = s*t;
    else
        t = x_j/x_i;
        c = 1/sqrt(1+t^2);
        s = c*t;
    end
endfunction
