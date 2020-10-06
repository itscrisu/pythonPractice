class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre 
        self.apellido = apellido

#Vamos a definir un método 
    def saludo(self):
        print('Hola! Mi nombre es', self.nombre, self.apellido)

# Vamos a aplicar el concepto de Herencia:

class Admin(Usuario): 
    def  superSaludo(self):
        print('Hola! Me llamo', self.nombre, ' y soy Administrador!')

usuario = Usuario('Cristian', 'Dominguez')
usuario2 = Usuario('Frodo', 'Baggins')

usuario.saludo()
usuario2.saludo()

# Ahora lo estamos utilizando como un saludo, pero eventualmente nos sirve para iniciar sesión, cambiar de contraseña
# para guardar datos en una BDD, tiene múltiples aplicaciones los métodos.

# Si bien no es necesario utilizar la palabra reservada self, se utiliza como convención ya que si otro
# programador ve tu código y en vez de self ve no sé, "chorizo" no va a entender nada cuando lea
# chorizo.nombre y se va a hacer muy dificil entenderlo. 

admin = Admin('Samwise', 'Gamgee')
admin.saludo()
admin.superSaludo()