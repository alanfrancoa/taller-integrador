#importaciones
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, Boolean
from flask_marshmallow import Marshmallow
from marshmallow import fields
'''
Modelo de Examen de Programación en Python (Flask, SQLAlchemy, Marshmallow)

Aquí tienes un modelo de examen completo con 4 ejercicios basados en una entidad Usuario:
Modelo y Esquema
'''
#configuraciones
app = Flask(__name__)
app.config["nombre"] = "App users"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datos.sql"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db=SQLAlchemy(app)
ma=Marshmallow(app)

#Modelo
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    saldo = db.Column(db.Float, default=0.0)
    activo = db.Column(db.Boolean, default=True)

#esquema
class UsuarioSchema(ma.Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.String()
    edad = fields.Integer()
    saldo = fields.Float()
    activo = fields.Boolean()
'''
Endpoints a implementar
1. usuarios/verificar-saldo/{username} (GET)

    Recibe un username por parámetro de ruta

    Retorna un JSON con:

        username: el username del usuario

        saldo_actual: el saldo del usuario

        puede_comprar: boolean que indica si el saldo es suficiente para una compra de $1000

        saldo_requerido: 1000 - saldo_actual (si es negativo, mostrar 0)
'''
@app.route('/usuarios/verificar-saldo/<string:username>', methods=['GET'])
def verificar_saldo(username):
    usuario = Usuario.query.filter_by(username=username).first()
    
    dif = 1000 - usuario.saldo 

    if dif>=0:
        saldo_requerido = dif
    else:
        saldo_requerido = 0

    resultado = {
        "username": usuario.username,
        "saldo_actual": usuario.saldo,
        "puede_comprar": usuario.saldo >= 1000,
        "saldo_requerido": saldo_requerido
        }

    return jsonify(resultado)
    


'''
2. usuarios/actualizar-email/{id} (PUT)

    Recibe el ID de un usuario y un JSON con el nuevo email

    Actualiza el email del usuario

    Retorna el objeto modificado ocultando los campos "id" y "activo"

    Requisito: Usar Marshmallow para la deserialización
'''
@app.route('/usuarios/actualizar-email/<int:id>', methods=['PUT'])
def actualizar_email(id):
    
    usuarioActualizar = Usuario.query.get(id)
    
    if usuarioActualizar is None:
        return jsonify({"error": "No existen usuarios con ese ID"}),400
    
    data = request.get_json()
    result = UsuarioSchema(partial=True).load(data)
    
    if 'email' in result:
        usuarioActualizar.email = result['email']
        
    db.session.commit()    
    return UsuarioSchema(exclude=['id', 'activo']).dump(usuarioActualizar),200

'''
3. usuarios/estadisticas (GET)

    Retorna un JSON con:

        total_usuarios: cantidad total de usuarios

        promedio_edad: promedio de edad de los usuarios

        usuario_mayor: username del usuario con mayor edad

        usuarios_activos: cantidad de usuarios con activo=True
'''

'''
4. usuarios/desactivar-mayores/{edad_limite} (PUT)

    Recibe una edad límite por parámetro de ruta

    Desactiva (activo=False) a todos los usuarios con edad mayor a la límite

    Retorna un JSON con:

        mensaje: "Usuarios desactivados"

        total_desactivados: número de usuarios afectados

        edad_limite: la edad límite recibida
'''
@app.route('/usuarios/desactivar/mayores/<int:edad_limite>', methods=['GET'])
def desactivar_edad(edad):
    listado_edad=Usuario.query.filter_by(Usuario.edad >=edad).list()

    acum =0
    for usuario in listado_edad:
        if usuario.activo:
            usuario.activo = False
            acum+=1

    resultado =({
        "Mensaje":"Usuarios desactivados",
        "total_desactivados": acum,
        "edad_limite": edad
    })

    return jsonify(resultado), 200
'''
Notas del examen

    Se asume que todas las búsquedas a la base siempre traen un resultado

    No es necesario realizar validaciones de datos

    Las querys de SQLAlchemy solo se deben usar para traer listas de modelos

    Para cálculos estadísticos, usar programación Python pura
'''