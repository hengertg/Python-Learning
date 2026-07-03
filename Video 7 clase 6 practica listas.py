# Practica de las listas video 7 clase 6

Mi_lista = ["Henger", "Daniela", "Jhoswar", "Santiago", "Valentina"]

# Imprimir la lista completa
print(Mi_lista[:]) # Imprime toda la lista print(Mi_lista) # esto se puede usar para imprimir toda la lista
# pero es mas recomendable usar la sintaxis de los corchetes [:] para indicar que se quiere imprimir toda la lista

# si queremos imprimir un elemento especifico de la lista, podemos usar su indice (posicion) dentro de la lista
# por ejemplo, para imprimir el primer elemento de la lista, que es "Henger",
#  podemos usar el indice 0, ya que el primer elemento de la lista se encuentra en el indice 0
print(Mi_lista[0]) # Imprime el primer elemento de la lista, que es

# Ejemplo si intentamos imprimir un elemento que no existe en la lista, por ejemplo el indice 5, que no existe en esta lista
# print(Mi_lista[5]) # Esto generaria un error o excepcion, ya que el indice 5 no existe en la lista
#  Mi_lista, que solo tiene indices del 0 al 4 ejemplo de error: IndexError: list index out of range

# print(Mi_lista[6]) # imprime el error list index out of range, ya que el indice 6 no existe en la lista Mi_lista

# Una particularidad con python con las listas usando indices negativos, se puede acceder a los elementos de la lista desde el final
#  hacia el principio usando indices negativos, por ejemplo el indice -1 se refiere al ultimo elemento de la lista
#  el indice -2 se refiere al penultimo elemento de la lista, y asi sucesivamente
print(Mi_lista[-1]) # Imprime el ultimo elemento de la lista, que es "Valentina" 

# cuando existen lsitas muy largas existe algo llamado porcion de lista o slicing, que nos permite imprimir solo una parte de la lista
#  usando indices de inicio y fin
#  por ejemplo, para imprimir los primeros tres elementos de la lista, podemos usar los indices
#  0 y 3, ya que el indice de inicio es inclusivo y el indice de fin es exclusivo, es decir, se imprime el elemento en el indice de inicio
#  pero no se imprime el elemento en el indice de fin
print(Mi_lista[0:3]) # Imprime los primeros tres elementos de la lista
#  que son "Henger", "Daniela" y "Jhoswar"

# Hyay nonmeclatura abreviadas para el slicing, por ejemplo, si queremos imprimir los primeros tres elementos de la lista
#  podemos usar la sintaxis abreviada print(Mi_lista[:3])
#  # Imprime los primeros tres elementos de la lista, que son "Henger", "Daniela" y "Jhoswar"
print(Mi_lista[:3]) # Imprime los primeros tres elementos de la lista, que son "Henger", "Daniela" y "Jhoswar"

print(Mi_lista[1:2]) # Imprime el segundo elemento de la lista, que es "Daniela" Excluyendo el primer elemento "Henger" 
# y el tercer elemento "Jhoswar" y asi sucesivamente, se puede usar el slicing para imprimir cualquier porcion de la lista que se desee
#  siempre respetando la sintaxis de los indices de inicio y fin.

print(Mi_lista[2:]) # Imprime desde el tercer elemento de la lista hasta el final, que son "Jhoswar", "Santiago" y "Valentina"

# Para agregar elementos a la lista, se puede usar el metodo append() que nos permite agregar un elemento al final de la lista
Mi_lista.append("Maria") # Agrega el elemento "Maria" al final de la lista
print(Mi_lista[:]) # Imprime la lista completa, que ahora incluye el nuevo elemento "Maria" al final de la lista

# Si queremos que se agregue un elemento en una posicion especifica de la lista, se puede usar el metodo insert()
#  que nos permite agregar un elemento en una posicion especifica de la lista ejemplo:
Mi_lista.insert(2, "Carlos") # Agrega el elemento "Carlos" en la posicion 2 de la lista, es decir, entre "Daniela" y "Jhoswar"
# primero la posicion donde se quiere agregar el elemento, y luego el elemento que se quiere agregar
print(Mi_lista[:]) # Imprime la lista completa, que ahora incluye el nuevo elemento "Carlos"

# si queremos agregar varios elementos a la lista, se puede usar el metodo extend()
#  que nos permite agregar varios elementos al final de la lista
Mi_lista.extend(["Ana", "Luis", "Pedro"]) # Agrega los elementos "Ana", "Luis" y "Pedro" al final de la lista
print(Mi_lista[:]) # Imprime la lista completa, que ahora incluye los nuevos elementos "Ana", "Luis" y "Pedro" al final de la lista

# Si queremos saber donde se encuentra un elemento especifico dentro de la lista, se puede usar el metodo index()
#  que nos devuelve el indice del primer elemento que coincide con el valor buscado ejemplo:
print(Mi_lista.index("Santiago")) # Imprime el indice del elemento "Santiago" en la lista, que es 4
#  ya que el elemento "Santiago" se encuentra en la posicion 4 de la lista, contando desde el indice 0

# Podemos comprobar si un elemento se encuentra en la lista usando el operador in, que nos devuelve un valor booleano (True o False)
#  dependiendo de si el elemento se encuentra o no en la lista ejemplo:
print("Carlos" in Mi_lista) # Imprime True, ya que el elemento "Carlos" se encuentra en la lista
print("Sofia" in Mi_lista) # Imprime False, ya que el elemento "Sofia" no se encuentra en la lista

# Tambien nos pueden dar dartos con diferentes tipos de datos, por ejemplo
Mi_lista2 = ["Henger", 2, True, 78.35] # Lista de diferentes tipos de datos. Texto, numero entero, booleano y numero decimal
print(Mi_lista2[:]) # Imprime la lista completa, que contiene diferentes tipos de datos

# Para eliminar un elemento de la lista, se puede usar el metodo remove() que nos permite eliminar un elemento especifico de la lista
Mi_lista.remove("Carlos") # Elimina el elemento "Carlos" de la lista
print(Mi_lista[:]) # Imprime la lista completa, que ya no incluye el elemento "Carlos"

# para eliminar el ultimo elemento de la lista, se puede usar el metodo pop() que nos permite eliminar el ultimo elemento de la lista
Mi_lista.pop() # Elimina el ultimo elemento de la lista, que es "Pedro"
print(Mi_lista[:]) # Imprime la lista completa, que ya no incluye el elemento "Pedro"

# podemos sumar listas usando el operador +, que nos permite concatenar dos listas ejemplo:
Mi_lista3 = Mi_lista + Mi_lista2 # Crea una nueva lista que es la concatenacion de Mi_lista y Mi_lista2
print(Mi_lista3[:]) # Imprime la lista completa, que es la concatenacion de Mi_lista y Mi_lista2

# Tambien podemos usar el operador * para repetir una lista un numero determinado de veces ejemplo:
Mi_lista4 = Mi_lista * 2 # Crea una nueva lista que es la repetición de Mi_lista
print(Mi_lista4[:]) # Imprime la lista completa, que es la repetición de Mi_lista

# Otra forma de usar el operador * seria ejemplo:
Mi_lista5 =["Juan", "Marta"] * 3 # Crea una nueva lista que es la repetición de ["Juan", "Marta"] tres veces
print(Mi_lista5[:]) # Imprime la lista completa, que es la repetición

print(len(Mi_lista2)) # Con len podemos sab er la logintud de la lista siempre despues del primer parentesis deber ir len print(len(aqui la lista))