'''
NumberToArray1. Dado un número natural n, regresar el arreglo de longitud n cuyos elementos son los cuadrados de los primeros números naturales.
Entrada: 5. Salida: [0, 1, 4, 9, 16]. 
'''

def nuevoArray(n):
    """Dado un número natural n, regresa el arreglo de longitud n cuyos elementos son los cuadrados de los primeros números naturales.
    
    Args:
        n (int): Longitud deseada

    
    Returns:
        list: Arreglo resultante
    """

    resultado = []
    for item in range(n):
        resultado.append(item**2)
    return resultado
    
#valores de entrada

longitud = 6


print(nuevoArray(longitud))