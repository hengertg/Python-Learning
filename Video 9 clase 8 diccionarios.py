# Los Diccionarios
# Son una estructura de datos que nos permite almacenar pares de clave-valor.
# Las claves deben ser únicas dentro del diccionario, y se utilizan para acceder a los valores almacenados en el diccionario.
# Los valores pueden ser de cualquier tipo de dato, incluyendo otros diccionarios, listas, tuplas, etc.
# La sintaxis para crear un diccionario es la siguiente: Nombre_del_diccionario = {clave1: valor1, clave2: valor2, clave3: valor3, ...}

# Los Dicionnarios
# Son esctructuras de datos que nos permite almacenar valores de diferentres tipos (Enteros, Flotantes, Cadenas de texto, Listas, Tuplas, Otros diccionarios).
# La principal caracteristiddca de los diccionarios es que los dato almacenan asociados a una clave de tal forma que se crea una asocion de tipo clave-valor. para cada
# elemento almacenado en el diccionario.

# Los elemenos almacenados no estan ordenados. el orden es indiferente a la hora de almacenar informacion en un diccionario.

Mi_diccionario = {"Republica Dominicana": "Santo Domingo", "Floida": "Miami", "Mexico": "Ciudad de Mexico", "Colombia": "Bogota"} # Para crear un diccionario
# se usan las llaves {} y dentro de las llaves se escriben los pares de clave-valor separados por comas. cada par de clave-valor se escribe con la clave seguida de dos puntos : 
# y luego el valor. # Nota los tipos texto se escriben entre comillas "" o '' y los numeros enteros o flotantes se escriben sin comillas.

# Para imprimir una parte del diccionario se puede usar la clave entre corchetes [] ejemplo:
print(Mi_diccionario["Republica Dominicana"]) #devuelve "Santo Domingo", el valor asociado a la clave "Republica Dominicana" en el diccionario Mi_diccionario

# Para imprimir el diccionario entero seria simplemente imprimir el nombre del diccionario, ejemplo:
print(Mi_diccionario) #devuelve el diccionario completo, con todas las claves y valores almacenados en el diccionario Mi_diccionario

# Como agregar mas elementos a un diccionario existente, ejemplo:
Mi_diccionario["Argentina"] = "Puerto plata" # Para agregar un nuevo elemento a un diccionario existente, se escribe el nombre del diccionario seguido
# de la nueva clave entre corchetes [] y luego se asigna el valor asociado a esa clave usando el caracter = # Nota esta incorrecto la ciudad a proposito pero hay forma de
# corregirlo.

# Como modificar un elemento existente en un diccionario, ejemplo:
Mi_diccionario["Argentina"] = "Buenos Aires" # Para modificar un elemento existente en un diccionario, se escribe el nombre del diccionario seguido de la clave entre corchetes []
# y luego se asigna el nuevo valor asociado a esa clave usando el caracter = # Nota se corrige la ciudad de Argentina a Buenos Aires.

print(Mi_diccionario)

# Como eliminar un elemento de un diccionario, ejemplo:
del Mi_diccionario["Colombia"] # Para eliminar un elemento de un diccionario, se usa la palabra reservada del seguida del nombre del diccionario y la clave entre corchetes []
print(Mi_diccionario) #devuelve el diccionario completo sin el elemento eliminado, en este caso el elemento con la clave "Colombia"
# ha sido eliminado del diccionario Mi_diccionario

Mi_diccionario2 = {"Alemania": "Berlin", 23: "Jordan", "Moesqueteros":3} # Para crear un diccionario se pueden usar diferentes tipos de datos
#para las claves y los valores, en este caso se usan cadenas de texto, numeros enteros y numeros flotantes como claves y valores.}

print(Mi_diccionario2) #devuelve el diccionario completo, con todas las claves y valores almacenados en el diccionario Mi_diccionario2

# Se puede utilizar una tupla para asignar un valor a una clave en un diccionario, ejemplo:

Mi_tupla=("Espana", "Francia", "Reino Unido")

Mi_diccionario3 = {Mi_tupla[0]: "Madrid", Mi_tupla[1]: "Paris", Mi_tupla[2]: "Londres"} # Para asignar un valor a una clave en un diccionario usando una tupla
# se escribe el nombre del diccionario seguido de la tupla entre corchetes [] y luego se asigna el valor asociado a esa clave usando el caracter =
#  # Nota se asigna el valor "Madrid" a la clave que es la tupla ("Espana", "Francia", "Reino Unido") en el diccionario Mi_diccionario3
print(Mi_diccionario3) #devuelve el diccionario completo, con todas las claves y valores almacenados en el diccionario Mi_diccionario3

# Para acceder a un elemento en concreto en el diccionaro seria

print(Mi_diccionario3["Francia"]) #devuelve el valor asociado a la clave "Francia" en el diccionario Mi_diccionario3, en este caso devuelve "Paris"

# Como hacer que un diccionario almacene una tupla entera de valores ejemplo:

Mi_diccionario4 = {23:"Jordan", "Nombre": "Michael", "Equipo": "Chicago Bulls", "Anillos": (1991, 1992, 1993, 1996, 1997, 1998)} # Para hacer que un diccionario
# almacene una tupla entera de valores
print(Mi_diccionario4)

# Si queremos acceder algunos de los valores ejemplo saber en que equipo jugo Jordan seria:

print(Mi_diccionario4["Equipo"]) # Me daria los resultados que estan almacenados en "Equipo"

# Si quisiera acceder al de los anillos seria de la misma manera ejemplo:

print(Mi_diccionario4["Anillos"]) # Me daria el resultado que estan almacenados en "Anillos"

# Para guardar un diccionaro dentro de otro diccionario seria lo siguiente: En este ejemplo seria en modo de lista en ves de una tupla pero tiene la misma logica
# si hacemos un diccionario como una lista.

Mi_diccionario5 = {23:"Jordan", "Nombre": "Michael", "Equipo": "Chicago Bulls", "Anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(Mi_diccionario5["Anillos"]) # Aqui imprimiria el sub dicccionario "temporadas" que creamos dentro del diccionario 

# Hay diferente tipos de metodos para un diccionario esta keys que nos devuelve las clave de un diccionario, el metodo values que nos devuelve los valores,
# y el metodo len que nos devuelve la logintud ejemplo:

print(Mi_diccionario5.keys()) # Este es un ejemplo con el metodo keys, siempre deber usarse con .keys()

print(Mi_diccionario5.values()) # Este es un ejemplo con el metodo values, siempre deber usarse con .values()

print(len(Mi_diccionario5)) # Este es un ejemplo con el metodo len, siempre despues del print() deber ir len ejemplo print(len(Aqui dentro va el diccionaro, lista o tuple))
