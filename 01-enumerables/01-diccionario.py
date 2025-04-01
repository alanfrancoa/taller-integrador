# Creación de un diccionario vacío usando dict()
diccionario = dict()  # Equivalente a diccionario = {}

# Añadiendo elementos al diccionario (clave: valor)
# Las claves son sensibles a mayúsculas/minúsculas (case sensitive)
diccionario["gato"] = "Felino chiquito de cuatro patas."
diccionario["perro"] = "Canino mediano de cuatro patas."  # "perro" ≠ "Perro" (son claves diferentes)

# Accediendo a un valor mediante su clave
print(diccionario["gato"])  # Imprime: "Felino chiquito de cuatro patas."

# Imprimiendo todo el diccionario
print(diccionario)  # Muestra {'gato': 'Felino...', 'perro': 'Canino...'}

# Otra forma de crear diccionarios (con datos iniciales)
numerines = {
    2: "dos",  # Las claves pueden ser números
    3: "tres"
} 
print(numerines)  # Imprime {2: 'dos', 3: 'tres'}

# Diccionario anidado (contiene otro diccionario y lista)
auto = {
    "patente": "AB345FY",  # Clave string, valor string
    "marca": "Ford",
    "modelo": "Escort",
    "Velocidad": 120.5,  # Clave string, valor float
    "multas": [100, 8000, 10000],  # Clave string, valor lista
    "dueno": {  # Clave string, valor diccionario
        "nombre": "Juan Domingo",
        "apellido": "Peron",
        "edad": 31  # Clave string, valor int
    }
}

# Accediendo a un valor en diccionario anidado
edad = auto["dueno"]["edad"]  # Primero accede a "dueno", luego a "edad"

# Concatenando string con número (necesita conversión con str())
print("La edad del dueño es: " + str(edad))  # Imprime: "La edad del dueño es: 31"