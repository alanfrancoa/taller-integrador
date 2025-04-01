'''
NumberToArray5. Dado un número natural n, regresar el arreglo de longitud n cuyos elementos son los números 1 (en posiciones pares) y −1 (en posiciones impares).
Entrada: 5. Salida: [1, −1, 1, −1, 1]. 
'''

def nuevoArray (n):
    resultado = []

    for item in range(n):
        if item % 2 == 0:
            resultado.append(1)
        else:
            resultado.append(-1)
    return resultado

#valores de entrada
longitud = 7

print(nuevoArray(longitud))