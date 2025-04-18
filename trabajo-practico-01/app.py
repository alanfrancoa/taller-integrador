#Practica Inicial API REST
'''
Crear una api con Flask, creando las rutas correspondientes en base
a lo documentación brindada a continuación.
'''
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def get_bienvenida():
    return 'Bienvenido!'

'''
Ruta: /suma
Detalle:
Recibe dos números (a y b) y retorna un JSON con el resultado de la
suma.
Query Params:
• a: El primer número
• b: El segundo número
Retorno:
• primero: el primer número (a)
• segundo: el segundo número (b)
• suma: el resultado de la suma de a y b
Ej:
Endpoint: /suma?a=2&b=3
Resultado: {"primero": 2, "segundo": 3, "suma": 5}s
'''

@app.route('/suma')
def suma():

    #creamos los query params
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    #creamos la estructura de la respuesta
    resultado = {
        "Primero": a,
        "Segundo": b,
        "Suma": a + b
    }

    #devolvemos la suma
    return resultado

'''
Ruta: /informacion/<int:numero>
Detalle:
Recibe un número por parámetro de ruta y retorna un JSON con
información sobre el número.
Parámetro de ruta:
• numero: El número a analizar
Retorno:
• numero: el número ingresado
• doble: el doble del número
• positivo: true si es positivo, false si es negativo o cero
• par: true si es par, false si es impar
• cuadrado: el número elevado al cuadrado
Ej:
Endpoint: /informacion/4
Resultado: {"numero": 4, "doble": 8, "positivo": true, "par": true,
"cuadrado": 16}
'''

@app.route('/informacion/<int:numero>')
def informacion(numero):
    #parseamos el numero del parametro a int
    #esto se hace asi, ya que flask no acepta valores negativos enteros por URL
    numero_int = int(numero)

    #validaciones
    es_positivo = False
    es_par = numero_int % 2 == 0

    if numero_int > 0:
        es_positivo = True
    elif numero_int == 0:
        es_positivo = 0

    resultado = {
        "Numero": numero_int,
        "Doble": numero_int * 2,
        "Positivo": es_positivo,
        "Par": es_par,
        "Cuadrado": numero_int ** 2
    }
    return resultado

'''
Ruta: /rectangulo
Detalle:
Recibe la base y la altura de un rectángulo por query params y
retorna un JSON con sus propiedades.
Query Params:
• base: Base del rectángulo
• altura: Altura del rectángulo
Retorno:
• base: la base ingresada
• altura: la altura ingresada
• area: base por altura
• perimetro: suma de todos los lados
• cuadrado: true si la base y altura son iguales
• alto: true si la altura es mayor que la base
Ej:
Endpoint: /rectangulo?base=4&altura=6
Resultado: {"base": 4, "altura": 6, "area": 24, "perimetro": 20,
"cuadrado": false, "alto": true}
'''

@app.route('/rectangulo')
def rectangulo():

    #creamos los query params
    base = request.args.get('base', type=int)
    altura = request.args.get('altura', type=int)

    es_cuadrado = False
    alto_mas_base = False

    if base == altura:
        es_cuadrado = True

    if altura > base:
        alto_mas_base = True
    
    #creamos respuesta
    respuesta = {
        "Base": base,
        "Altura": altura,
        "Area": base * altura,
        "Perimetro": (base*2)+(altura*2),
        "Cuadrado": es_cuadrado,
        "Altura Mas Base": alto_mas_base
    }

    return respuesta

'''
Ruta: /palabra/<palabra>
Detalle:
Recibe una palabra por parámetro de ruta y retorna un JSON con
información sobre esa palabra.
Parámetro de ruta:
• palabra: La palabra a analizar
Retorno:
• palabra: la palabra ingresada
• largo: cantidad de caracteres
• empieza_con_vocal: true si empieza con vocal
• mayuscula: true si está toda en mayúsculas
• invertida: la palabra al revés
Ej:
Endpoint: /palabra/Hola
Resultado: {"palabra": "Hola", "largo": 4, "empieza_con_vocal":
false, "mayuscula": false, "invertida": "aloH"}
'''

@app.route('/palabra/<palabra>')
def info_palabras(palabra):
    empieza_vocal = False

    if palabra[0].lower() in "aeiou":
        empieza_vocal = True

    resultado = {
        "Palabra": palabra,
        "Largo": len(palabra),
        "Vocal": empieza_vocal,
        "Mayuscula": palabra.isupper(),
        "Invertida": palabra[::-1]
    }

    return resultado


'''
Ruta: /repetir/<palabra>
Detalle:
Recibe una palabra por parámetro de ruta y un número por query param
(veces). Retorna un JSON con la palabra repetida la cantidad de
veces indicada.
Parámetro de ruta:
• palabra: La palabra a repetir
Query Params:
• veces: Número de repeticiones
Retorno:
• palabra: la palabra ingresada
• veces: cantidad de repeticiones
• resultado: string con la palabra repetida
Ej:
Endpoint: /repetir/hola?veces=3
Resultado: {"palabra": "hola", "veces": 3, "resultado":
"holaholahola"}
'''

@app.route('/repetir/<palabra>')
def repetir_palabra(palabra):

    #Creo el query param
    veces = request.args.get('veces', type=int)

    #Creamos la respuesta
    resultado = {
        "Palabra": palabra,
        "Veces": veces,
        "Repetir": palabra * veces
    }

    return resultado

'''
Ruta: /potencias/<int:numero>
Detalle:
Recibe un número por parámetro de ruta y un valor veces por query
param. Retorna un JSON con la lista de potencias del número, desde
el exponente cero hasta el exponente indicado. Para calcular
potencias en Python pueden usar el operador **.
Parámetro de ruta:
• numero: El número base que se va a elevar
Query Params:
• veces: Número máximo de veces que se va a elevar (incluye el
cero)
Retorno:
• elementos: lista de resultados que incluye el número base
elevado a la 0, a la 1, a la 2, y así sucesivamente hasta el
número ingresado en veces
• cantidad: cantidad de elementos generados en la lista
Ejemplo:
Endpoint: /potencias/2?veces=4
Resultado: {"elementos": [1, 2, 4, 8, 16], "cantidad": 5}
'''

@app.route('/potencias/<int:numero>')
def potencia(numero):

    #creo el query params
    veces = request.args.get('veces', type=int)

    potencias = []

    for i in range(0,veces + 1):
        potencias.append(numero ** i)

    resultado = {
        "elementos": potencias,
        "cantidad": len(potencias)
    }

    return resultado