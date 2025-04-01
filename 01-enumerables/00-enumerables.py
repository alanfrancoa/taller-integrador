# Creación de un rango (range) que genera números del 0 al 99998 (99999 no incluido)
# IMPORTANTE: range() es un objeto de tipo "lazy" que genera los números bajo demanda
# No ocupa memoria para todos los valores al crearlo, sino que los calcula cuando se iteran
mi_rango = range(0, 99999)

print("Hola")  # Mensaje inicial

# Conversión PELIGROSA del rango a lista (genera todos los números en memoria)
# Esto consumiría ~800KB de RAM (99,999 números * 8 bytes c/u)
# En sistemas con poca memoria podría colgarse o ser muy lento
mi_lista = list(mi_rango)  # ¡Cuidado! Esto materializa todos los valores en memoria

# Iteración eficiente sobre el rango original (sin convertir a lista)
# range() sigue siendo óptimo porque genera cada número bajo demanda
for x in mi_rango:
    if x % 100 == 0:  # Filtramos múltiplos de 100
        print(x)  # Nota: Las operaciones de I/O (como print) son lentas en bucles grandes

# Creación de una tupla con números pares del 2 al 8 (paso 2)
# Las tuplas son inmutables (no se pueden modificar después de crearse)
# range(2, 10, 2) genera: 2, 4, 6, 8 (10 no incluido)
mi_tupla = tuple(range(2, 10, 2))

print(mi_tupla)  # Salida: (2, 4, 6, 8)
print("Fin")  # Mensaje final