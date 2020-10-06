class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'me llamo', self.nombre, ' y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = "gato"


class Perro(Animal):
    tipo = "perro"
    
gato = Gato('Frodo', 'maullido')
gato.saludo()

perro = Perro('Pupi', 'ladrido')
perro.saludo()
