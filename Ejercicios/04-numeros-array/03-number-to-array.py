'''
NumberToArray3. Dado un número natural n, regresar el arreglo a de longitud n cuyos elementos son las primeras potencias de 2, a partir de la potencia 0. Sugerencia: utilizar la fórmula recursiva para las potencias de 2. En otras palabras, para cada j con j ≥1, expresar a[j] a través de a[j − 1].
Entrada: 5. Salida: [1, 2, 4, 8, 16]. 
'''

def nuevoArray(v):
    """Crea un arreglo con la longitud de v, y potencias de dos.
    
    Args:

        v (int): Longitud deseada
    
    Returns:
        list: Arreglo resultante
    """

    resultado = []
    valor = 1 #empezamos en 2 a la potencia de 0 = 1
    for item in range(v):
        resultado.append(valor)
        valor *= 2
    return resultado
    
#valores de entrada

longitud = 5


print(nuevoArray(longitud))