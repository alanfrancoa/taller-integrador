# Python, al igual que JavaScript, tiene funciones.
# A diferencia de lenguajes como Java o C#, en Python no es necesario que las funciones pertenezcan a una clase.

# Ejemplo básico de impresión en consola
print("Hola Mundo")

# Python se ejecuta en consola. Por ejemplo, puedes ejecutar este script con el comando:
# py app.py

# Definición de una variable con tipo (aunque Python es de tipado dinámico)
num: int = 4  # Aunque se define como entero, Python permite asignar otros tipos de datos.

# Ejemplo de concatenación de cadenas y números
# print("El código es: " + num)  # Esto causaría un error, ya que no se pueden concatenar cadenas con enteros directamente.
print("El código es: " + str(num))  # Convertimos el número a cadena para concatenar correctamente.

# Los errores en Python pueden ser silenciosos o no ser explícitos, por lo que es importante ser cuidadoso.
# La flexibilidad de Python puede ser un arma de doble filo si no se maneja con precaución.

# Uso de condicionales para verificar tipos de datos y realizar acciones específicas.
# Esto es común en Python debido a su tipado dinámico.

# Solicitud de entrada al usuario
respuesta = input("¿Cuál es tu nombre? :")  # input() siempre retorna un string.
print("Hola " + respuesta)

respuesta = input("¿Cuál es tu edad? :") 
edad = int(respuesta)  # Convertimos la entrada a entero usando la función int().
print("El doble de tu edad es: ")
print(edad * 2)  # Mostramos el doble de la edad.

# Python permite reasignar variables con diferentes tipos de datos, lo que puede ser peligroso si no se maneja con cuidado.
num = "cuatro"  # Ahora 'num' es una cadena, no un número.

# Estructura condicional para verificar la edad
if edad >= 65:
    # pass  # 'pass' es una declaración nula, similar a dejar un bloque vacío en otros lenguajes.
    print("Te puedes jubilar, aprovecha antes de que haya una reforma laboral. ¡AUUUUUUUn't!")
    print(":)") 
elif edad < 0:
    print("Todavía no has nacido.")
else:
    print("No puedes jubilarte, sigue aportando, contribuyente.")
print("The end")  # Esta línea se ejecuta siempre, independientemente de la condición.

# Consejos para la indentación en Python:
# - Para tabular: Presiona TAB.
# - Para eliminar una tabulación: Presiona Shift + Tab.


#las funciones son ciudadanos de primer orden -> objeto reservado que apunta a una funcion

mostrar = print #no me refiero a la ejecucion de la funcion, me refiero a la funcion en si. s
#mostrar = print() -> mostrar va a dar lo que retorna la funcion print, en este caso seria NONE (null), es la ejecucion

mostrar("Hola bombon, dame una docena de sorrentinos de salmon auuuuuuuuu")

