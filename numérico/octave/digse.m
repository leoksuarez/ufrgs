function digse = digse(x, x_aprox)
  % computa o número de dígitos significativos de uma aproximação para um número real x
  % inputs:
    % x - número real
    % x_aprox - aproximação de x
  % outputs:
    % digse - número de dígitos significativos corretos na aproximação de x por x_aprox
  erro_rel = abs(x-x_aprox)/abs(x);
  digse = floor(-log10(erro_rel)+1/2);
endfunction
