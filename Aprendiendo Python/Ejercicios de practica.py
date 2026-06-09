#Ejercicio de practica, crear 2 variables

#Suma de las variables

a = 15
b = 7

c = a + b
print(c)
print(type(c)) #con print(type(c)) se muestra el tipo de dato de la variable c, en este caso es un int (entero) porque la suma de dos enteros da como resultado un entero.

#Restar de las variables

d = a - b
print(d)
print(type(d))

#Multiplicar las variables 

e = a * b
print(e)
print(type(e))

#Dividir las variables

f = a / b
print(f)
print(type(f))

#Modulo de las variables 
g = a % b
print(g)
print(type(g))

#Division entera de las variables

h = a // b
print(h)
print(type(h))

#Potencia de las variables

i = a ** b
print(i)
print(type(i))

#Ejercicio 2 tipo de dato de las variables

nombre = "Nombre: \nHenger"  #Nota: el \n es un salto de linea, lo que hace que el texto se muestre en dos lineas
#en este caso "Nombre:" en la primera linea y "Henger" en la segunda linea. Tambien se puede usar """ para escribir un texto en varias lineas sin necesidad de usar el \n
#  ejemplo: nombre = """Nombre: Henger""" esto tambien mostrara el texto en dos lineas.
print(type(nombre))

edad = "Edad: \n20"
print(type(edad))

altura = "Altura: \n1.80"
print(type(altura))

print(nombre, edad, altura)

#Ejercicio 4, Mayor de edad

edad = int(input("Ingrese su edad: ")) #Nota: la funcion input() devuelve un valor de tipo str (cadena de texto) por lo que se debe convertir a int (entero)
#para poder comparar con el numero 18, si no se convierte a int se producira un error al intentar comparar un str con un int.
#Nota2: la funcion int() convierte un valor a entero, en este caso se convierte el valor ingresado por el usuario a entero para poder compararlo con el numero 18.
if edad >= 18:
    print("Eres mayor de edad")
elif edad < 18:
    print("Eres menor de edad")

#Ejercicio 5, Mayor de edad con else
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#ejercicio 6 Comparar numeros

numero1 = 50
numero2 = 100
if numero1 > numero2:
    print("El numero 1 es mayor que el numero 2")
elif numero1 < numero2:
    print("El numero 2 es mayor que el numero 1")
else:
    print("Los numeros son iguales")

