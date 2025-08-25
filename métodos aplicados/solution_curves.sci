function ydot=f(t,y)
    ydot=5*y
endfunction

xf= -3:0.25:3;
yf= -3:0.25:3;
clf()
fchamp(f,0,xf,yf)
xlabel('x');
ylabel('y');
