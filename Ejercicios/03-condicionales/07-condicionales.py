'''
Cond7. Están dados dos números enteros, a y b. Hagamos un análisis de la ecuación lineal a x = b, donde la incógnita x puede ser un número racional. Si la ecuación tiene una única solución, entonces regresar 1. Si la ecuación no tiene solución, entonces regresar 0. Si la ecuación tiene más de una solución, entonces regresar 2.
Ejemplo. Entrada: 70, −37. Salida: 1. Ejemplo. Entrada: 0, 56. Salida: 0. Ejemplo. Entrada: 0, 0. Salida: 2. 
'''

def analizar_ecuacion(a, b):
    # Primero verificamos si el coeficiente 'a' es diferente de cero
    if a != 0:
        # Caso 1: Solución única
        # Cuando a ≠ 0, la ecuación tiene exactamente una solución x = b/a
        # Ejemplo: 70x = -37 → x = -37/70 (solución única)
        return 1  # Retornamos 1 indicando que hay una única solución
    
    # Si a = 0, verificamos el valor de 'b'
    elif b != 0:
        # Caso 2: Sin solución
        # Cuando a = 0 y b ≠ 0, la ecuación es 0 = b (contradicción)
        # Ejemplo: 0x = 56 → 0 = 56 (no tiene solución)
        return 0  # Retornamos 0 indicando que no hay solución
    
    else:
        # Caso 3: Infinitas soluciones
        # Cuando a = 0 y b = 0, la ecuación es 0 = 0
        # Esto se cumple para cualquier valor de x (infinitas soluciones)
        # Ejemplo: 0x = 0 → todos los números reales son solución
        return 2  # Retornamos 2 indicando infinitas soluciones

# Ejemplos de prueba:

# Caso 1: Solución única (a ≠ 0)
# Ecuación: 70x = -37 → x = -37/70
print(analizar_ecuacion(70, -37))  # Salida: 1

# Caso 2: Sin solución (a = 0, b ≠ 0)
# Ecuación: 0x = 56 → 0 = 56 (falso)
print(analizar_ecuacion(0, 56))    # Salida: 0

# Caso 3: Infinitas soluciones (a = 0, b = 0)
# Ecuación: 0x = 0 → 0 = 0 (siempre verdadero)
print(analizar_ecuacion(0, 0))     # Salida: 2