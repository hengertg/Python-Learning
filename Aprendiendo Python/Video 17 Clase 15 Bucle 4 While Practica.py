# Practica bucle While

# i=1

# while i <=10:
#    print("Ejecucion" + str(i))

# print ("Termino la ejecucion")


# Arriba estamos viendo un ejemplo de bucle infinito jamas llegara a leer la ultima linea del programa

# Esto pasa porque el programa entra dentro del bucle print("Ejecucion" + str(i)) porque el flujo de ejecucion entra en el bucle que
# que la evalua como verdadera y la sigue ejecutando, para resolver esto debemos escribir una condicion que pase a ser falsa ejemplo

i=1

while i <=10:
    print("Ejecucion " + str(i))
    i=i+1 # Esto vendria siendo un contador, estamos incrementando en 1 la variable i cuando entre por segunda vez el bucle
    # la i valdra 2 pero en este ejemplo vendria valiendo 11

print ("Termino la ejecucion")


# 2do Ejemplo donde veremos la naturaleza del bucle While

# Programa de edad 

# En este caso haremos un programa en donde si ponemos una edad negativa nos lo dara como invalido y nos preguntara que
# coloquemos una edad

# Ejemplo:

edad=int(input("Introduce tu edad por favor: "))

while edad<0:
    print("Has introducido una edad negativa. Vuelve a intentarlo")
    edad=int(input("Introduce tu edad por favor: ")) # Como vemos en este ejemplo esto seria un bucle con while en la cual no tiene definicion hasta que introduzcamos
    # la opcion correcta en este caso una edad que no sea negativo para que de como finalizado el bucle.

print("Gracias por colaborar, puedes pasar")
print("Tu edad es: " + str(edad))


# Otro ejemplo de edad en dado caso de que la edad sea mayor a lo comun

edaduser=int(input("Introduce tu edad por favor: "))

while edaduser<5 or edaduser>100:
    print("Has introducido una edad incorrecta. Vuelve a intentarlo")
    edaduser=int(input("Introduce tu edad por favor: ")) 

print("Gracias por colaborar, puedes pasar")
print("Tu edad es: " + str(edaduser))

# Ejemplo como hacer que un bucle no sea infinito por mucho que el usuario quiera hacerlo infinito ejemplo:

import math # para usar clases en python hay que importarla y eso se hace en la primera lina del codigo ejemplo import math en este caso como esta escrito primeramente

print ("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero por favor: "))

intentos=0

while numero<0:
    print("No se puede hallar la raiz de un numero negativo")

    if intentos==2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break; # Que es brake. Brake es una instruccion que te permite salir del bucle y continuar la ejecucion del programa si hay mas codigo de programa cuando se lea y
# me permite seguir dentro del if

    numero=int(input("Introduce un numero por favor: "))
    if numero<0:
        intentos=intentos+1 # Nota para hacer un contador siempre tengo que crear una variable y darle un valor numero y para ejecutar el contador o hacerlo funcionar
        # es como en el ejemplo anterior intentos=intentos+1
if intentos<2:
    solucion=math.sqrt(numero)

    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))