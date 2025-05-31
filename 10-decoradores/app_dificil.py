def agregar_print_auto(func):
    def inner (n1, n2):
        x = func(n1, n2)
        print(f"Se ejecuto con {n1} y {n2}, el resultado es {x}")
        return x    
    return inner #esta funcion retorna lo que haga y le agrega el print automaticamente. 

def suma(a, b):
    return a+b

suma_con_print = agregar_print_auto(suma)

def resta(a, b):
    return a - b

resta_con_print = agregar_print_auto(resta)

suma_con_print(1, 7)  # Esto imprimirá 8 y retornará 8

suma_con_print(10, 20)  # Esto imprimirá 30 y retornará 30

resta_con_print(10, 5)  # Esto imprimirá 5 y retornará 5

@agregar_print_auto # Decorador aplicado a la función multiplicar
def multiplicar(a, b):
    return a * b

'''
uso vs creacion del decorador
no nos importa lo que hace por dentro
sino su funcionamiento
'''

def masivo_bro(func):
    def inner(lista):
        resultado = []
        for x in lista:
            resultado.append(func(x))
        return resultado
    return inner
    


@masivo_bro
def duplicar(a):
    return a*2

v = [1, 2, 3, 4]

print(duplicar(v))