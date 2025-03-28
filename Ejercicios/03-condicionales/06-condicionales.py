'''
Cond6. Escribir la función de dos argumentos reales positivos p, q, que calcule y regrese la raíz más grande de la ecuación x2 − 2p x − q = 0 
'''

from math import *

def raizMayor (p, q):
    #Calculamos usando cuadratica x=−b± √b2−4ac / 2.a
    discriminante = sqrt(p**2 + q) #Calcula √(p² + q)
    return p + discriminante #x1​=p+p2+q (la mayor)

#Valores de entrada
print(raizMayor(1, 1))
print(raizMayor(3, 4))
