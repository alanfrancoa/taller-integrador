'''
NumberToBool1. Determinar si el número entero dado es estrictamente menor que 7.
Ejemplo. Entrada: 5. Salida: True.
Ejemplo. Entrada: 7. Salida: False.
Ejemplo. Entrada: 82. Salida: False.
Ejemplo. Entrada: −31. Salida: True. 
'''

def menorASiete(a):
    if isinstance(a, int):
        return a < 7
    else:
        print("Solo se admiten numeros enteros")
        return False
    
#valores de entrada
numA = 5
numB = 7
numC = 82
numD = -31

resultado = menorASiete(numA)
print("El numero", numA, "es menor a 7?", str(resultado))

resultado = menorASiete(numB)
print("El numero", numB, "es menor a 7?", str(resultado))

resultado = menorASiete(numC)
print("El numero", numC, "es menor a 7?", str(resultado))

resultado = menorASiete(numD)
print("El numero", numD, "es menor a 7?", str(resultado))