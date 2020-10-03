def miFuncion():
    print('Mi primera función')

miFuncion()

# Dentro de la función, argumentoUno es un argumento:
# Una función puede estar definida con la cantidad de argumentos que queramos indicarle
# Obviamente mientras menos argumentos tenga, más fácil será de leer y entender qué hace.

def imprimeDato(argumentoUno):
    print('Mi argumento es', argumentoUno)

# Si nosotros le damos un valor dentro de esta función, se llama parámetro:

imprimeDato('parametro 1')

# Otro ejemplo:
def imprimeInfo(nombre, apellido):
    print('El nombre completo es', nombre, apellido)

imprimeInfo('Cristian', 'Dominguez')
imprimeInfo('Salame', 'Conqueso')
imprimeInfo('Manteca', 'Bronceada')
imprimeInfo('Tengo', 'Hambre')

# Podemos establecer el simbolo reservado * para que podamos ingresar la cantidad
# de argumentos que queramos (cabe destacar que será transformado en una tupla, es decir,
# será inmutable) Veamos:

def listaInfo(*dato):
    print('Los datos son:', dato)

listaInfo('Seguro', 'Fácil', 'Rápido', 'Efectivo')

# Si quisiera acceder al primer elemento de esta lista que se ha creado, puedo modificar en mi función
# lo siguiente:

# def listaInfo(*dato):
#     print('Los datos son:', dato[0])

# De esta forma, imprimiría el primer parámetro: Seguro
# Si quisiera acceder al parámetro Fácil, entonces sería 1, y así sucesivamente.

# Qué pasaría si no me acuerdo el orden de los argumentos como están definidos en mi función?
# Muy fácil, haríamos de esta forma:

def nombreGatitos(apellido, nombre):
    print('Mi gatito se llama:', nombre, apellido)

nombreGatitos(nombre='Frodo', apellido='Baggins')

# Nosotros podemos acceder a los argumentos que tiene una función utilizando otra sintaxis:
# kwargs: KEY WORD ARGUMENTS - entendido como ARGUMENTO POR LLAVE

def nombreGatitos2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

nombreGatitos2(nombre='Samwise', apellido='Gamgee')

# Qué pasa si no quiero estar todo el tiempo pasandole un argumento a mi función?

def miFuncion2(argumento = 'Pope'):
    print(argumento)

miFuncion2('Esto también se va a imprimir por encima de Pope')

# Si queremos que nuestra funcion admita parámetros como una lista, deberíamos definirla de la siguiente
# manera:

def miFuncionLista(lista):
    for el in lista:
        print(el)

miFuncionLista(['Samito', 'Frodito', 'Gatitos', 'Bonitos'])

# Tambien podemos hacer que las funciones retornen un valor para que podamos utilizarlo después, por ej:

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

# Utilizamos return i para que podamos volver a utilizarlo más adelante en caso de necesitarlo.
# Si dejaramos solamente el llamado a la función esto no imprimiría nada, ya que si los valores los estamos
# retornando, necesitamos si o si capturarlos en otra variable (o cajita) por eso, cuando llamemos a la función
# le indicaremos que se llama nombresGatitos:

nombresGatitos = concatenaNombres(['Samito', 'y', 'Frodito', 'son', 'gatitos', 'muy', 'bonitos'])
print(nombresGatitos)