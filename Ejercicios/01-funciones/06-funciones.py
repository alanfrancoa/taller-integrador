'''
Fun6. Dado un número real estrictamente positivo, regresar su raíz cúbica. Sugerencia: usar exp y log.
Ejemplo. Entrada: 65. Salida: 4.02072575858906.
Ejemplo. Entrada: 1000. Salida: 10.0000000000000.
'''

from math import *

def raizCubica (a):
    if a > 0:
        return exp((1/3) * log(a))
        '''
        -log(A): Te dice a qué potencia debes elevar E para obtener A.
        -1/3⋅log(A): Te da el logaritmo de la raíz cúbica de A.
        -exp(...): Convierte ese logaritmo de nuevo en la raíz cúbica.
        '''
    else:
        return print("No es posible calcular la raiz de numeros negativos.")

numA = 65
numB = 1000

print("Raiz cubica de " + str(numA) + ": " + str(raizCubica(numA)))
print("Raiz cubica de " + str(numB) + ": " + str(raizCubica(numB)))