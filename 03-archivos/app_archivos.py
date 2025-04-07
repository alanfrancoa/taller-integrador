# Definimos el texto que escribiremos en el archivo
texto = "hola"

# UTILIZANDO LA SENTENCIA WITH (MANEJO SEGURO DE ARCHIVOS)
# with crea un contexto que maneja automáticamente el cierre del archivo
# incluso si ocurren excepciones durante la operación
with open("archivito.txt", "w") as f:
    # 'w' -> modo escritura (Write)
    # Si el archivo existe, lo sobrescribe
    # Si no existe, lo crea
    
    # Escribimos el contenido en el archivo
    f.write(texto)  # Escribe la cadena 'hola' en el archivo

# Al salir del bloque with, el archivo se cierra automáticamente
# Esto ocurre gracias al protocolo de manejo de contexto de Python

# ----------------------------------------------------------
# COMPARACIÓN CON EL MÉTODO TRADICIONAL (NO RECOMENDADO):
# f = open("archivito.txt", "w")  # Abre el archivo en modo escritura
# try:
#     f.write(texto)
# finally:
#     f.close()  # Se debe cerrar manualmente
# ----------------------------------------------------------

# Ventajas del método with:
# 1. Cierre automático garantizado
# 2. Código más limpio y legible
# 3. Manejo implícito de excepciones
# 4. Aplicable a cualquier objeto con métodos __enter__ y __exit__

# Notas importantes:
# - El modo 'w' sobrescribe el archivo si ya existe
# - Para añadir contenido sin borrar lo existente, usar modo 'a' (append)
# - Siempre es preferible usar with sobre open/close manual