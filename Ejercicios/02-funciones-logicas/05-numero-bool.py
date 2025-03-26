'''
NumberToBool5. Determinar si el número entero dado es un múltiplo de 3. En otras palabras, dado un número entero a, regresar True si a es un múltiplo de 3; regresar False en otro caso. Sugerencia: en el lenguaje de programación elegido encontrar la operación o función que regresa el resto al dividir un número entre otro.
Ejemplo. Entrada: 18. Salida: True.
Ejemplo. Entrada: −42. Salida: True.
Ejemplo. Entrada: −71. Salida: False.
Ejemplo. Entrada: 0. Salida: True. 
'''

def multiploDeTres(a):
    return a%3 == 0

#valores de entrada
numA = 18
numB = -42
numC = -71
numD = 0


print("El numero: "+str(numA)+ " es multiplo de 3? " + str(multiploDeTres(numA)))
print("El numero: "+str(numB)+ " es multiplo de 3? " + str(multiploDeTres(numB)))
print("El numero: "+str(numC)+ " es multiplo de 3? " + str(multiploDeTres(numC)))
print("El numero: "+str(numD)+ " es multiplo de 3? " + str(multiploDeTres(numD)))