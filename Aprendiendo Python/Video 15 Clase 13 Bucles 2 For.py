# Hoy veremos recorrido strings
# El tipo Range
# Notaciones especiales con print.

for i in ["Henger", "YoPemka", 1]:
    print("Hola", end=" ") # El argumento end="" es para que finalice la extension en un espacio que no existe y no haga saltos de linea y este todo corrido
                            # Tambien se puede poner contenido dentro.






for i in "hengertg@outlook.com": # Cuando imprimos el print("Hola", end=" ") se imprimira tantas veces dependiendo cuantos caracteres hay
    print("Hola", end=" ")



# Con este sistema se pueden hacer varias cosas por ejemplo ver si un correo es correcto o no
# En este ejemplo estamos elaborando en python si un correo es correcta o no



Email=False # Nota el False y True en python van con la primera letra en mayuscula

for i in "hengertg@outlook.com":

    if(i=="@"):
        Email=True  

if Email==True:
    print("Email es corerecto")
else:
    print("Email es incorrecto")


Email=False # Nota el False y True en python van con la primera letra en mayuscula

for i in "hengertg@outlook.com":

    if(i=="@"):
        Email=True  

if Email: # Nota En python si ponemos if y la variable reduce el codigo sin necesidad de poner Email==True ya que python lo detecta autmaticamente o llama esa variable
    print("Email es corerecto")
else:
    print("Email es incorrecto")


# == compara 1 = asigna

#En este ejemplo vamos a hacer un sistema de correo electronicos donde el usuario podra colocar su correo y el codigo detectara si es correcto o no
# Ejemplo:


Email=False
EmailUser=input("Introduce tu Email: ")

for i in EmailUser:

    if(i=="@"): 
        Email=True  

if Email==True:
    print("Email es corerecto")
else:
    print("Email es incorrecto")


# Ejemplo para comprobanr si tiene un dominio

contador=0
EmailUser=input("Introduce tu Email: ")
# En este caso creamos 2 variables una que es contador que le dimos el valor 0 y la variable con la funcion input para introducir lo del teclado

for i in EmailUser: # Aqui creamos un bucle dando con lo que el usuario introduzca en el teclado en este caso al variable EmailUser

    if(i=="@" and i=="."):  # Aqui damos la instruccion del bucle para que cuando llegue a cierto carracter lo pueda dar como valido o no en este caso "@" y "."

        contador=contador+1 # Aqui estamos haciendo que la variable contatord sea igual a contador + 1 para cuando detecte 1 se sume por ejemplo @=0 .=1
        # Entonces da contador ==2 esto esta dando la confirmacion de la suma de 2 verificaciones con el if que hemos hecho

if contador==2: # Cuando la variable o las verificaciones sea igual a 2 como hicimos aqui en el anterior codigo imprimira que es correcto o dara el else que sea incorrecto
    print("Email es corerecto")
else:
    print("Email es incorrecto")

# El tipo range en un bucle for nos devolvera un contador o casi un contador

# Ejemplo

for i in range(5): # el range debe ir por () ejemplo range()
    # en este caso el range lo que esta haciendo es estar contando desde 0,1,2,3,4 porque comienza con el 0
    print("Hola") # Aqui imprimira hola 5 veces
    print(i) # Aqui imprimira 0,1,2,3,4

    