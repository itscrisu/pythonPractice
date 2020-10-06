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

# Escribir una función que indique si el usuario es mayor de edad

# Escribir una función que indique si el número ingresado es par o impar 
