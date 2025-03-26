'''
NumberToBool2. Dados tres números enteros a, b, x, determinar si x es mayor o igual al número a y al mismo tiempo estrictamente menor que b. En otras palabras, determinar si el número x pertenece al intervalo [a, b[.
Observación: si a ≥b, entonces para cualquier x la función debe regresar False.
Ejemplo. Entrada: 3, 32, 20. Salida: True.
Ejemplo. Entrada: −7, 40, 43. Salida: False.
Ejemplo. Entrada: 40, 6, 30. Salida: False. 
'''

def intervalo (a, b, x):
    if a>=b:
        return False
    elif (a <= x < b):
        return True
    else:
        return False
    
#valores de entrada:
print(intervalo(3, 32, 20))   # True (20 está en [3, 32))
print(intervalo(-7, 40, 43))  # False (43 no está en [-7, 40))
print(intervalo(40, 6, 30))   # False (a >= b, retorna False directamente)