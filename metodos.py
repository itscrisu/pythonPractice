class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre 
        self.apellido = apellido

#Vamos a definir un método 
    def saludo(self):
        print('Hola! Mi nombre es', self.nombre, self.apellido)

usuario = Usuario('Cristian', 'Dominguez')
usuario2 = Usuario('Frodo', 'Baggins')

usuario.saludo()
usuario2.saludo()

# Ahora lo estamos utilizando como un saludo, pero eventualmente nos sirve para iniciar sesión, cambiar de contraseña
# para guardar datos en una BDD, tiene múltiples aplicaciones los métodos.