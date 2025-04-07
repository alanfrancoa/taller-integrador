# Trabajando con JSON en Python
import json  # Importamos el módulo json para trabajar con formato JSON

# Primer método: convertir diccionario a JSON string y luego guardar
dic_perrito1 = {"nombre": "Pippo", "edad": 1}  # Creamos un diccionario Python

# Convertimos el diccionario a una cadena JSON (serialización)
# dumps = "dump string" - convierte a string JSON
json_perrito = json.dumps(dic_perrito1)  

# Guardamos el string JSON en un archivo
with open("perrito1.json", "w") as f:  # Abrimos en modo escritura ('w')
    f.write(json_perrito)  # Escribimos el string JSON en el archivo

# Segundo método: guardar directamente diccionario como JSON
dic_perrito2 = {"nombre": "Chicho", "edad": 7}  # Otro diccionario

# Usamos json.dump() para guardar directamente en el archivo
# dump (sin 's') escribe directamente en un file object
with open("perrito2.json", "w") as f:  # Abrimos segundo archivo
    json.dump(dic_perrito2, f)  # Convierte y escribe en un solo paso

print("fin")  # Mensaje de finalización