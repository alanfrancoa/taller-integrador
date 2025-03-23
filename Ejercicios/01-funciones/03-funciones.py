'''
Fun3. Dados dos números enteros, regresar la suma de sus cubos. Sugerencia: usar la función programada en el Ejercicio Fun0.
Ejemplo. Entrada: 3, −12. Salida: −1701.
Ejemplo. Entrada: 15, −14. Salida: -2744.
'''

from moduloCubo import *

num = -12
res = cubo(num)
print("El nro es: " + str(num) + " su cuadrado es: " + str(res))

num = -14
res = cubo(num)
print("El nro es: " + str(num) + " su cuadrado es: " + str(res))