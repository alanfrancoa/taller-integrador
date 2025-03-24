'''
Fun8. Dados dos números reales positivos a, b, regresar la medida del ángulo BAC en el triángulo ABC, si el ángulo ACB es recto, |BC| = a y |AC| = b. Sugerencia: en el lenguaje de programación elegido encontrar la función trigonométrica inversa adecuada.
Entrada: 2.7, 5. Salida: 0.4951332634684. 
'''

from math import *

def angulo_BAC(a,b):
    # Calculamos el ángulo theta en radianes usando la función atan (arcotangente).
    # La función atan nos permite encontrar el ángulo cuya tangente es a/b.
    
    theta = atan(a/b)
    return theta

#Valores de entrada
a = 2.7
b = 5

#Calculo de angulo en radianes
resultado = angulo_BAC(a, b)
print("Angulo BAC en grados:", resultado)