'''
Listas en Python
Las listas son estructuras de datos que permiten almacenar múltiples elementos en una sola variable.
Son similares a los arrays en otros lenguajes, pero con más flexibilidad.
'''

# Definimos una lista llamada 'vecty' con los elementos 1, 2, 3, 4, 5
vecty = [1, 2, 3, 4, 5]

# Añadimos un nuevo elemento al final de la lista usando el método append()
# Similar al método add() en otros lenguajes
vecty.append(6)

# Accedemos a los elementos de la lista por su índice
print(vecty[0])  # Muestra el primer elemento: "1"
print(vecty[-1])  # Muestra el último elemento: "6" (índices negativos cuentan desde el final)
print(vecty[-2])  # Muestra el penúltimo elemento: "5"

# Slicing (rebanado) de listas
print(vecty[1:3])  # Muestra desde el índice 1 hasta el 3 (sin incluir el 3): [2, 3]
print(vecty[:3])   # Muestra desde el inicio hasta el índice 3 (sin incluir el 3): [1, 2, 3]
print(vecty[:-3])  # Muestra desde el inicio hasta el tercer elemento desde el final (sin incluirlo): [1, 2, 3]

print("--------------------------------------")

# Slicing con paso: [inicio:fin:paso]
print(vecty[::2])  # Muestra los elementos de la lista de dos en dos: [1, 3, 5]
# Esto no modifica la lista original, solo crea una nueva lista temporal para la operación

# Mostramos la lista original para confirmar que no ha sido modificada
print(vecty)

# RECOMENDACIÓN: Ver métodos de listas en la documentación oficial de Python para más funcionalidades.

# Iteración sobre la lista usando un bucle for (en Python, solo existe el foreach)
for x in vecty:
    print(x)

print("--------------------------------------")

# Uso de la función range() para generar una secuencia de números
# range(inicio, fin, paso) -> genera números desde 'inicio' hasta 'fin-1', con un incremento de 'paso'
rango = range(3, 20, 2)  # Genera números del 3 al 19, de dos en dos: 3, 5, 7, ..., 19

# Iteramos sobre el rango y mostramos cada número
for x in rango:
    print(x)

# Definición de funciones en Python
def suma(a, b):
    '''
    Función que recibe dos parámetros (a y b) y retorna su suma.
    '''
    return a + b

# RECOMENDACIÓN: Hacer guía de trabajos prácticos para ya subida al aula virtual. 