from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
app.config["nombre"] = "App autos"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datos.sql"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Auto(db.Model):
    id = Column(Integer, primary_key=True)
    patente = Column( String(length=10))
    precio =Column(Float(asdecimal=True))
    velocidad = Column(Float())

class AutoSchema( ma.Schema ):
    id = fields.Integer()
    patente = fields.String()
    precio = fields.Float()
    velocidad = fields.Float()

# Crear las tablas antes de la primera solicitud
@app.route('/iniciar')
def crear_tablas():
    db.create_all()

    return "DB iniciada"

# Ejecutar la aplicación Flask
@app.route('/')
def index():
    return "Bienvenido al app de autos"

#endpoint alta de autos por json
@app.route('/autos/alta', methods=['POST'])
def alta():
    data = request.get_json()

    nuevo_auto = Auto(
        patente = data['patente'],
        velocidad = data['velocidad'],
        precio = data['precio']
    )
    db.session.add(nuevo_auto)
    db.session.commit()
    return AutoSchema().jsonify(nuevo_auto), 201
    #return AutoSchema().dump(nuevo_auto) //serializacion

# Endpoint para listar todos los autos
@app.route('/autos', methods=['GET'])
def listar_autos():
    autos = Auto.query.all()
    return AutoSchema(many=True).jsonify(autos)

# Endpoint para obtener un auto por ID
@app.route('/autos/<int:id>', methods=['GET'])
def obtener_auto(id):
    auto = Auto.query.get(id)
    if auto is None:
        return jsonify({"error": "No se encontro auto"})
    
    return AutoSchema().jsonify(auto), 200

# Endpoint para eliminar un auto por ID
@app.route('/autos/eliminar/<int:id>', methods=['DELETE'])
def eliminar(id):
    auto = Auto.query.get(id)

    if not auto:
        return jsonify({"error":"No hay auto"})
    
    db.session.delete(auto)
    db.session.commit()
    return jsonify({"Message": "Exito, auto borrado correctamente"}), 200

# Endpoint para actualizar un auto por ID
@app.route('/autos/editar/<int:id>', methods=['PUT'])
def editar(id):

    auto = Auto.query.get(id)
    data = request.get_json()

    if not auto:
        return jsonify({"error":"No hay auto"})
    
    if not data:
        return jsonify({"error":"No hay data"})

    if 'patente' in data:
        auto.patente = data['patente']

    if 'precio' in data:
        auto.precio = float(data['precio'])    

    if 'velocidad' in data:
        auto.velocidad = float(data['velocidad'])   

    db.session.commit()

    return AutoSchema(exclude=id).jsonify(auto)


# Endpoint para buscar autos por patente
@app.route('/autos/buscar/patente/<string:patente>', methods=['GET'])
def buscar_patente(patente):

    auto = Auto.query.filter_by(patente=patente).first()

    if auto is None:
        return jsonify({"error": "No hay auto con esa patente"}), 404
    
    return AutoSchema().jsonify(auto), 200
    

# Endpoint para buscar autos por velocidad
@app.route('/autos/buscar/velocidad', methods=['GET'])
def obtener_velocidad():
    velocidad = request.args.get('velocidad', type=float)
    autos = Auto.query.filter(Auto.velocidad >= velocidad).all()

    if not autos:
        return jsonify({"error": "No hay autos tan rapidos"}), 404
    
    return AutoSchema(many=True).jsonify(autos), 200

# Endpoint para buscar autos por precio
@app.route('/autos/buscar/precio', methods=['GET'])
def obtener_precio():
    precio = request.args.get('precio', type=float)

    autos = Auto.query.filter(Auto.precio <= precio).all()

    if not autos:
        return jsonify({"error":"No hay autos por ese precio"})
    
    return AutoSchema(many=True).jsonify(autos), 200
# Endpoint para buscar autos por patente y precio
@app.route('/autos/buscar/patente-precio', methods=['GET'])
def obtener_patente_precio():
    patente = request.args.get('patente')
    precio = request.args.get('precio', type=float)

    if not patente or not precio:
        return jsonify({"error": "Ingrese precio y patente son necesarios"}), 404
    
    auto = Auto.query.filter(Auto.patente == patente, Auto.precio <= precio).first()

    if not auto:
        return jsonify({"error": "No hay auto con ese precio y o patente"}), 404
    
    return AutoSchema().jsonify(auto)
    

# Endpoint para buscar autos por patente y velocidad
# Endpoint para buscar autos por precio menor o igual y velocidad mayor o igual
'''
1. autos/financiar/{patente} (GET)
Recibe una patente por parámetro de ruta y un presupuesto por argumento para retornar un json
con los siguientes atributos:
patente: la patente del auto.
presupuesto: el presupuesto ingresado
aclanza: un boolean determinando si el importe ingresado alcanza para comprar el auto
precio: el precio del auto
precio_cuotas: el 150% del precio.
'''
@app.route('autos/financiar/<string:patente>', methods=['GET'])
def financiar(patente):
    presupuesto = request.args.get('presupuesto', type=float)

    auto=Auto.query.filter(Auto.patente == patente).first()

    if not auto:
        return jsonify({"error":"No hay coincidencias en la busqueda"}), 400

    resultado = {
        "patente":auto.patente,
        "presupuesto": presupuesto,
        "alcanza": presupuesto >= auto.precio,
        "precio": auto.precio,
        "precio_cuotas": auto.precio * 1.5 #150% DEL PRECIO DEL AUTO
    }

    return jsonify(resultado), 200

'''
2. autos/editar/{id}
Recibe la id de un auto y un json con precio y velocidad. Una vez hecho esto, edita dichos datos
en el auto y retorna el objeto modificado ocultando su id.
Requisito: Usar Marshmallow
'''

@app.route('/autos/editar/<int:id>', methods=['PUT'])
def editar_auto_id(id):

    auto = Auto.query.get(id)

    if not auto:
        return jsonify({"error":"no existe auto"})
    
    data=request.get_json()

    if not data:
        return jsonify({"error":"No hay datos"})
    
    if 'precio' in data:
        auto.precio=data['precio']

    if 'velocidad' in data:
        auto.velocidad=data['velocidad']

    db.session.commit()
    return AutoSchema(exclude=['id']).dump(auto), 200 #marshmallow
'''
3. autos/totales
Retorna un json con los siguientes atributos:
promedio: promedio de precios
minimo: el precio más bajo de autos.
cantidad: la cantidad de autos registrados
'''
@app.route('/autos/totales', methods=['GET'])
def autos_totales():
    autos=Auto.query.all()
    
    precios=[]
    for auto in autos:
        precios.append(auto.precio)

    acumulador = 0

    for precio in precios:
        acumulador += precio
    
    cantidad = len(precios)
    
    if cantidad > 0:
        promedio = acumulador/cantidad
        minimo = min(precios)
    else:
        promedio = minimo = 0

    resultado={
        "promedio":promedio,
        "minimo": minimo,
        "cantidad": cantidad
    }

    return jsonify(resultado)

#alans version


if __name__ == '__main__':
    app.run(debug=True)