def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)

# Si la llamamos con el valor de 6, va a preguntar si 6 es menor a 1 (no) ok, saltamos a la siguiente linea:
# va a imprimir 6, y luego se va a llamar a sí misma nuevamente, pero ahora tendrá el valor de 5 ya que 
# i = 6 - 1 -> 5
# De esta forma continuará hasta que el valor de i sea igual a 1 y ahí se detendrá y nos dará el valor de 1

# La idea de este ejercicio es entender de manera fácil como funciona la recursividad:
# Cuando nosotros estamos utilizando recursividad, tenemos que escribir la lógica que queremos ejecutar
# y también tenemos que indicar una condición de salida, si se cumple, tenemos que detener la ejecución
# de esta función por ende, no volver a llamarla

# Pero para cuándo sirve la recursividad?
# Para cuando queremos por ejemplo trabajar sobre una colección de datos, o cuando queremos hacer reintentos
# para llamar a un servidor o una base de datos en caso de que esta falle.

# Mini ejemplo:
# Si nosotros nos conectamos con una API la primera vez nos brinda un error, podemos escribir una pequeña
# función recursiva que lo que haga es intentar una máxima de, por ejemplo, 3 o 5 veces de conectarse. 
# Si se vuelve a llamar una 5ta vez y nos brinda otro error, en ese caso ahi lanzamos un error en la App.
# Si intenta 3 veces, pero a la 4ta ya puede ingresar, prevenimos enviarle un mensaje de error al usuario

# Otro mini ejemplo:
# Si queremos procesar una lista con 50 elementos y luego pasamos y procesamos los siguientes de otra lista
# y así sucesivamente.

 