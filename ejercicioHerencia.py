class Gato:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy un gato, me llamo', self.nombre, ' y mi sonido es el', self.onomatopeya)

class Perro:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    
    def saludo(self):
        print('Hola! Soy un perro, me llamo', self.nombre, ' y mi sonido es el', self.onomatopeya)
    
gato = Gato('Frodo', 'maullido')
gato.saludo()

perro = Perro('Pupi', 'ladrido')
perro.saludo()
