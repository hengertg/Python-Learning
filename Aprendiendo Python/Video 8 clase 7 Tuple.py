# Las Tuplas

# Las tuplas son similares a las listas, pero son inmutables, lo que significa que no se pueden modificar después de su creación.
#  Se definen utilizando paréntesis () en lugar de corchetes [].

# No Permiten anadir, eliminar o modificar elementos después de su creación. (no append, no remove, no pop, no clear, no sort, no reverse)
# Si permiten extraer porciones, pero el resultado de la extracion es una nueva tupla, no se modifica la tupla original.
# No  Permiten buesquedas (No index, no count) pero si permiten contar el numero de elementos o la cantidad de veces que se repite un elemento usando el metodo count()
#  y len() respectivamente.

# Si permiten comprobar si un elemento se encuentra en la tupla usando el operador in, que nos devuelve un valor booleano (True o False)

# Que utilidad o ventaja tienen respeco a las listas?

# Mas rapidas que las listas, ya que al ser inmutables, no requieren de la sobrecarga de memoria que implica la modificacion de una lista.
#  Esto las hace ideales para almacenar datos que no necesitan ser modificados, como coordenadas, fechas, etc.

# Menos espacions de memoria que las listas, ya que al ser inmutables, no requieren de la sobrecarga de memoria que implica la modificacion de una lista. 
# (Mayor optimizacion de memoria)

# Formatean strings de manera mas eficiente que las listas, ya que al ser inmutables, no requieren de la sobrecarga de memoria que implica la modificacion de una lista. 
# (Mayor optimizacion de memoria)

# Pueden utilizarse como clabes en un diccionario, ya que al ser inmutables, pueden ser hashables, lo que las hace ideales para utilizar como claves en un diccionario.
#  (Las listas no).

# Las tuplas van entre parentesis () tambien los parentesis pueden ser opcionales y los elementos deben estar separados por comas diferente a las listas que van entre corchetes []
#  y los elementos deben estar separados por comas

# Ejemplo de una tupla: nombre_de_la_tupla = (elemento1, elemento2, elemento3, ...)

Mi_tupla = ("Juan", 13,1,1995) # En este ejemplo, Mi_tupla es una tupla que contiene una cadena de texto ("Juan") y tres números enteros (13, 1 y 1995).
print(Mi_tupla[1]) # Imprime el segundo elemento de la tupla, que es el numero 13

# Tenemos 2 metodos para convertir una tupla en una lista y viceversa, el metodo list()
#  para convertir una tupla en una lista y el metodo tuple() para convertir una lista en una tupla ejemplo:

Mi_lista = list(Mi_tupla) # Convierte la tupla Mi_tupla en una lista y la almacena en la variable Mi_lista
print(Mi_lista) # Imprime la lista Mi_lista, que es la conversion de la tupla Mi_tupla

# Para convertir una lista en una tupla, se puede usar el metodo tuple() ejemplo:
Mi_lista2 = ["Henger", "Daniela", "Jhoswar", "Santiago", "Valentina"] # Creamos una lista con 5 elementos
Mi_tupla2 = tuple(Mi_lista2) # Convierte la lista Mi_lista2 en una tupla y la almacena en la variable Mi_tupla2
print(Mi_tupla2) # Imprime la tupla Mi_tupla2

# Con la instruccion in podemos comprobar si un elemento se encuentra en la tupla, lo que nos devuelve un valor booleano (True o False) ejemplo:
print("Juan" in Mi_tupla) # Imprime True, ya que el elemento "Juan" se encuentra en la tupla Mi_tupla
print("Maria" in Mi_tupla) # Imprime False, ya que el elemento

# El metodo count() nos permite contar cuantas veces se repite un elemento o cuantos elementos se encuentran en la tupla, lo que nos devuelve un numero entero ejemplo:
print(Mi_tupla.count(13)) # Imprime el numero de veces que se repite el elemento 13 en la tupla Mi_tupla, que es 1

# El metodo len() nos permite contar el numero de elementos o longitudes que se encuentran en la tupla, lo que nos devuelve un numero entero ejemplo:
print(len(Mi_tupla)) # Imprime el numero de elementos que se encuentran en la tupla Mi_tupla, que es 4

# Se pueden hacer tupla unitarias, es decir, tuplas con un solo elemento, pero para ello es necesario colocar una coma despues del elemento, ejemplo:
Mi_tupla3 = ("Henger",) # Tupla unitaria que contiene un solo elemento, que es la cadena de texto "Henger"
print(len(Mi_tupla3)) # Imprime la longitud de la tupla Mi_tupla3, que es 1

# Ejemplo de tupla sin parentesis:

Mi_tupla4 = "Pedro", 25, "Mendoza" # Tupla sin parentesis que contiene tres elementos: una cadena de texto ("Pedro"), un numero entero (25) y otra cadena de texto ("Mendoza")
print(Mi_tupla4) # Imprime la tupla Mi_tupla4

# Es mas recomendable usar los parentesis para definir las tuplas, ya que esto hace que el codigo sea mas legible y facil de entender
#  ademas de evitar posibles errores de sintaxis al no colocar la coma despues del elemento en una tupla unitaria.

# Desempaquetado de tuplas

Mi_tupla5 = ("Esther", 24, 12, 1998) # Tupla que contiene tres elementos: una cadena de texto ("Esther"), un numero entero (24)
nombre, dia, mes, ano = Mi_tupla5 # Desempaquetado de tuplas, donde se asignan los elementos de la tupla Mi_tupla5 a las variables nombre, dia, mes y año respectivamente
# Nota 2 Python automaticamente asigna los valores de la tupla a las variables, siempre y cuando el numero de variables sea igual al numero de elementos en la tupla
print(nombre) # Imprime el valor de la variable nombre, que es "Esther"
print(dia) # Imprime el valor de la variable dia, que es 24
print(ano) # Imprime el valor de la variable ano, que es 1998
print(mes) # Imprime el valor de la variable mes, que es 12

# Si usamos.append nos dara un error, ya que las tuplas son inmutables y no permiten modificar su contenido despues de su creacion
#  por lo que no se pueden agregar nuevos elementos a una tupla usando el metodo append() como se hace con las listas. Ejemplo de error:
#  AttributeError: 'tuple' object has no attribute 'append'

Mi_tupla.append("Maria") # Esto generaria un error, ya que las tuplas son inmutables y no permiten modificar su contenido despues de su creacion

# En las tuplas se puede usar index para buscar el indice de un elemento, pero no se puede usar el metodo index() como en las listas
#  ya que las tuplas no permiten modificar su contenido despues de su creacion

# Ejemplo de uso del operador in para comprobar si un elemento se encuentra en la tupla con index:
print(Mi_tupla.index("Juan")) # Imprime el indice del elemento "Juan" en la tupla Mi_tupla, que es 0
