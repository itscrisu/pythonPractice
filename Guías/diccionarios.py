# Voy a hacer un diccionario con los datos de mi gato
# Siempre recordar que se definen cada elemento entre doble comillas - dos puntos - coma 
# Ademas siempre va entre llaves definido el diccionario.

diccionario = {
    "nombre": "Frodo",
    "raza": "Tuxedo",
    "edad": 3
}

# Si queremos acceder solamente a uno de los valores del diccionario, basta con declarar de esta forma:
print(diccionario['nombre'])
# Si quiero acceder a la raza sería de esta forma:
print(diccionario['raza'])
# No siempre es necesario utilizar los corchetes, también podemos llamar al mismo valor anterior de esta forma:
print(diccionario.get('raza'))

# Otro dato interesante, si utilizamos el comando len en diccionario veremos los elementos del mismo
# En este caso claramente, tenemos 3, por lo tanto ese será el resultado de esta declaración:
print(len(diccionario))

# Si queremos agregar un elemento y su valor a un diccionario, podemos hacerlo de esta forma:
diccionario['ronronea'] = 'Si, muy bajito'
print(diccionario)

# Si queremos eliminar un valor del diccionario, utilizamos esta forma:
diccionario.pop('ronronea')
print(diccionario)

# Otra forma de eliminar más rápido el último valor que se agrego a nuestro diccionario, es utilizando
# la siguiente forma:
# diccionario.popitem()

# Otra forma de eliminar un elemento de la lista, es utilizando el lenguaje reservado del:
# del diccionario['ronronea']
# Podemos eliminar ronronea como cualquier otra propiedad obviamente

# Si queremos hacer una copia de este diccionario, utilizamos el comando .copy de esta forma:
copiaDiccionario = diccionario.copy()





