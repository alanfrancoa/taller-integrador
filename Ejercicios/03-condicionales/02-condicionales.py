'''
Cond2. Escribir una función max2 de dos argumentos enteros que regrese el más grande de estos dos números. Ejemplo. Entrada: 70, −43. Salida: 70.
Ejemplo. Entrada: −23, −10. Salida: −10. Ejemplo. Entrada: −42, 35. Salida: 35. Ejemplo. Entrada: −17, −17. Salida: −17. 
'''

def maximoDeDos (a, b):
    return a if a > b else b

#valores de entrada

numA = -23
numB = -10

numC = -42
numD = 35

numE = -17
numF = -17

print("Numeros ingresados: "+ str(numA) +" y "+str(numB)+ " Maximo: " + str(maximoDeDos(numA, numB)))
print("Numeros ingresados: "+ str(numC) +" y "+str(numD)+ " Maximo: " + str(maximoDeDos(numC, numD)))
print("Numeros ingresados: "+ str(numE) +" y "+str(numF)+ " Maximo: " + str(maximoDeDos(numE, numF)))