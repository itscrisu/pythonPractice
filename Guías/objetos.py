# Una clase es como un plano de una casa, esto significa que nos va a decir las dimensiones, el n° de hab
# darnos una idea de cómo van a ser las casas cuando las construyamos, las mismas casas construidas son
# las instancias de esta clase. 

# Plano de la casa = Clase
# Casa construida = Objetos

#class Usuario:
# Ahora declaramos las propiedades o métodos que puede tener esta clase:
#    nombre = "Cristian"
#    apellido = "Dominguez"
# Si queremos crear una instancia de este usuario, tenemos que crear una variable primero
# (Algo interesante de remarcar, es que las clases siempre se inician con la primer letra en Mayusculas)
#usuario = Usuario()
# Ahora usuario será la instancia de nuestra clase Usuario

# Si quisiera acceder a las propiedades del usuario (yo se que tiene una que se llama nombre y 
# otra apellido) así que para eso, tengo que realizarlo de esta forma:

#print(usuario.nombre, usuario.apellido)

# Ahora, qué pasa si yo no quiero que cada Usuario tenga el mismo nombre y apellido, sino que existan varios?
# Podemos declarar la clase de la siguiente forma:

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre 
        self.apellido = apellido

usuario = Usuario('Cristian', 'Dominguez')
usuario2 = Usuario('Frodo', 'Baggins')

print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

# La palabra reservada self hace referencia a una instancia, que nos permite modificar y agregar el valor
# que deseemos a las próximas que declaremos como lo estamos haciendo ahí, podemos cambiar el nombre y apellido
# No es necesario que lo pasemos como un parámetro cuando estemos instanciando

