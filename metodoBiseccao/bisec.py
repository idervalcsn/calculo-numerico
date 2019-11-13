import numpy as np

#parametros da funcao exemplo
t, v, m, g = 10, 40, 68, 9.8


def f(c):
    #função exemplo
    f = ((g*m)/c)*(1 - np.exp((-c*t)/m)) - v
   
    return f

#erro relativo aceitável
erro = 0.005

#estimativas iniciais
a, b = 14, 16

z = 0

#inicia raiz antiga como infinito para que raizNova > raizAntiga
raizAntiga = float('inf')
for i in range(150):
        raizNova = (a+b)/2       

        if abs(raizNova - raizAntiga)/raizNova < erro:
            break
        elif f(b)*f(raizNova) < 0:
            a,b = raizNova, b
        elif f(a)*f(raizNova) < 0:
            a,b = a, raizNova

        raizAntiga = raizNova
        z+= 1

print("A raiz achada foi: " + str(raizNova) + " na " + str(z) + "a iteracao, e seu valor é: " + str(f(raizNova)))

