usuarios = ['Frodo', 'Sami', 'Quesito', 'Milanga']

for usuario in usuarios:
    print(usuario)

# Si quiero tambien puedo iterar sobre un string, de esta forma:

persona = 'Pupito'

for c in persona:
    print(c)

# También puedo utilizar break en estos casos:

personas = ['Pedro', 'Juan', 'Guillermo', 'Ariel', 'Soraka']

for macho in personas:
    if macho == 'Ariel':
        break
    print(macho)

# Podemos utilizar la palabra reservada de continue también,
# en estos casos es más fácil porque si fuese Ariel por ejemplo,
# no imprimiría Ariel, pero si Soraka y los demás, porque Ariel
# es macho.

# Utilizamos range:

for x in range(6):
    print(x)

# Podemos determinar distintas operaciones que queremos que pasen
# en range, por ejemplo, que empiece por el n° 3:

for x in range(3, 6):
    print(x)

# Y también si queremos que vaya de 2 en 2:

for x in range(3, 20, 2):
    print(x)

# En los for loops, el else se va a ejecutar cuando terminemos la 
# iteración que le hayamos indicado en el primer paso:

for x in range(3, 20, 2):
    print(x)
else:
    print('Terminamos!')

