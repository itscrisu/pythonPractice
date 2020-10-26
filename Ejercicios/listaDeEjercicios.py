# Multiplicar dos números sin usar el símbolo de multiplicación

a = 2
b = 8

resultado = 0

for x in range(a):
    resultado += b

print(resultado)

# Ingresar un nombre y apellido e imprimelo al revés

nombre = 'Cristian'
apellido = 'Dominguez'

ambos = nombre + ' ' + apellido

print(ambos[::-1])

# Intercambiando valores:

nombre = 'Crisu'
apellido = 'Damins'

nombre, apellido = apellido, nombre

print(nombre)
print(apellido)

# Escribir una función que encuentre el elemento menor de una lista

lista = [1, 4, 7, 13, 44, 24, -30]

menor = 'inicial'

for x in lista:
    if menor == 'inicial':
        menor = x
    else:
        menor = x if x < menor else menor

print('El número menor es', menor) 

# Escribir una función que devuelva el volumen de una esfera por su radio 
# 4/3 * pi * r ** 3

def calculaVolumen(r):
    return 4/3 * 3.14 * r ** 3

resultado = calculaVolumen(6)
print(resultado)

# Escribir una función que indique si el usuario es mayor de edad

def esMayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(21)
usuario3 = Usuario(17)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)
resultado3 = esMayor(usuario3)

print(resultado1, resultado2, resultado3)

# Escribir una función que indique si el número ingresado es par o impar 

def esPar(n):
    return n % 2 == 0

resultado = esPar(10)
resultado2 = esPar(3)
resultado3 = esPar(11)
resultado4 = esPar(14)

print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)

# Escribir una funcion que indique cuantas vocales tiene una palabra:

palabra = 'Cristian'
vocales = 0

for x in palabra:
    y = x.lower()
    vocales += 1 if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else 0

print(vocales)

# escribir una app que reciba una cantidad infinita de n° hasta decir basta, luego que
# devuelva la suma de los n° ingresados

lista = []

print('Ingrese numeros y para salir escriba "basta"')

while True:
    valor = input('Ingrese un valor: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('Dato no válido')
            exit()

resultado = 0

for x in lista:
    resultado += x

print(resultado)

# escriba una funcion que reciba un nombre y un apellido y los vaya agregando a un archivo

def nameToFile(nombre, apellido):
    c = open('nombreCompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

nameToFile('Cristian', 'Dominguez')

