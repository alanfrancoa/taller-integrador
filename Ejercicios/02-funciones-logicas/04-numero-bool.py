'''
NumberToBool4. Determinar si el número entero dado es impar.
Sugerencia: en el lenguaje de programación elegido encontrar la operación o función que regresa el resto al dividir un número entre otro.
Ejemplo. Entrada: 5. Salida: True.
Ejemplo. Entrada: −44. Salida: False.
Ejemplo. Entrada: 0. Salida: False.
Ejemplo. Entrada: 466. Salida: False. 
'''

def esImpar(a):
    return a % 2 != 0

#valores de entrada:
numA = 5
numB = -44
numC = 0
numD = 466 

print("El numero: "+str(numA)+ " es impar? " + str(esImpar(numA)))
print("El numero: "+str(numB)+ " es impar? " + str(esImpar(numB)))
print("El numero: "+str(numC)+ " es impar? " + str(esImpar(numC)))
print("El numero: "+str(numD)+ " es impar? " + str(esImpar(numD)))