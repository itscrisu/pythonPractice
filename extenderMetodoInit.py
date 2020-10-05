class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'me llamo', self.nombre, ' y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = "gato"
# Una forma de extender el método:
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola, soy un gato extendido :P')


class Perro(Animal):
    tipo = "perro"
# Otra forma de extender el método de __init__
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('Hola, soy un perro extendido :P')
    
gato = Gato('Frodo', 'maullido')
gato.saludo()

perro = Perro('Pupi', 'ladrido')
perro.saludo()


# De esta forma podemos extender el comportamiento que tiene el método __init__ de la clase padre
# que en este caso es Animal