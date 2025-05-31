def crear_multiplicador(m):
    def inner(num): #la funcion que devuelve. 
        return num*m
    return inner #retornamos la funcion

triplicar = crear_multiplicador(3) 

print(triplicar)

print(triplicar)

print(triplicar(6)) #18

print(crear_multiplicador(4)(2)) #8