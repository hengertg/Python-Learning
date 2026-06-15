for letra in "Python":

    if letra == "h":
        continue

    print("viendo la letra: " + letra)

    # En este ejemplo estamops usando el continue ner un bucle lo que esta haciendo en el codigo es ignorar una parte del bucle lo que esta ignorando es Viendo la letra h en el codigo en este ejemplo


    # Ejemplo de utilidad en la instruccion continue


nombre = "Henger Tejeda" 

contador=0

for i in nombre:

    if i == " ":
        continue

    contador+=1


print(contador)


# Ejemplo con instruccion pass

# while True:
    # pass

# Esto hace que manter el programa ocupado hasta que el usuario presiona ctrl + c ya que esta la instruccion pass


# Otro ejemplo de la instruccion pass

class MiClase:
     pass # para implementar mas tarde


# ese es otro ejemplo el pass se puede tambien utilizar en un def y en otros tipos de codigos


# Ejemplo de la instruccion else

# se puede utilizar dentro de los bucle y no es necesario porque tambien se pueder tener el mismo resultado sin utilizarlo


email=input("Introduce tu email, por favor: ")

for i in email:

   if i=="@": 

        arroba=True
        break;

else:
    arroba=False

print(arroba)

# El else solo va a funcionar cuando en el codigo termina o no queda mas que recoger como en este ejemplo para el flujo del codigo

