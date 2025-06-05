#importaciones
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, Boolean
from flask_marshmallow import Marshmallow
from marshmallow import fields

#configuraciones
app = Flask(__name__)
app.config["nombre"] = "App libros"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datos.sql"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

#modelo
class Libro(db.Model):
    id = Column(Integer, primary_key=True)
    titulo = Column(String(length=100))
    autor = Column(String(length=50))
    paginas = Column(Integer)
    precio = Column(Float(asdecimal=True))
    publicado = Column(Boolean)

#esquema
class LibroSchema(ma.Schema):
    id = fields.Integer()
    titulo = fields.String()
    autor = fields.String()
    paginas = fields.Integer()
    precio = fields.Float()
    publicado = fields.Boolean()

'''
1) libros/presupuesto/{titulo} (GET)
Recibe un título de libro por parámetro de ruta y un presupuesto máximo por argumento.
Retorna un JSON con:
titulo: el título del libro
presupuesto: el presupuesto ingresado
alcanza: boolean indicando si el presupuesto cubre el precio del libro
precio_actual: precio del libro
precio_descuento: 80% del precio (para compras al contado)
'''

'''
2)libros/actualizar/{id} (PUT)
Recibe el ID de un libro y un JSON con titulo y páginas.
Actualiza estos datos en el libro correspondiente.
Retorna el objeto modificado ocultando el campo "publicado".
Requisito: Usar Marshmallow para la serialización.
'''

'''
3)libros/estadisticas
Retorna un JSON con:
total_libros: cantidad total de libros registrados
promedio_paginas: promedio de páginas de todos los libros
libro_mas_caro: título del libro con mayor precio
libros_publicados: cantidad de libros con campo publicado=True
'''