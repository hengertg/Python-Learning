# Video 4 Clase 3

#En python existen operadores aritmeticos para realizar operaciones matematicas, como suma, resta, multiplicacion, division, etc. ejemplo:

5+6 #suma
5-6 #resta
5*6 #multiplicacion
5/6 #division
5%6 #modulo, devuelve el resto de la division
5//6 #division entera, devuelve el cociente de la division sin decimales
5**6 #potencia, devuelve el resultado de elevar el primer numero al segundo numero 

#Como declarar variables con operadores aritmeticos, se puede usar cualquier operador para asignar el valor a la variable, ejemplo:
suma = 5 + 6
suma

resta = 5 - 6
resta

multiplicacion = 5 * 6
multiplicacion

division = 5 / 6
division

modulo = 5 % 6
modulo

division_entera = 5 // 6
division_entera 

potencia = 5 ** 6
potencia

#Tambien se pueden usar operadores aritmeticos para realizar operaciones con variables, ejemplo:

a = 10
b = 5  
suma_variables = a + b
suma_variables

resta_variables = a - b
resta_variables 

multiplicacion_variables = a * b
multiplicacion_variables

division_variables = a / b
division_variables

modulo_variables = a % b
modulo_variables    

division_entera_variables = a // b
division_entera_variables

potencia_variables = a ** b
potencia_variables

#funcion type() para conocer el tipo de dato de una variable, ejemplo:

c = 20
type(c) #devuelve el tipo de dato de la variable c, en este caso es int (entero) #nota: los numeros enteros se consideran int en python
d = 10
type(d) #devuelve el tipo de dato de la variable d, en este caso es int (entero) #nota: los numeros enteros se consideran int en python
e = 3.14
type(e) #devuelve el tipo de dato de la variable e, en este caso es float (decimal) #nota: los numeros con decimales se consideran float en python

nombre = "Henger"
type(nombre) #devuelve el tipo de dato de la variable nombre, en este caso es str (cadena de texto) #nota: las cadenas de texto se consideran str en python

booleano = True
type(booleano) # devuelve el tipo de dato de la variable booleano, en este caso es bool (booleano) # nota: los valores booleanos se consideran bool en python,
# y que pueden ser True o False, y se usan para representar valores de verdad en las operaciones logicas y condicionales.d

#Tambien se pueden usar operadores aritmeticos para realizar operaciones con diferentes tipos de datos, ejemplo:
f = 10
g = 3.14
suma_diferentes = f + g
suma_diferentes #devuelve 13.14, el resultado de sumar un entero con un decimal es un decimal (float) #nota: cuando se suman diferentes tipos de datos
#el resultado es del tipo de dato mas grande en este caso el float es mas grande que el int, por lo tanto el resultado es un float
type(suma_diferentes) #devuelve el tipo de dato de la variable suma_diferentes, en este caso es float (decimal)
 #nota: el resultado de sumar un entero con un decimal es un decimal (float)

#Tambien se pueden usar operadores aritmeticos para realizar operaciones con diferentes tipos de datos, ejemplo:
h = 10
i = "Henger"
suma_diferentes2 = h + i #devuelve un error, no se pueden sumar un entero con una cadena de texto, ya que son tipos de datos incompatibles
#nota: para sumar un entero con una cadena de texto, se debe convertir el entero a cadena de texto usando la funcion str(), ejemplo:
suma_diferentes3 = str(h) + i
suma_diferentes3 #devuelve "10Henger", el resultado de sumar un entero convertido a cadena de texto con una cadena de texto es una cadena de texto (str) 
#nota: el resultado de sumar un entero convertido a cadena de texto con una cadena de texto es una cadena de texto (str)
type(suma_diferentes3) #devuelve el tipo de dato de la variable suma_diferentes3, en este caso es str (cadena de texto) 
#nota: el resultado de sumar un entero convertido a cadena de texto con una cadena de texto es una cadena de texto (str)    

#Para incluir saltos de linea dentro de un texto con una variable se puede usar el caracter """" ejemplo:
texto_con_salto_de_linea = """Hola, este es un texto con salto de linea
este es el salto de linea y este es el final del texto"""
print(texto_con_salto_de_linea) #devuelve el texto con el salto de linea incluido, el caracter """" permite incluir saltos de linea dentro de un texto

#Otra forma de incluir saltos de linea dentro de un texto es usando el caracter "\n" ejemplo:
texto_con_salto_de_linea2 = "Hola, este es un texto con salto de linea\neste es el salto de linea y este es el final del texto"
print(texto_con_salto_de_linea2) #devuelve el texto con el salto de linea incluido, el caracter "\n" permite incluir saltos de linea dentro de un texto

#Uso del condicional if para realizar operaciones dependiendo de una condicion, ejemplo:
edad = 18 
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

#Otro ejemplo de uso del condicional if para realizar operaciones dependiendo de una condicion, ejemplo:
numero10 = 10
numero20 = 20
if numero10 > numero20:
    print("El numero 10 es mayor que el numero 20")
elif numero10 < numero20:
    print("El numero 10 es menor que el numero 20")
else:    print("El numero 10 es igual al numero 20")
#Nota: el condicional if se puede usar para realizar operaciones dependiendo de una condicion, se pueden usar los operadores de comparacion
#  para comparar diferentes valores, como >, <, >=, <=, ==, !=, etc.
#Nota2: elif se usa para agregar una condicion adicional a la condicion if, y else se usa para agregar una accion
#  a realizar cuando ninguna de las condiciones anteriores se cumple.
#Nota3: else es opcional, se puede usar solo if y elif
#  sin necesidad de usar else, pero si se usa else, debe ser el ultimo bloque de codigo despues de todos los bloques if y elif.

#Nota: el caracter = se usa para asignar un valor a una variable, mientras que el caracter == se usa para comparar dos valores, ejemplo:
x = 10 #asignacion, se asigna el valor 10 a la variable x
y = 20 #asignacion, se asigna el valor 20 a la variable y
x == y #comparacion, devuelve False, ya que el valor de x es diferente al valor de y
x == 10 #comparacion, devuelve True, ya que el valor de x es igual al valor 10