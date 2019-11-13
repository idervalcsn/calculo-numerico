import numpy as np

MAX_ITER = 150


#estimativa inicial
est = 0

#erro absoluto aceitável
erro = 10**-9


def f(x):
    #funcao exemplo
    f = -0.9*x**2 + 1.7*x + 2.5
    return f


def df(x):
    #derivada da função exemplo    
    return 1.7 - 1.8*x

z = 0
for i in range(MAX_ITER):
    
    if abs(f(est)) < erro:
        break
    if df(est) == 0:
        print("Quebrou. Divisao por zero")
        break
    else:
        est = est - f(est)/df(est)
    z+= 1

print("Raiz: " + str(est) + "após " + str(z) + "iteracoes.")