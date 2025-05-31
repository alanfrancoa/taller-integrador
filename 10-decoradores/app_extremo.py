
from random import Random

'''

'''
def regalar_random(func):
    r = Random()
    def inner(x):
        random = r.randint(0,10)
        return func(x, random)
    return inner

def regalar_random_fijo(func): 
    r = Random()
    random = r.randint(0,10)
    def inner(x):
        return func(x, random)
    return inner


@regalar_random #este decorador te da un parametro, num aleatorio.
def suma_random(x, rand):
    return x + rand

@regalar_random_fijo
def resta_random_f(y, rand):
    return y - rand

print(suma_random(3))

print(resta_random_f(7))
print(resta_random_f(8))
print(resta_random_f(9))