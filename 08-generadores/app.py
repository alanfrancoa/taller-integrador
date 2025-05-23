'''
generadores
'''

def generarNumeros(salto):
    i = 0
    while(True):
        yield i #devuelve I y se queda esperando. 
        i += 1 * salto
    
'''
si quisieramos que tuviera un numero desde donde empezar:

def generarNumeros(comienzo, salto):
    i = comienzo
    while(True):
        yield i #devuelve I y se queda esperando. 
        i += 1 * salto
    
si quisieramos que tuviera un fin:

def generarNumeros(comienzo, salto, fin):
    i = comienzo
    while(i < fin):
        yield i #devuelve I y se queda esperando. 
        i += 1 * salto
'''
def generadorVocales():
    yield 'a'
    yield 'e'
    yield 'i'
    yield 'o'
    yield 'u'

gA = generarNumeros(2)
gB = generarNumeros(3)
gC = generarNumeros(10)

generador = generarNumeros()

for x in generador:
    print(x)

g1 = generadorVocales()
g2 = generadorVocales()
g3 = generadorVocales()

a = next(g1)
a = next(g2)
a = next(g3)
a = next(g1)

print(a)