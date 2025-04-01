def suma(a, b):
    """Suma dos números y retorna el resultado.
    
    Args:
        a (int, float): Primer operando de la suma
        b (int, float): Segundo operando de la suma
    
    Returns:
        int, float: Resultado de la operación a + b
    
    Examples:
        >>> suma(3, 5)
        8
        >>> suma(10.5, 2.3)
        12.8
    """
    return a + b


def info_numero(num):
    """Genera un diccionario con propiedades matemáticas de un número.
    
    Args:
        num (int, float): Número a analizar
    
    Returns:
        dict: Diccionario con:
            - original (int, float): Número original
            - cuadrado (int, float): Número elevado al cuadrado
            - doble (int, float): Número multiplicado por 2
            - es_par (bool): True si el número es par
            - negativo (int, float): Versión negativa del número
    
    Notes:
        - Para números negativos, el campo 'negativo' será positivo
        - El 0 se considera par
    
    Examples:
        >>> info_numero(3)
        {
            'original': 3,
            'cuadrado': 9,
            'doble': 6,
            'es_par': False,
            'negativo': -3
        }
    """
    return {
        "original": num,
        "cuadrado": num ** 2,
        "doble": num * 2,
        "es_par": num % 2 == 0,
        "negativo": -num
    }


def sumar_todos(iterable):
    """Acumula la suma de todos los elementos en un iterable.
    
    Args:
        iterable (list, tuple, set): Contenedor con elementos numéricos
    
    Returns:
        int, float: Suma total de los elementos
    
    Raises:
        TypeError: Si el input no es un iterable
        ValueError: Si el iterable contiene elementos no numéricos
    
    Examples:
        >>> sumar_todos([1, 2, 3])
        6
        >>> sumar_todos((1.5, 2.5, 3.5))
        7.5
    """
    if not hasattr(iterable, '__iter__'):
        raise TypeError("Se esperaba un objeto iterable")
    
    total = 0
    for elemento in iterable:
        if not isinstance(elemento, (int, float)):
            raise ValueError("Todos los elementos deben ser numéricos")
        total += elemento
    
    return total