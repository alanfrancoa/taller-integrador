'''
NumberToArray6. Dado un número natural n y dos números enteros a y d, regresar el arreglo de longitud n que contiene los primeros n elementos de la progresión aritmética con el valor inicial a y la diferencia (incremento) d.
Entrada: 5, −3, 11. Salida: [−3, 8, 19, 30, 41].
Entrada: 4, 20, −15. Salida: [20, 5, −10, −25].
Entrada: 0, 5, −3. Salida: []. 
'''

def nuevoArray (n, a, d):
    """
    Crea un arreglo con la longitud de n, empezando desde a, haciendo progresion en base a d.
    Args:
        n (int): longitud arreglo
        a (int): Punto de partida
        b (int): Progresion aritmetica
    
    Returns:
        list: Arreglo resultante
    """

    resultado = []

    partida = a
    progresion = d

    for item in range(n):
        resultado.append(partida)
        partida += progresion
    
    return resultado

#Prueba

print(nuevoArray(5, -3, 11))
print(nuevoArray(4, 20, -15))
print(nuevoArray(0, 5, -3))