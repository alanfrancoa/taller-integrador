'''
Fun4. Escribir una función de dos argumentos reales a, b que calcule y regrese la raíz cuadrada de la suma de sus cuadrados, es decir, la longitud de la hipotenusa del triángulo rectángulo cuyos catetos tienen longitudes a, b. Sugerencia: en el lenguaje de programación elegido encontrar la función que calcula la raíz cuadrada.
Ejemplo. Entrada: 11, 27.5. Salida: 29.6184064392398. 
'''
from math import *

def hipotenusa (a, b):
    return sqrt(pow(a, 2) + pow(b, 2))

numA = 11
numB = 27.5

print("La longitud de la hipotenusa es: " + str(hipotenusa(numA, numB)))