function erro_rel = erro_rel(x, x_aprox)
  % computa o erro relativo de uma aproximação
  % inputs:
    % x - número real
    % x_aprox - aproximação de x
  % outputs:
    % erro_rel - erro relativo da aproximação
  erro_abs = abs(x-x_aprox);
  erro_rel = erro_abs/abs(x);
endfunction
