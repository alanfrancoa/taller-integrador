# Importamos los módulos necesarios para trabajar con JSON y peticiones HTTP
import json
import requests

# Definimos la URL base de la API de dinosaurios
urlBase = "https://dinosaur-facts-api.shultzlab.com"

# Realizamos una petición GET para obtener todos los dinosaurios
r = requests.get(urlBase + "/dinosaurs")

# Convertimos la respuesta JSON directamente a una lista de Python
# La anotación de tipo ":list" es opcional y solo para ayuda en el autocompletado del IDE
listaDinos: list = r.json()  # Equivalente a json.loads(r.text) pero más eficiente

# Iteramos sobre cada dinosaurio en la lista
for dino in listaDinos:
    # Imprimimos el nombre del dinosaurio
    # Usamos f-strings (formato más moderno y legible)
    print(f"Nombre: {dino['Name']}")
    
    # Imprimimos la descripción del dinosaurio
    print(f"Descripción: {dino['Description']}")  # Corregido el texto "Nombre" por "Descripción"
    
    # Línea separadora para mejor legibilidad entre dinosaurios
    print("-" * 50)

# --------------------------
# MEJORAS Y BUENAS PRÁCTICAS:
# --------------------------

# 1. Manejo de errores recomendado
"""
try:
    r = requests.get(urlBase + "/dinosaurs", timeout=5)
    r.raise_for_status()  # Lanza excepción para códigos 4XX/5XX
    listaDinos = r.json()
    
    for dino in listaDinos:
        print(f"Nombre: {dino.get('Name', 'Desconocido')}")
        print(f"Descripción: {dino.get('Description', 'No disponible')}\n")
        
except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la API: {e}")
except json.JSONDecodeError:
    print("Error al decodificar la respuesta JSON")
except KeyError as e:
    print(f"Error: Falta clave en los datos - {e}")
"""

# 2. Uso de .get() para evitar KeyError
"""
# Es más seguro que dino["Name"] porque provee un valor por defecto
print(f"Nombre: {dino.get('Name', 'Nombre no disponible')}")
"""

# 3. Consideraciones adicionales
# - Podríamos agregar parámetros a la petición (headers, auth, etc.)
# - Para APIs grandes, implementar paginación
# - Cachear respuestas para no saturar la API
# - Usar logging en lugar de print para producción