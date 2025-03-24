'''
NumberToBool0. Determinar si el número entero dado es positivo. En otras palabras, escribir una función de un argumento entero; si el número dado es positivo, la función debe regresar True; en otro caso la función debe regresar False.
Ejemplo. Entrada: 8. Salida: True.
Ejemplo. Entrada: 53. Salida: True.
Ejemplo. Entrada: 0. Salida: False.
Ejemplo. Entrada: −4. Salida: False.
Ejemplo. Entrada: −70. Salida: False. 
'''

def positivo (a):
    if isinstance(a, int):
        return a > 0
    else:
        print("Solo se admiten numeros enteros")
        return False
    
    
#valores de entrada
numA = 8
numB = 53
numC = 0
numD = -4
numE = -7.2

resultado = positivo(numA)
print("El numero", numA, "es positivo?", str(resultado))

resultado = positivo(numB)
print("El numero", numB, "es positivo?", str(resultado))

resultado = positivo(numC)
print("El numero", numC, "es positivo?", str(resultado))

resultado = positivo(numD)
print("El numero", numD, "es positivo?", str(resultado))

resultado = positivo(numE)
print("El numero", numE, "es positivo?", str(resultado))
