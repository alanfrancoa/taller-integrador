'''
NumberToArray4. Dado un número natural n, regresar el arreglo de longitud n cuyos elementos son los factoriales de los primeros números naturales. Sugerencia: utilizar la fórmula recursiva para la función factorial.
Entrada: 5. Salida: [1, 1, 2, 6, 24]. 
'''

def nuevoArray (v):
    """Crea un arreglo con la longitud de v, donde el contenido son los factoriales del indice.
    
    Args:

        v (int): Longitud deseada
    
    Returns:
        list: Arreglo resultante
    """
    resultado = [] 
    factorial = 1 
    for i in range(1, v-1):
        resultado.append(i*factorial)
        factorial *= i
    return resultado

#valores de entrada

longitud = 7

print(nuevoArray( longitud))