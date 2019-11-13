import numpy as np

#parametros da funcao exemplo
t, v, m, g = 10, 40, 68, 9.8


def f(c):
    #funcao exemplo
    f = ((g*m)/c)*(1 - np.exp((-c*t)/m)) - v

    return f

#erro absoluto aceitável
erro = 10**-9

#estimativas iniciais
a, b = 14, 16

z = 0
for i in range(150):
    if f(b) * f(a) > 0:
        print("Intervalos com sinais iguais.")
        exit(1);

    raiz = a*f(b) - b*f(a)
    raiz = raiz/(f(b) - f(a))

      
    if abs(f(raiz)) < erro:        
        break        
    elif f(b)*f(raiz) < 0:
        a, b = raiz, b
    elif f(a)*f(raiz) < 0:
        a, b = a, raiz
    
    z += 1  
    
    
    

print("A raiz achada foi: " + str(raiz) + " na " + str(z) + "a iteracao, e seu valor é: " + str(f(raiz)))