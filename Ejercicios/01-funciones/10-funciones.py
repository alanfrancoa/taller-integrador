'''
 Fun10. Dado un número entero no negativo x, devolver la suma de los últimos dos dígitos de x en el sistema decimal.
Sugerencia: usar el cociente y el resido al dividir entre 10.
Ejemplo. Entrada: 729. Salida: 11.
Ejemplo. Entrada: 688. Salida: 16.
Ejemplo. Entrada: 5. Salida: 5.

'''

def sumaUltimosDigitos (a):
    if a > 0:
        ultimoDigito = a % 10 #extraemos ultimo digito
        aSinUltimoDigito = a // 10 #calculamos el nro sin el ultimo digito
        penuntimoDigito = aSinUltimoDigito % 10 #extraemos el penultimo digito
        return ultimoDigito + penuntimoDigito #retornamos la suma de ambos.
    else:
        return print("Ingrese un nro mayor a 0")
    
#Valores de entrada
numA = 729
numB = 688
numC = 5

resultado = sumaUltimosDigitos(numA)
print("Suma de los dos digitos es:", resultado)
resultado = sumaUltimosDigitos(numB)
print("Suma de los dos digitos es:", resultado)
resultado = sumaUltimosDigitos(numC)
print("Suma de los dos digitos es:", resultado)

