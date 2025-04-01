'''
NumberToArray0. Dado un número natural n y un número entero v, regresar el arreglo de longitud n tal que todas sus entradas son iguales a v. En otras palabras, construir un arreglo constante de longitud dada y con el valor dado.
Entrada: 6, −14. Salida: [−14, −14, −14, −14, −14, −14]. 
'''

def nuevoArray(n, v):
    """Crea un arreglo con la longitud de v y donde todos los elementos son n.
    
    Args:
        n (int): Longitud deseada
        v (int): Valor a repetir
    
    Returns:
        list: Arreglo resultante
    """

    resultado = []
    for item in range(v):
        resultado.append(n)
    return resultado
    
#valores de entrada

longitud = 6
elemento = -22

print(nuevoArray(elemento, longitud))