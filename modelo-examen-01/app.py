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
1. autos/financiar/{patente} (GET)
Recibe una patente por parámetro de ruta y un presupuesto por argumento para retornar un json
con los siguientes atributos:
patente: la patente del auto.
presupuesto: el presupuesto ingresado
aclanza: un boolean determinando si el importe ingresado alcanza para comprar el auto
precio: el precio del auto
precio_cuotas: el 150% del precio.
2. autos/editar/{id}
Recibe la id de un auto y un json con precio y velocidad. Una vez hecho esto, edita dichos datos
en el auto y retorna el objeto modificado ocultando su id.
Requisito: Usar Marshmallow
3. autos/totales
Retorna un json con los siguientes atributos:
promedio: promedio de precios
minimo: el precio más bajo de autos.
cantidad: la cantidad de autos registrados
NOTAS:
• Se asume que todas las búsquedas a la base siempre traen un resultado.
• No es necesario realizar validaciones.
• Las querys de SQLAlchemy solo se deben usar para traer listas de modelos, todo lo
demás debe ser realizado de forma programática.

'''

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
app.config["nombre"] = "Super app 123!"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datos.sql"
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
    class Meta:
        fields = ('patente', 'precio', 'velocidad')

# Endpoint 1: Financiamiento de auto por patente
@app.route('/autos/financiar/<patente>', methods=['GET'])
def financiar_auto(patente):
    # Obtener presupuesto de parámetros de consulta
    presupuesto = float(request.args.get('presupuesto'))
    
    # Buscar auto por patente (asumiendo que siempre existe)
    auto = Auto.query.filter_by(patente=patente).first()
    
    # Calcular valores requeridos
    alcanza = presupuesto >= float(auto.precio)
    precio_cuotas = float(auto.precio) * 1.5  # 150% del precio
    
    # Construir respuesta
    return jsonify({
        "patente": auto.patente,
        "presupuesto": presupuesto,
        "alcanza": alcanza,
        "precio": float(auto.precio),
        "precio_cuotas": precio_cuotas
    })

# Endpoint 2: Editar auto por ID
@app.route('/autos/editar/<int:id>', methods=['PUT'])
def editar_auto(id):
    # Obtener datos del JSON recibido
    datos = request.get_json()
    
    # Buscar auto por ID (asumiendo que siempre existe)
    auto = Auto.query.get(id)
    
    # Actualizar campos
    auto.precio = datos['precio']
    auto.velocidad = datos['velocidad']
    
    # Guardar cambios
    db.session.commit()
    
    # Crear schema sin incluir el ID
    schema = AutoSchema()
    
    # Retornar objeto modificado (sin ID)
    return schema.jsonify(auto)

# Endpoint 3: Estadísticas de autos
@app.route('/autos/totales', methods=['GET'])
def totales_autos():
    # Obtener todos los autos
    autos = Auto.query.all()
    
    # Calcular estadísticas
    precios = [float(auto.precio) for auto in autos]
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

if __name__ == '__main__':
    app.run(debug=True) 
