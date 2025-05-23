'''
una funcion puede crear funciones
'''
def crearFuncionSuma():
    def suma(a, b):
        return a+b
    
    return suma
    

xd = crearFuncionSuma()

print(1)

x = xd(1, 3)
y = crearFuncionSuma()(5, 7) #funcion descartable.

print(x)

#LAS FUNCIONES EN PYTHON SON CIUDADANOS DE PRIMER ORDEN.-
