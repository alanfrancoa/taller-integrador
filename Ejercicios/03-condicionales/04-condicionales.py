'''
Cond4. Escribir una función min2 de dos argumentos enteros que regrese el más pequeño de estos dos números. Ejemplo. Entrada: 70, −43. Salida: 43.
Ejemplo. Entrada: −23, −10. Salida: −23. Ejemplo. Entrada: −42, 35. Salida: −42. Ejemplo. Entrada: −17, −17. Salida: −17. 
'''

def minimoDeDos(a, b):
    return a if a < b else b

numA = -23
numB = -10

numC = -42
numD = 35

numE = -17
numF = -17


print("Numeros ingresados: "+ str(numA) +" y "+str(numB)+ " Minimo: " + str(minimoDeDos(numA, numB)))
print("Numeros ingresados: "+ str(numC) +" y "+str(numD)+ " Minimo: " + str(minimoDeDos(numC, numD)))
print("Numeros ingresados: "+ str(numE) +" y "+str(numF)+ " Minimo: " + str(minimoDeDos(numE, numF)))