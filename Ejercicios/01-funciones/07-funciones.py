'''
Fun7. Dados tres números a, b, c, regresar la longitud de la diagonal del paralelogramo cuyos lados tienen longitudes a, b, c.
Entrada: −2.5, 0.3, −1.9. Salida: 3.1532620591175. 
'''
from math import *

def diagonalParalelepipedo(a, b, c):
    return sqrt(pow(a,2) + pow(b, 2) + pow(c, 2))
'''
La diagonal de un paralelepípedo es la hipotenusa de un triángulo rectángulo en 3D, 
y la fórmula es una extensión del Teorema de Pitágoras a tres dimensiones.
'''

numA = -2.5
numB = 0.3
numC = -1.9

print("La diagonal del paralelepipedo es: " + str(diagonalParalelepipedo(numA, numB, numC)))