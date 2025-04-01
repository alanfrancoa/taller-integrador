'''
NumberToArray2. Dados un número natural n y un número entero x, regresar el arreglo de longitud n cuyos elementos son los cuadrados de los enteros consecutivos, a partir de x.
Entrada: 7, −4. Salida: [16, 9, 4, 1, 0, 1, 4]. 
'''

def nuevoArray(n, v):
    """Crea un arreglo con la longitud de v y donde todos los elementos son potencia de la longitud, empezando N.
    
    Args:
        n (int): desde que potencia partimos
        v (int): Longitud deseada
    
    Returns:
        list: Arreglo resultante
    """

    resultado = []
    for item in range(v):
        valor = item + n
        resultado.append((valor)**2)
    return resultado
    
#valores de entrada

longitud = 7
elemento = -4

print(nuevoArray(elemento, longitud))