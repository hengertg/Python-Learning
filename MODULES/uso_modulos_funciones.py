# import funciones_matematicas

#=======================================================================================================================================================================================================================
# Para importar un modulo en python se usa
#
# import + el nombre del modulo
#
# Asi como en el ejemplo del principio
#
# El modulo es basicamente otro archivo.py con codigo dentro en la cual podemos reutilizar
#=======================================================================================================================================================================================================================



#=======================================================================================================================================================================================================================
# Como usar un modulo en el codigo?
#
# Para eso debemos usar la nomenclatura del .
# Porque no basta con poner el nombre de la variable
# En python debemos darle a entender que vamos a utilizar un codigo de otro archivo
# y para eso es la nomenclatura del punto
#
# Por Ejemplo se haria de la siguiente manera
#
# nombre del modulo + . + tu variable
#
# En este caso como hicimos una funcion de suma seria de la siguiente manera
#
# nombre del modulo + . + funcion(valor+valor)
#
# Vendria siendo funciones_matematicas.plus(7,5)
#=======================================================================================================================================================================================================================

# funciones_matematicas.plus(7,5)

# funciones_matematicas.minus(9,5)

# from funciones_matematicas import plus

from funciones_matematicas import *

#=======================================================================================================================================================================================================================
#
# Si queremos evitar usar la nomeblatura del punto y tener que repetir codigo hay un modo
#
# si usamos from + nombre de modulo + import + la funcion, clase, variable o lo que sea que hayamos escrito en codigo que queramos usar.
#
# Esto no permite utulizar codigo en especifico del modulo que habiamos hecho anteriormente para ahorrarnos codigo
# por ejemplo en este caso donde tenemos un modulo con funciones aritmeticas
#
# con usar plus(valor, valor) ya seria mas que sunficiente y funcionaria y no tendria que poner el nombre del mudulo. delante
#
# Pero esto tiene un problema que solo nos permite usar cierto codigo en especifico
#
# pero si queremos aplicar esta misma logica y usar todo lo que tenemos del codigo en el modulo sin necesidad de usar nombre del modulo.
#
# podemos usar * 
# Incluyendo un asterisco le damos a entender a python que queremos utilizar todo el codigo que hay dentro de nuetro modulo que en este caso es funciones_matematicas.
#
#======================================================================================================================================================================================================================
# NOTA
#=======================================================================================================================================================================================================================
# Existen diferentes situaciones en la cual no usaremos from funciones_matematicas import *, from funciones_matematicas import plus o import funciones_matematicas ya que esto dependeria de lo que quisieramos hacer
# porque asi ahorrariamos memoria y asi el programa o el codigo seria mas rapido en pocas palabras es una question de optimizacion a la hora de usar aplicaciones muy complejas porque como lo usariamos
# estariamos reservando un espacio en la memoria.
#=======================================================================================================================================================================================================================

plus(7,5)

minus(9,5)

times(5,6)