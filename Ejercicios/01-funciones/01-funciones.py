'''
Fun1. Escribir una función de un argumento x que devuelva el cuadrado de x.
Ejemplo. Entrada: 17. Salida: 289.
Ejemplo. Entrada: −6. Salida: 36. 
'''

from math import * 

num = 17
res = pow(num, 2)
print("El nro es: " + str(num) + " su cuadrado es: " + str(res))

num = -6
res = pow(num, 2)
print("El nro es: " + str(num) + " su cuadrado es: " + str(res))