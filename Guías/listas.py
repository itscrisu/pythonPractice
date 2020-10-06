# Esto es una lista
lista = ['Elemento0', 'Elemento1', 'Elemento2', 'Elemento3']

# Podemos hacer una copia de la lista anterior de esta forma:
lista2 = lista.copy()

# Este comando ordena la lista de manera ascendente automaticamente:
lista.sort()

# Aunque tambien podemos declararlo de la siguiente forma para que lo haga de manera descendente:
lista.sort(reverse=True)

# Le podemos agregar a la lista original un último elemento. 
# Cabe destacar que al agregarlo luego de hacer la copia, la copia no va a tener este elemento claramente!

lista.append('Elemento4')

# Esto es una tupla:
tupla = ('Elemento0', 'Elemento1', 'Elemento2', 'Elemento3')

# Y podemos transformarla en una lista si queremos de esta forma:
listaDeTupla = list(tupla)

# Este comando nos va a servir para utilizar luego en las iteraciones:
rango = range(4)
# Si le damos al comando print(rango) nos va a indicar que estará en un range(0, 4)




