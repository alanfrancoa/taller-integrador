'''
Fun2. Escribir una función de dos argumentos x, y que devuelva su diferencia x − y.
Ejemplo. Entrada: 5, 18. Salida: −13.
Ejemplo. Entrada: 32, −5. Salida: 37. 
'''

def diferencia (a, b):
    return a - b

numA = 5
numB = 18
print(str(numA) + " - " + str(numB) + " = " + str(diferencia(numA, numB)))

numA = 32
numB = -5
print(str(numA) + " - " + str(numB) + " = " + str(diferencia(numA, numB)))
