'''
Fun9. Dado un número entero x, regresar el resto al dividir x entre 7.
Sugerencia: encontrar la operación o la función correspondiente en el lenguaje de programación elegido.
Ejemplo. Entrada: 17. Salida: 3.
Ejemplo. Entrada: −40. Salida: 2.
Ejemplo. Entrada: 35. Salida: 0. 
'''

def restoDeSiete (a):
    return a%7

#valores de entrada
numA = 17
numB = -40
numC = 35

#Calculo de resto
resultado = restoDeSiete(numA)
print("Resto de 7:", resultado)

resultado = restoDeSiete(numB)
print("Resto de 7:", resultado)

resultado = restoDeSiete(numC)
print("Resto de 7:", resultado)