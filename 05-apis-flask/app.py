from flask import Flask, request

# Creamos un objeto de tipo Flask y le pasamos la ubicación actual (__name__)
# __name__ es una variable que viene con FLASK, esta variable va a contener la ubicación del archivo donde estamos parado y se está ejecutando. 
app = Flask(__name__)

# Especificamos la ruta donde se va a ejecutar la lógica. Si usamos '/' esto quiere decir que es la ruta principal. 
@app.route('/')
def get_hola():
    return 'Buenas! Que tal? -> <button> Click aqui </button>'

#Ruta que devuelve un diccionario Python, flask lo convierte automaticamente a JSON.
@app.route('/dinosaurio')
def get_dinosaurio():
    dino = {"nombre": "T-Rex", "dieta": "Carnivoro"}
    return dino

# Otra forma de devolver JSON, esta vez escribiendo el string manualmente
@app.route('/dino2')
def get_dino2():
    return '{"nombre" : "T-Rex", "dieta": "Carnivoro"}'

#Ruta que devuelve un listado de numeros y un codigo de estado HTTP (402)
@app.route('/numeros')
def get_numeros():
    lista = []
    for i in range(20):
        lista.append(i)

    #Si quiero devolver una tupla, debo devolver el body y el status o header, al menos dos elementos.
    return(lista, 402)


#Ruta dinamica con parametro de tipo entero en la URL
#mediante el uso de <type: nombre_param>, podemos especificar el tipo de dato del parametro.
@app.route('/doble/<int:numero>')
def doble_numero(numero): #el parametro de la funcion se obtiene a traves del PARAM
    return{"Original": numero, "Doble": numero * 2}


#Ruta que usa parametros por query string. Ejemplo: /multiplicar/5?por=3
@app.route('/multiplicar/<int:numero>')
def multiplicar(numero):
    
    #Obtenemos todos los parametros enviados 
    parametrosQuery = request.args

    #convertimos el valor del parametro "por" a entero.
    multiplicar_por = int(parametrosQuery["por"])

    #devolvemos un json con el nro original y su resultado multiplicado.
    return {"Original": numero, "Multiplicado": numero * multiplicar_por}

# Como repetimos anteriormente, si estamos ejecutando el archivo main entonces corremos nuestro servidor. De paso le decimos que mientras corra nos debugge la ejecución. 
if __name__ == '__main__':
    app.run(debug=True)