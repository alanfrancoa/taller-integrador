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
app.config["nombre"] = "Super app 123!"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datos.sql"   # Asumiendo que la base de datos ya está configurada
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)   

# Modelo Auto (según especificación)
class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patente = db.Column(db.String(length=10))
    precio = db.Column(db.Float(asdecimal=True))
    velocidad = db.Column(db.Float())
    
# Schema para Auto usando Marshmallow
class AutoSchema(ma.Schema):
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

@app.route('/autos/financiar/<string:patente>', methods=['GET'])   
def financiar_auto(patente):
    presupuesto = request.args.get('presupuesto', type=float)
    auto = Auto.query.filter_by(patente=patente).first() # Asumiendo que la patente es única
    if not auto:
        return jsonify({"error": "Auto no encontrado"}), 404
    
    precio = auto.precio    
    precio_cuotas = precio * 1.5
    alcanza = presupuesto >= precio
    return jsonify({
        "patente": auto.patente,
        "presupuesto": presupuesto,
        "alcanza": alcanza,
        "precio": precio,
        "precio_cuotas": precio_cuotas
    })
'''
2. autos/editar/{id}
Recibe la id de un auto y un json con precio y velocidad. Una vez hecho esto, edita dichos datos
en el auto y retorna el objeto modificado ocultando su id.
Requisito: Usar Marshmallow
'''
@app.route('/autos/editar/<int:id>', methods=['PUT'])
def editar_auto(id):
    auto = Auto.query.get(id) # Buscar el auto por ID
    if not auto:
        return jsonify({"error": "Auto no encontrado"}), 404 # Obtener el auto por ID
    
    data = request.get_json() # Obtener los datos del JSON
    if 'precio' in data:
        auto.precio = data['precio']

    if 'velocidad' in data:
        auto.velocidad = data['velocidad']
    db.session.commit() # Guardar los cambios en la base de datos
    schema = AutoSchema(exclude=['id']) # Crear el schema sin incluir el ID
    return schema.jsonify(auto) # Retornar el objeto modificado sin ID


'''
3. autos/totales
Retorna un json con los siguientes atributos:
promedio: promedio de precios
minimo: el precio más bajo de autos.
cantidad: la cantidad de autos registrados

'''
@app.route('/autos/totales', methods=['GET'])
def autos_totales():
    autos = Auto.query.all() # Obtener todos los autos
    precios = [auto.precio for auto in autos] # Obtener los precios de los autos
    cantidad = len(precios) # Calcular la cantidad de autos
    if cantidad > 0: # Calcular promedio y mínimo si hay autos
        promedio = sum(precios) / cantidad
        minimo = min(precios)
    else: # Si no hay autos, establecer valores por defecto
        promedio = 0
        minimo = 0
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
'''
Apartado extra: 
Crear las tablas en la base de datos al iniciar la aplicación.
Esto se puede hacer utilizando el decorador `before_first_request` de Flask para asegurarse de que las tablas se creen antes de la primera solicitud.
# NOTA: Este apartado es opcional y se puede ejecutar una sola vez para crear las tablas.
# Si la base de datos ya existe, no es necesario volver a ejecutar este código.
'''
@app.before_first_request # Crear las tablas antes de la primera solicitud
def create_tables():
    db.create_all() 

# Ejecutar la aplicación Flask
@app.route('/')
def index():
    return "Bienvenido a la API de Autos"

#endpoint alta de autos
@app.route('/autos/alta', methods=['POST'])
def alta_auto():
    data = request.get_json()
    nuevo_auto = Auto(
        patente=data['patente'],
        precio=data['precio'],
        velocidad=data['velocidad']
    )
    db.session.add(nuevo_auto)
    db.session.commit()
    return AutoSchema().jsonify(nuevo_auto), 201

# Endpoint para listar todos los autos
@app.route('/autos', methods=['GET'])
def listar_autos():
    autos = Auto.query.all()
    schema = AutoSchema(many=True)
    return schema.jsonify(autos)

# Endpoint para obtener un auto por ID
@app.route('/autos/<int:id>', methods=['GET'])
def obtener_auto(id):
    auto = Auto.query.get(id)
    if not auto:
        return jsonify({"error": "Auto no encontrado"}), 404
    schema = AutoSchema()
    return schema.jsonify(auto)

# Endpoint para eliminar un auto por ID
@app.route('/autos/<int:id>', methods=['DELETE'])
def eliminar_auto(id):
    auto = Auto.query.get(id)
    if not auto:
        return jsonify({"error": "Auto no encontrado"}), 404
    db.session.delete(auto)
    db.session.commit()
    return jsonify({"message": "Auto eliminado exitosamente"}), 204

# Endpoint para actualizar un auto por ID
@app.route('/autos/<int:id>', methods=['PUT'])
def actualizar_auto(id):
    auto = Auto.query.get(id)
    if not auto:
        return jsonify({"error": "Auto no encontrado"}), 404
    data = request.get_json()
    if 'patente' in data:
        auto.patente = data['patente']
    if 'precio' in data:
        auto.precio = data['precio']
    if 'velocidad' in data:
        auto.velocidad = data['velocidad']
    db.session.commit()
    schema = AutoSchema()
    return schema.jsonify(auto)

# Endpoint para buscar autos por patente
@app.route('/autos/buscar/<string:patente>', methods=['GET'])
def buscar_auto_por_patente(patente):
    auto = Auto.query.filter_by(patente=patente).first() # Asumiendo que la patente es única
    if not auto: # Si no se encuentra el auto por patente
        return jsonify({"error": "Auto no encontrado"}), 404
    schema = AutoSchema() # Crear el schema para serializar el auto
    return schema.jsonify(auto) # Retornar el auto encontrado

# Endpoint para buscar autos por velocidad
@app.route('/autos/buscar/velocidad', methods=['GET'])
def buscar_auto_por_velocidad():
    velocidad = request.args.get('velocidad', type=float)
    if velocidad is None:
        return jsonify({"error": "Parámetro de velocidad es requerido"}), 400
    
    autos = Auto.query.filter(Auto.velocidad >= velocidad).all()  # Buscar autos con velocidad mayor o igual
    if not autos:
        return jsonify({"message": "No se encontraron autos con la velocidad especificada"}), 404
    schema = AutoSchema(many=True) # Crear el schema para serializar múltiples autos
    return schema.jsonify(autos)

# Endpoint para buscar autos por precio
@app.route('/autos/buscar/precio', methods=['GET'])
def buscar_auto_por_precio():
    precio = request.args.get('precio', type=float)
    if precio is None:
        return jsonify({"error": "Parámetro de precio es requerido"}), 400
    
    autos = Auto.query.filter(Auto.precio <= precio).all()
    if not autos:
        return jsonify({"message": "No se encontraron autos con el precio especificado"}), 404
    schema = AutoSchema(many=True)
    
    return schema.jsonify(autos)  # Retornar los autos encontrados con el precio especificado

# Endpoint para buscar autos por patente y precio
@app.route('/autos/buscar/patente_precio', methods=['GET'])
def buscar_auto_por_patente_y_precio():
    patente = request.args.get('patente')
    precio = request.args.get('precio', type=float)
    
    if not patente or precio is None:
        return jsonify({"error": "Parámetros de patente y precio son requeridos"}), 400
    
    auto = Auto.query.filter_by(patente=patente, precio=precio).first()
    
    if not auto:
        return jsonify({"message": "No se encontró un auto con la patente y precio especificados"}), 404
    
    schema = AutoSchema() # Crear el schema para serializar el auto
    return schema.jsonify(auto)# Retornar el auto encontrado con la patente y precio especificados

# Endpoint para buscar autos por patente y velocidad
@app.route('/autos/buscar/patente_velocidad', methods=['GET'])
def buscar_auto_por_patente_y_velocidad():
    patente = request.args.get('patente')
    velocidad = request.args.get('velocidad', type=float)
    
    if not patente or velocidad is None:
        return jsonify({"error": "Parámetros de patente y velocidad son requeridos"}), 400
    
    auto = Auto.query.filter_by(patente=patente, velocidad=velocidad).first()
    
    if not auto:
        return jsonify({"message": "No se encontró un auto con la patente y velocidad especificados"}), 404
    
    schema = AutoSchema() # Crear el schema para serializar el auto
    return schema.jsonify(auto)

# Endpoint para buscar autos por precio menor o igual y velocidad mayor o igual
@app.route('/autos/buscar/precio_velocidad', methods=['GET'])
def buscar_auto_por_precio_y_velocidad():
    precio = request.args.get('precio', type=float)
    velocidad = request.args.get('velocidad', type=float)
    
    if precio is None or velocidad is None:
        return jsonify({"error": "Parámetros de precio y velocidad son requeridos"}), 400
    
    autos = Auto.query.filter(Auto.precio <= precio, Auto.velocidad >= velocidad).all() # Buscar autos con precio menor o igual y velocidad mayor o igual
    
    if not autos:
        return jsonify({"message": "No se encontraron autos con el precio y velocidad especificados"}), 404
    
    schema = AutoSchema(many=True) # Crear el schema para serializar múltiples autos
    return schema.jsonify(autos) 


if __name__ == '__main__':
    db.create_all()  # Crear las tablas en la base de datos
    app.run(debug=True)  # Ejecutar la aplicación Flask 

