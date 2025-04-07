# Importamos los módulos necesarios
import json  # Para trabajar con datos JSON
import requests  # Para hacer peticiones HTTP

# Definimos la URL base de la API de dinosaurios
urlBase = "https://dinosaur-facts-api.shultzlab.com"

# Hacemos una petición GET a la ruta que devuelve un dinosaurio aleatorio
r = requests.get(urlBase + "/dinosaurs/random")

# Obtenemos el código de estado HTTP de la respuesta
status = r.status_code
# Los códigos más comunes:
# 200 = OK (éxito)
# 404 = No encontrado
# 500 = Error del servidor

# Obtenemos el contenido completo de la respuesta como texto
contenido = r.text  # Esto será un string en formato JSON

# Imprimimos el código de estado para verificar si la petición fue exitosa
print(status)

# Imprimimos el contenido crudo de la respuesta (texto JSON)
print(contenido)

# Convertimos el texto JSON a un diccionario de Python
json_dino = json.loads(contenido)  # 'loads' = load string (de JSON a Python)

# Accedemos a la clave "Name" del diccionario para obtener el nombre del dinosaurio
print(json_dino["Name"])
