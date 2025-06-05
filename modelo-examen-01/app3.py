'''
A partir del siguiente modelo y schema, asumiendo que la base de datos ya se encuentra
configurada, armar los endpoints solicitados:
class Auto(db.Model):
id = Column(int, primary_key=True)
patente = Column( String(length=10))
precio =Column(Float(asdecimal=True))
velocidad = Column(Float() )
class AutoSchema( ma.Schema ):
id = fields.Integer()
patente = fields.String()
precio = fields.Float()
velocidad = fields.Float()
'''
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
    id = Column(int, primary_key=True)
    patente = Column( String(length=10))
    precio =Column(Float(asdecimal=True))
    velocidad = Column(Float())

class AutoSchema( ma.Schema ):
    id = fields.Integer()
    patente = fields.String()
    precio = fields.Float()
    velocidad = fields.Float()

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

@app.route('/autos/financiar/<string: patente>', method=['GET'])
def financiar(patente):
    presupuesto = request.args.get("presupuesto", type=float)
    auto = Auto.query.filter_by(patente == patente).first()

    if not auto:
        return jsonify({"error":"Auto no encontrado"}), 404
    
    precio = auto.precio
    alcanza = precio <= presupuesto
    precio_cuotas = precio * 1.5

    return jsonify({
        "patente": patente,
        "presupuesto": presupuesto,
        "precio": precio,
        "precio_cuotas": precio_cuotas,
        "alcanza": alcanza
    })

'''
2. autos/editar/{id}
Recibe la id de un auto y un json con precio y velocidad. Una vez hecho esto, edita dichos datos
en el auto y retorna el objeto modificado ocultando su id.
Requisito: Usar Marshmallow
'''

@app.route('/autos/editar/<int: id>', method=['PUT'])
def editar(id):
    auto = Auto.query.filter_by(id == id).first()

    if not auto:
        return jsonify({"error":"Auto no encontrado"}), 404
    
    data = request.get_json()

    if 'precio' in data:
        auto.precio = data['precio']

    if 'velocidad' in data:
        auto.velocidad = data['velocidad']

    db.session.commit()

    schema = AutoSchema(exclude=['id'])

    return schema.jsonify(auto)

'''
3. autos/totales
Retorna un json con los siguientes atributos:
promedio: promedio de precios
minimo: el precio más bajo de autos.
cantidad: la cantidad de autos registrados
'''

@app.route('/autos/totales', method=['GET'])
def totales():
    autos = Auto.query.all()
    precios = [auto.precio for auto in autos]
    cantidad = len(precios)

    if cantidad > 0:
        promedio = sum(precios) / cantidad
        minimo = min(precios)
    else:
        promedio = minimo = 0

    return jsonify({
        "promedio": promedio,
        "minimo": minimo,
        "cantidad": cantidad
    })

'''
NOTAS:
• Se asume que todas las búsquedas a la base siempre traen un resultado.
• No es necesario realizar validaciones.
• Las querys de SQLAlchemy solo se deben usar para traer listas de modelos, todo lo
demás debe ser realizado de forma programática.

'''
# Crear las tablas antes de la primera solicitud
@app.before_first_request
def crear_tablas():
    db.create_all()

# Ejecutar la aplicación Flask
@app.route('/')
def index():
    return "Bienvenido al app de autos"

#endpoint alta de autos por json
@app.route('/autos/alta', method=['POST'])
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

# Endpoint para listar todos los autos
@app.route('/autos', method=['GET'])
def listar_autos():
    autos = Auto.query.all()
    schema = AutoSchema(many=True)
    return schema.jsonify(autos)

# Endpoint para obtener un auto por ID
@app.route('/autos/<int: id>', method=['GET'])
def get_auto_by_id(id):
    auto = Auto.query.filter_by(id == id).first()
    if not auto:
        return jsonify({"error": "No hay auto"}), 404
    schema = AutoSchema()
    return schema.jsonify(auto), 201

# Endpoint para eliminar un auto por ID
@app.route('/autos/<int: id>')
def eliminar_by_ID(id):
    auto = Auto.query.filter_by(id == id).first()
    
    if not auto:
        return jsonify({"error": "Auto no encontrado"}), 404

    db.session.delete(auto)
    db.session.commit()
    return jsonify({"message": "Auto eliminado exitosamente"}), 204

# Endpoint para actualizar un auto por ID
@app.route('/autos/<int: id>', method=['PUT'])
def editar_auto(id):
    auto = Auto.query.filter_by(id == id).first()

    if not auto:
        return jsonify({"error": "Auto no encontrado"})
    
    data = request.get_json()

    if 'patente' in data:
        auto.patente = data['patente']

    if 'velocidad' in data:
        auto.velocidad = float(data['velocidad'])
    
    if 'precio' in data:
        auto.precio = float(data['precio'])

    db.session.commit()
    schema = AutoSchema()
    return schema.jsonify(auto)

# Endpoint para buscar autos por patente
@app.route('/autos/buscar/<string: patente>')
def buscar_por_patente(patente):
    auto = Auto.query.filter_by(patente == patente).first()

    if not auto:
        return jsonify({"error": "no hay auto"}), 404
    
    schema = AutoSchema()
    return schema.jsonify(auto)
# Endpoint para buscar autos por velocidad
@app.route('/autos/buscar/velocidad', method=['GET'])
def buscar_por_velocidad():
    velocidad = request.args.get('velocidad', type=float)

    if velocidad is None:
        return jsonify({"error":"Se necesita definir velocidad"}), 400
    
    autos = Auto.query.filter(Auto.velocidad >= velocidad).all()

    if not autos:
        return jsonify({"message": "No hay autos que vayan tan rapido"}),404
    
    schema = AutoSchema(many=True)
    return schema.jsonify(autos)

# Endpoint para buscar autos por precio
@app.route('/autos/buscar/precio', methods=['GET'])
def buscar_por_precio():
    precio = request.args.get('precio', type=float)

    if precio is None:
        return jsonify({"error": "Ingrese un precio"}), 400
    
    autos = Auto.query.filter(Auto.precio <= precio).all()

    if not autos:
        return jsonify({"error":"No se encontraron autos por ese monto"}), 404
    
    schema = AutoSchema(many=True)
    return schema.dump(autos)

# Endpoint para buscar autos por patente y precio
@app.route('/autos/buscar/patent-precio', methods=['GET'])
def buscar_patente_precio():
    precio = request.args.get('precio', type=float)
    patente = request.args.get('patente')

    if not precio or not patente:
        return jsonify({"error":"Ingrese auto o patente"}), 404
    
    auto = Auto.query.filter_by(Auto.patente == patente, Auto.precio >= precio).first()

    if not auto:
        return jsonify({"error":"No hay auto"}), 404
    
    schema = AutoSchema()
    return schema.dump(auto)


# Endpoint para buscar autos por patente y velocidad3 
# @app.route('/autos/buscar/patente-velocidad', methods=['GET'])

# Endpoint para buscar autos por precio menor o igual y velocidad mayor o igual

