'''
Cond3. Escribir una función max3 de tres argumentos enteros que regrese el más grande de estos tres números. Sugerencia: usar la función max2 del Ejercicio Cond2. 
'''

def maximoDeDos (a, b):
    return a if a > b else b


def maximoDeTres(a,b,c):
        return maximoDeDos(maximoDeDos(a, b), c)

#valores de entrada
print(maximoDeTres(5, 9, 3))  
print(maximoDeTres(-2, 0, 2)) 
print(maximoDeTres(7, 7, 1)) 