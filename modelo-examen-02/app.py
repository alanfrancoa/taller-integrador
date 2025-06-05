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
@app.route('/libros/presupuesto/<string:titulo>', methods=['GET'])
def presupuesto(titulo):
    libro = Libro.query.filter_by(titulo=titulo).first()
    presupuesto = request.args.get('presupuesto', type=float)

    if not libro:
        jsonify({"error":"No hay libro con ese titulo"}), 404

    if not presupuesto:
        jsonify({"error":"Ingrese un presupuesto"}), 404

    resultado = {
        "titulo": libro.titulo,
        "presupuesto": presupuesto,
        "alcanza": presupuesto > libro.precio,
        "precio_actual": libro.precio,
        "precio_descuento": libro.precio * 0.8
    }
    
    return jsonify(resultado)


'''
2)libros/actualizar/{id} (PUT)
Recibe el ID de un libro y un JSON con titulo y páginas.
Actualiza estos datos en el libro correspondiente.
Retorna el objeto modificado ocultando el campo "publicado".
Requisito: Usar Marshmallow para la serialización.
'''
@app.route('/libros/actualizar/<int:id>', methods=['PUT'])
def editar(id):
    libro=Libro.query.filter_by(id=id).first()

    # Usar Marshmallow para cargar los datos de entrada
    schema = LibroSchema(partial=True)  # partial=True permite actualización parcial
    data = schema.load(request.get_json()) # Carga los datos del JSON, 

    if 'titulo' in data:
        libro.titulo = data['titulo']

    if 'paginas' in data:
        libro.paginas = int(data['paginas'])
    
    db.session.commit()
    return LibroSchema(exclude=["id","publicado"]).dump(libro), 200

'''
3)libros/estadisticas
Retorna un JSON con:
total_libros: cantidad total de libros registrados
promedio_paginas: promedio de páginas de todos los libros
libro_mas_caro: título del libro con mayor precio
libros_publicados: cantidad de libros con campo publicado=True
'''
@app.route('/libros/estadisticas', methods=['GET'])
def estadisticas():
    libros=Libro.query.all()

    cantidad_libros=len(libros)

    if cantidad_libros > 0:
        paginas_array=[libro.paginas for libro in libros]
        paginas_total=sum(paginas_array)
        promedio_paginas = paginas_total/cantidad_libros
    else:
        promedio_paginas=0

    libro_caro = None
    maximo=0

    for libro in libros:
        if libro.precio > maximo:
            libro_caro=libro
            maximo = libro_caro.precio

    contador_publicados=0
    for libro in libros:
        if libro.publicado:
            contador_publicados+=1


    resultado={
        "total_libros":cantidad_libros,
        "promedio_paginas": promedio_paginas,
        "libro_mas_caro": libro_caro.titulo,
        "libros_publicados": contador_publicados
    }
    return jsonify(resultado), 200

'''
NOTAS:
• Se asume que todas las búsquedas a la base siempre traen un resultado.
• No es necesario realizar validaciones.
• Las querys de SQLAlchemy solo se deben usar para traer listas de modelos, todo lo
demás debe ser realizado de forma programática.
'''
