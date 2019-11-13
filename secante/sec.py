import numpy as np

#parametros da função exemplo
t, v, m, g = 10, 40, 68, 9.8


def f(c):
    #funcao exemplo
    f = ((g*m)/c)*(1 - np.exp((-c*t)/m)) - v    
    return f

#estimativas iniciais
a, b = 1.05, 2.16

#erro absoluto aceitavel
erro = 10**-8

z = 0
for i in range(1000):
    z+= 1
    if abs(f(b)) < erro:
        print("Achou...")
        break
    else:
        novo = (f(b)*a - f(a)*b)/(f(b) - f(a))
        a, b = b, novo

print("Raiz: " + str(b) + "\nIteracao: " + str(z) )