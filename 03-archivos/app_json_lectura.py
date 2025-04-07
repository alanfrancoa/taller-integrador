# Importamos el módulo json para trabajar con datos JSON
import json

# --------------------------
# PRIMER MÉTODO: usando read() + loads()
# --------------------------
with open("perrito1.json", "r") as f:  # Abrimos el archivo en modo lectura
    # Leemos todo el contenido del archivo como un string
    json_perrin = f.read()  
    # Convertimos el string JSON a un diccionario de Python
    p1 = json.loads(json_perrin)  # 'loads' = load string

# Accedemos a la clave 'edad' del diccionario resultante
print(p1["edad"])

'''
Diferencia entre load() y loads():
    • Usar LOADS cuando:
      - Ya tienes el contenido JSON como string en memoria
      - Ejemplo: respuesta de una API, texto generado manualmente
    
    • Usar LOAD cuando:
      - Tienes un archivo JSON legible (objeto file)
      - Es más directo y eficiente para leer archivos
'''

# --------------------------
# SEGUNDO MÉTODO: usando load() directamente
# --------------------------
with open("perrito2.json", "r") as f:  # Abrimos el segundo archivo
    # Convertimos directamente el archivo JSON a diccionario
    p2 = json.load(f)  # 'load' trabaja con objetos archivo

# Accedemos a la clave 'nombre' del segundo diccionario
print(p2["nombre"])

# --------------------------
# MEJORES PRÁCTICAS ADICIONALES:
# --------------------------
# 1. Siempre especificar la codificación (utf-8 es estándar para JSON):
#    with open("archivo.json", "r", encoding="utf-8") as f:

# 2. Manejar posibles errores con try-except:
#    try:
#        with open("archivo.json", "r") as f:
#            data = json.load(f)
#    except FileNotFoundError:
#        print("El archivo no existe")
#    except json.JSONDecodeError:
#        print("Error en el formato JSON")

# 3. Para archivos grandes, considerar cargas parciales
#    o procesamiento por líneas si son JSON lines (.jsonl)