'''
Fun0. Escribir una función de un argumento entero a que calcule y regrese el cubo de a.
Ejemplo. Entrada: −11. Salida: −1331.
Ejemplo. Entrada: 5. Salida: 125.
'''

def cubo ( a):
    return a**3

num = -11
res = cubo(num)
print("El nro es: " + str(num) + " su cubo es: " + str(res))

num = 5
res = cubo(num)
print("El nro es: " + str(num) + " su cubo es: " + str(res))