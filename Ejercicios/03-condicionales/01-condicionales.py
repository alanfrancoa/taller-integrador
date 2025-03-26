'''
Cond1. Dado un número entero a, regresar su parte positiva. En otras palabras, si a es mayor o igual a cero, entonces regresar el mismo número a; en otro caso regresar el número cero.
Ejemplo. Entrada: −20. Salida: 0.
Ejemplo. Entrada: 38. Salida: 38. 
'''

def partePositiva(a):
    return a if a >=0 else 0

#valores de entrada
numA = -20
numB = 38


print("Numero: "+str(numA)+ " | Parte positiva: " + str(partePositiva(numA)))
print("Numero: "+str(numB)+ " | Parte positiva: " + str(partePositiva(numB)))

