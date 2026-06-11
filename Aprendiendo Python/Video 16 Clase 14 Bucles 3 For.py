# Hoy veremos a mas detalle range() en los bucles

import email


for i in range(5):
    print(f"Valor de la variable {i}")   # En este ejemplo el tipo f le estamos dando a python una notacion especial siempre debe ir {} para concatenar el texto
                                         # Si no le ponemos el f python no la entenderia


for i in range(5,10): # En Este ejemplo estamos haciendo que con el range cuente desde el 5 hasta el 9 
    # Nota esto siempre debe estar separado por , el primero numero es el inicio y el segundo numero es el final 5,10 del 5 hasta el 9
    print(f"Valor de la variable {i}")

   
for i in range(5,50,3): # En este ejemplo contara desde el 5 hasta el 50 de 3 en 3 
     # nota para este caso aqui hay 3 numeros el primer numero donde iniciar el segundo la cantidad o hasta donde y el tercero de cuanto en cuanto se contara 5,50,3 siempre debe ir
     # separados por ,
    print(f"Valor de la variable {i}")


# En el bucle for en python tenemos la funcion len la cual nos devolvera la logintud o la cantida de caracteres ejemplo:

len("juan") # Aqui nos devovler la cantidad de caracteres que estan dentro del ("juan") que vendria siendo 1234


# Ejemplo de bucle for para comprobar si un email es correcto o no con range()

Valido=False
EmailUser=input("Introduce tu Email: ")

for i in range(len(email)): # Este bucle for lo que hace es en len devolver la logintud del string (En este caso de la variable EmailUser) nos devolveria la cantidad de elementos
    # o en otras palabras dara la cantidad de vuelta de bucles como lo tenemos en "@" hasta que no de el @ no lo dara como valido

    if email[i]=="@":
        valido=True

if valido:

    print("El Email es correcto")

else:
    
    print("Email incorrecto")