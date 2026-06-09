#Clase de hoy sintaxis de python.

#Zona de parametros, aqui se pueden declarar variables, funciones, clases, etc. ejemplo:

def  mi_funcion(): #() es el simbolo de los parametros, en este caso no tiene parametros, pero se pueden agregar dentro de los parentesis.
    print("Hola mundo") #print() es una funcion que imprime en pantalla lo que se le indique entre los parentesis.

    #Nota def es la palabra reservada para definir una funcion, seguida del nombre de la funcion y los parentesis.

#Para llamar a la funcion se escribe el nombre de la funcion seguido de parentesis.
mi_funcion()

#Una funcion es un bloque de codigo que se ejecuta cuando se le llama, y puede recibir parametros para realizar una tarea especifica.
#Tambien una funcion duevuelve un valor, para eso se usa la palabra reservada return.




def mensaje():

    print("estamos aprendiendo python")
    print("Estamos aprendiendo instrucciones basicas de python")
    print("Poco a poco iremos avanzando en el aprendizaje de python")

mensaje() #Llamamos a la funcion mensaje para que se ejecute el bloque de codigo que contiene.

#Las funciones se utilizan para organizar el codigo, evitar la repeticion de codigo y facilitar la lectura del codigo.
# Tambien para llamarlas desde otras partes del codigo, lo que permite reutilizar el codigo y hacer el programa mas modular.
# Sin necesidad de escribir el mismo codigo varias veces, lo que hace que el programa sea mas eficiente y facil de mantener.
# Ejemplo:

mensaje() #Llamamos a la funcion mensaje para que se ejecute el bloque de codigo que contiene.
mensaje() #Llamamos a la funcion mensaje para que se ejecute el bloque de codigo que contiene.
mensaje() #Llamamos a la funcion mensaje para que se ejecute el bloque de codigo que contiene.

#En este ejemplo se llama a la funcion mensaje tres veces, lo que hace que se ejecute el bloque de codigo que contiene tres veces
#  sin necesidad de escribir el mismo codigo tres veces.
# Se puede llamar a la funcion tantas veces como se quiera, lo que hace que el programa sea mas eficiente y facil de mantener.

# Ejemplo de que la funcion para llamarlas desde otras partes del codigo:

print("Ejecutando codigo fuera de la funcion mensaje") #Este codigo se ejecuta antes de llamar a la funcion mensaje.
mensaje() #Llamamos a la funcion mensaje para que se ejecute el bloque de codigo que contiene.
print("Ejecutando codigo despues de llamar a la funcion mensaje") #Este codigo se ejecuta despues de llamar a la funcion mensaje.