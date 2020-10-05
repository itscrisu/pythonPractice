# También podemos importar el modulo entero como hacemos acá:

import modulos

# O bien, importar solamente una variable o una función del módulo de esta forma:

# from modulos import saludo, mascotas

# Entonces luego no haría falta declarar "modulos.saludo" o "modulos.mascotas"
# Simplemente quedaría de esta forma nuestro código:

# print(mascotas)
# saludo('Cristian')


# Si quisiera renombrar a este modulo, es tan facil como declarar:
# import modulos as xs
# de esta forma, en vez de utilizar "modulos.saludo()" utilizaría "xs.saludo()"
print(modulos.mascotas)
modulos.saludo('Cristian')

