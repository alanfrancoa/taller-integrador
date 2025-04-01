# Módulo: main.py
"""Ejemplo de uso de funciones importadas desde un módulo personalizado."""

print("Hola")  # Saludo inicial

# Importa todas las funciones del módulo 'funciones'
from funciones import *

# Obtiene información estadística sobre el número 3
info = info_numero(3)
print(info)  # Imprime el diccionario completo

# Itera sobre cada clave-valor del diccionario y los imprime formateados
for clave in info:
    print(clave + ": " + str(info[clave]))  # Ejemplo: "original: 3"

# Crea una tupla de números para demostrar sumar_todos()
tuplita = (1, 7, 44, 2)
print(sumar_todos(tuplita))  # Imprime la suma: 54

# Usa range() para demostrar que sumar_todos funciona con cualquier iterable
print(sumar_todos(range(2, 12, 2)))  # Imprime la suma de números pares: 30