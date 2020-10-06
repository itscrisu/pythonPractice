primero = input("Ingrese el primer número: ")


#primerNumero = int(primero)
#segundoNumero = int(segundo)

#print(primerNumero + segundoNumero)

# Otra forma de realizar la misma operación pero utilizando try y except de esta forma:

try: 
    primero = int(primero)
except:
    primero = "chanchito feliz"

segundo = input("Ingrese el segundo número: ")

try: 
    segundo = int(segundo)
except:
    segundo = "chanchito feliz"

if segundo == "chanchito feliz":
    print('El dato ingresado no es un entero')
    exit()

simbolo = input("Ingrese operación: ")

if simbolo == '+':
    print('Suma:', primero + segundo)
elif simbolo == '-':
    print('Resta:', primero - segundo)
elif simbolo == '*':
    print('Multiplicación:', primero * segundo)
elif simbolo == '/':
    print('División:', primero / segundo)
else:
    print('El simbolo ingresado no es válido')