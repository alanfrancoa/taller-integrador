from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from marshmallow import Schema, fields

app = Flask(__name__)

app.config["nombre"] = "Super app 123!"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datos.sql" # Mi configuracion para SqlAlchemy utilizando sqlite
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Se añade para evitar warnings

db = SQLAlchemy(app)

# SQLALCHEMY
class Empleado(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column(String(length=20), nullable=False)
    sueldo = Column(Float(asdecimal=True))

# MARSHMALLOW
class EmpleadoSchema(Schema):
    nombre = fields.Str()
    sueldo = fields.Float()
    id = fields.Integer()

# Vamos a usar el objeto DB que creamos
@app.route('/iniciar')
def iniciar():
    db.drop_all() # Esto NUNCA se hace en producción
    db.create_all()
    return "La base de datos ha sido destruida y recreada con éxito"

@app.route('/')
def hello():
    nombreApp = app.config["nombre"]
    return "Bienvenidx a: " + nombreApp

@app.route('/alta')
def alta_empleado():
    nombre = request.args.get("nombre")

    # Creamos la nueva entidad que será el registro
    emple = Empleado()

    # Le asignamos los valores
    emple.nombre = nombre
    emple.sueldo = 100

    # Agregamos el nuevo empleado
    db.session.add(emple)

    # Guardamos los cambios realizados
    db.session.commit()
    
    return f"Empleado {nombre} añadido con éxito"  # Se añade retorno

@app.route('/mostrar')
def mostrar():
    emp = db.session.query(Empleado).all() #.first()

    # Usando Marshmallow
    # sch = EmpleadoSchema(only=["id"]) Mostrame solo el id
    sch = EmpleadoSchema(many=True) # Mostrame una lista de objetos

    # El objeto Empleado me lo convierte en un schema y Marshmallow puede convertirme el schema en un diccionario
    return sch.dump(emp)

if __name__ == '__main__':
    app.run(debug=True)