# Ejemplo de contextos en Python con una funcion flexible y valor dinamico

# En este ejemplo, la variable numero queda fuera de la funcion crear_funcion, y seguira tomando el valor f1 y de f2.
numero = 5 

def crear_funcion():
    def f():
        print(numero)
    return f

# En este ejemplo, la variable numero es global y se usa dentro de la función f.
# def crear_funcion():
#     x = numero * 2
#     def f():
#         print(numero)
#     return f


# contexto y asociación de variables
f1 = crear_funcion(1)
f2 = crear_funcion(2)
