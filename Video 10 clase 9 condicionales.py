# Los condicionales

# instruccion IF

# Flujo de ejecucion de un programa

# Es el orden con el que se ejecuta sus instrucciones, un programa esta compuesto por varias instrucciones y el flujo de ejecucion es el orden que sigue el programa
# de leer y ejecutar esas instrucciones, normamente es de arriba hacia abajo.

# Si la condicion if es verdadera se sigue ejecutando el programa si no es verdadera en este caso falsa(false) deja de ejecutarse el programa ya que cuando se llega a la parte
# del IF empieza un flujo de ejecucion sea como lo hayamos programado y al no cumplirse con el IF no se ejecutaria si se cumpliera si se siguiera ejecutando.

# vamos a crear una evalucion usando una funcion dev evaluacion para comprobar si lo nota es mayor 5 dando como aprobado y si la suspende ejemplo:

def evaluacion(nota):
    valoracion="aprobado"
    if nota <5:
        valoracion = "suspenso"
    return valoracion

# print(evaluacion(4)) #para llamar a esta funcion se usa del siguiente ejemplo hay que darle un parametro para que nos de el resultado como pusimos prin(evaluacion(4))
# nos dara la valoracion suspenso por que esta el 4

# Los operadores de comparacion de python son > mayor que < menor que == igual que >= mayor o igual que <= menor o igual que y != diferente que

# Ahora vamos hacer le introduccion por teclado para que entre en nuestro programa y el programa nos de un resultado

# Con inpunt() es lo que permite que introduzcamos datos o informacion con el teclado

print("programa de evaluacion de alumnos")

nota_alumno=input() # Nota con Inpunt python cualqueir informacion introducida lo considera como texto o str

def evaluacion(nota):
    valoracion="aprobado"
    if nota <5:
        valoracion = "suspenso"
    return valoracion

# Ya la llamada no puede ser igual porque hel usuario debe introducirlo por teclado entonces seria como este ejemplo:

print(evaluacion(nota_alumno)) 

# Esto causa un error por que python esta detectasndo inpunt() como str 

# existe una forma para solucionar este problema que es con int() para que detecte el numero entero ejemplo seria:

print("programa de evaluacion de alumnos")

nota_alumno=input() # Nota con Inpunt python cualquier informacion introducida lo considera como texto o str

def evaluacion(nota):
    valoracion="aprobado"
    if nota <5:
        valoracion = "suspenso"
    return valoracion

# Ya la llamada no puede ser igual porque hel usuario debe introducirlo por teclado entonces seria como este ejemplo:

print(evaluacion(int(nota_alumno))) # Aqui estariamos diciendo que la nota_alumno lo transforme en un entero int, asi evitando el error

nota_alumno=input("Introduce la nota del alumno: ") # Nota dentro de los () de inpunt se puede intruducir un mensaje para eso deber estar ""

def evaluacion(nota):
    valoracion="aprobado"
    if nota <5:
        valoracion = "suspenso"
    return valoracion

# Nota una variable solo es accesible dentro de un ambito el ambito vendria siendo todo lo que esta dentro del if algo que se puede leer y manipular pero si declaramos
# otra variable y lo hacemos dentro del if solo es accesible dentro del bloque if o su ambito que vendria siendo dentro de if ejemplo:

def evaluacion(nota):
    valoracion="aprobado"
    if nota <5:
        valoracion = "suspenso"
        calificacion = 7
    return valoracion
