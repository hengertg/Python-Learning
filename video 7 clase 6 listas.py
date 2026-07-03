# La Listas

#Las listas son un tipo de dato que nos permite almacenar una colección de elementos. 
# (equivalente a los arrays en otros lenguajes de programación)

# En python las listas pueden guardar diferentes tipos de datos (en otros lenguajes no ocurre esto con los arrays)

# Se pueden expandir dinamicamente anadiendo nuevos elementos (otra novedad respecto a los arrays en otros lenguajes)

# Ejemplo de sintaxis de las listas:

Nombre_de_la_lista = [elemento1, elemento2, elemento3, ...] #el contenido debe estar entre corchetes y separado por comas

# los elemntos de la lista deben estar identificados y localizables por su indice (posicion) dentro de la lista, el primer elemento
#  tiene el indice 0, el segundo el indice 1, y asi sucesivamente en otras palabras los indices vendrian siendo elemnto1 = indice 0,
#  elemento2 = indice 1, elemento3 = indice 2, etc

# Siempre se empieza a contar desde el indice 0,
#  por lo que el ultimo elemento de la lista se encuentra en el indice n-1, donde n es la cantidad de elementos en la lista

# Nota las listas tipo textos deben estar entre comillas simples o dobles
#  las listas tipo numeros no necesitan comillas, y las listas tipo booleanos
#  deben escribirse con la primera letra mayuscula (True o False)

# Ejemplo de una lista con diferentes tipos de datos:

Mi_lista = ["Hola", 42, True, 3.14, "Mundo", False]
# En este ejemplo, Mi_lista es una lista que contiene una cadena de texto ("Hola")
#  un número entero (42), un valor booleano (True)
#  un número decimal (3.14), otra cadena de texto ("Mundo") y otro valor booleano (False)

Mi_lista2 = [1, 2, 3, 4, 5]
# En este ejemplo, Mi_lista2 es una lista que contiene cinco números enteros del
# 1 al 5.

Mi_lista3 = ["Python", "es", "genial"]
# En este ejemplo, Mi_lista3 es una lista que contiene tres cadenas de texto: "Python", "es" y "genial".

Mi_lista4 = [True, False, True, False]
# En este ejemplo, Mi_lista4 es una lista que contiene cuatro valores booleanos: True

Mi_lista5 = [3.14, 2.718, 1.618]
# En este ejemplo, Mi_lista5 es una lista que contiene tres números decimales: 3.14, 2.718 y 1.618.

Mi_lista6 = ["Python", 3.14, True, "es", 42, False]
# En este ejemplo, Mi_lista6 es una lista que contiene una mezcla de diferentes tipos de
#  datos: una cadena de texto ("Python"), un número decimal (3.14), un valor booleano (True)
#  otra cadena de texto ("es"), un número entero (42) y otro valor booleano (False).