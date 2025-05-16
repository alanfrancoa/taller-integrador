#clases

class Perro:
    def __init__(this, nombre, edad): #init, es un constructor, se escriben los atributos en el constructor. No requiere toda la estructura. This es el primer parametro (self) 

        this.nombre = nombre
        this.edad = edad

perrito = Perro("Chicho", 2) # funcion constructora

print(perrito.nombre)