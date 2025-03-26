'''
Cond0. Dado un número entero, regresar su valor absoluto. Sugerencia: usar la expresión condicional o el operador condicional.
Ejemplo. Entrada: −17. Salida: 17.
Ejemplo. Entrada: 63. Salida: 63.
Ejemplo. Entrada: 0. Salida: 0.
'''

def absoluto(a):
    return a if a  >= 0 else -a

#valores de entrada
numA = -17 
numB = 63
numC = 0

print("Numero: "+str(numA)+ " | valor absoluto: " + str(absoluto(numA)))
print("Numero: "+str(numB)+ " | valor absoluto: " + str(absoluto(numB)))
print("Numero: "+str(numC)+ " | valor absoluto: " + str(absoluto(numC)))
