'''
NumberToBool3. Determinar si el número entero dado es par.
Sugerencia: en el lenguaje de programación elegido encontrar la operación o función que regresa el resto al dividir un número entre otro.
Ejemplo. Entrada: 5. Salida: False.
Ejemplo. Entrada: −44. Salida: True.
Ejemplo. Entrada: 0. Salida: True.
Ejemplo. Entrada: 466. Salida: True. 
'''

def esPar(a):
    return a % 2== 0

#valores de entrada:
numA = 5
numB = -44
numC = 0
numD = 466 

print("El numero: "+str(numA)+ " es par? " + str(esPar(numA)))
print("El numero: "+str(numB)+ " es par? " + str(esPar(numB)))
print("El numero: "+str(numC)+ " es par? " + str(esPar(numC)))
print("El numero: "+str(numD)+ " es par? " + str(esPar(numD)))