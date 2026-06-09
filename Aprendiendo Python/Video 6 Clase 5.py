#Parametros argumentos.

def suma():

    num1 = 5
    num2 = 7
    print(num1 + num2)

suma() #Llamamos a la funcion suma para que se ejecute el bloque de codigo que contiene.

suma()

suma()

def sumaEX(num1, num2): #Definimos la funcion suma con dos parametros, num1 y num2.
    #Nota Dentro de los parentesis se pueden colocar los parametros, que son variables que se definen dentro de la funcion y que solo existen dentro de ella.
    #  Ejemplo: def suma(num1, num2): Esto sirve
    # para que la funcion reciba dos parametros, num1 y num2, que se pueden usar dentro de la funcion para realizar una tarea especifica.
    #Nota 2 si vamos a anadir mas parametros a la funcion, se deben separar por comas, ejemplo: def suma(num1, num2, num3): Esto sirve para que la funcion reciba tres parametros
    #  num1, num2 y num3.

    #Nota 3 Ya no seria necesario definir las variables num1 y num2 dentro de la funcion, ya que ahora son parametros que se reciben al llamar a la funcion, ejemplo: suma(5, 7)
    #  Esto sirve para llamar a la funcion suma y pasarle los valores 5 y 7 como argumentos para los parametros num1 y num2 respectivamente.

    print(num1 + num2)

sumaEX(10, 20) #Llamamos a la funcion suma y le pasamos los valores 10 y 20 como argumentos para los parametros num1 y num2 respectivamente. Esto hace que se ejecute
# el bloque de codigo
#que contiene la funcion suma, y se realice la suma de los valores 10 y 20, dando como resultado 30.
#Recordado que siempre deben estar separados por comas los argumentos que se pasan a la funcion, ejemplo: suma(5, 7) Esto es correcto, pero suma(5 7) 
# Esto es incorrecto, ya que no se estan separando los argumentos por comas.

sumaEX(0, 20) 

sumaEX(391, 2800)

# Funcion Return

# La funcion return se utiliza para devolver un valor desde una funcion, lo que permite que la funcion pueda ser utilizada en otras partes del codigo
#  y que el valor devuelto pueda ser almacenado en una variable o utilizado en una expresion.

def sumaReturn(num1, num2):
    return num1 + num2 #La palabra reservada return se utiliza para devolver el resultado de la suma de num1 y num2, lo que permite que este valor
    # pueda ser utilizado en otras partes del codigo.

# Otro ejemplo de Return seria:

def sumaReturn2(num1Return, num2Return):
    resultado = num1Return + num2Return
    return resultado #En este caso se almacena el resultado de la suma en una variable llamada resultado, y luego se devuelve esta variable con la palabra reservada return.

print(sumaReturn2(50,100)) #Llamamos a la funcion sumaReturn2 y le pasamos los valores 50 y 100 como argumentos
# para los parametros num1Return y num2Return respectivamente. Esto hace que se ejecute

print(sumaReturn2(1000, 2000))

print(sumaReturn2(0, 0))

# Para poder imprimir en pantalla el resultado con return hay que usar print() para imprimir el valor devuelto por la funcion
#  ejemplo: print(sumaReturn(10, 20)) Esto hace que se ejecute la funcion sumaReturn con los argumentos 10 y 20
#  y se imprima el resultado de la suma de estos dos numeros, que es 30.


# Return tambien se puede usar para almacenar el resultado de una funcion en una variable, lo que permite que este valor pueda ser utilizado en otras partes del codigo, ejemplo:

Almacena_resultado = sumaReturn(15, 25) #En este caso se almacena el resultado de la funcion sumaReturn en una variable llamada Almacena_resultado
#lo que permite que este valor pueda ser utilizado en otras partes del codigo.
print(Almacena_resultado) #Imprimimos el valor almacenado en la variable Almacena_resultado

