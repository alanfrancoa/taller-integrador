'''
Cond5. Escribir una función min3 de tres argumentos enteros que regrese el más pequeño de estos tres números. Sugerencia: usar la función min2 del Ejercicio Cond4. 
'''

def minimoDeDos(a, b):
    return a if a < b else b

def minimoDeTres(a, b, c):
    return minimoDeDos(minimoDeDos(a, b), c)

#valores de entrada
print(minimoDeTres(5, 9, 3))  
print(minimoDeTres(-2, 0, 2)) 
print(minimoDeTres(7, 7, 1)) 