

numeros = [4, 3, 2, 7, 8, 1, 12, 5]

def filtroPares(n):
    return n % 2 == 0

def filtroImpares(n):
    return n % 2 != 0


def filter(lista, predicado):
    resultado = []

    for elemento in lista:
        if predicado(elemento): #la funcion va a llegar por parametro
            resultado.append(elemento)
    
    return resultado

x = filter(numeros, filtroPares)
y = filter(numeros, filtroImpares)
print(x)
print(y)