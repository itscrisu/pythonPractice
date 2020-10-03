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

if primero == "chanchito feliz" or segundo == "chanchito feliz":
    print('Ingresaste mal un dato, intenta de nuevo sólo con numeros')
else: 
    print(primero + segundo)