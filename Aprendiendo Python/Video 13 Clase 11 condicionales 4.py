# Hoy Veremos los operadores and & or y tambien el operador in

# Ejemplo de codigo donde veremos si un alumno tiene derecho a beca o no.

# Este programa evaluara la distancia del alumno, si tiene mas hermanos en el centroy el salario familiar.

from pickle import OBJ


print("Programa de becas ano 2026")

distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce cuantos hermanos tienes: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario familiar: "))
print(salario_familiar)


if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 20000: # Con el operador "and" obligamos a que se cumpla toda ya que se traduciria como y si ejemplo distancia
    # mayor a 40 y numero de hermanos mayor a 2 y salario menor o igual a 2000 entonces imprime tienes derecho a beca ya que es un y si debe pasar por cada condicion para que se cumpla
    print("Tienes derecho a beca")

else:
    print("No tienes derecho a beca")


# Ejemplo 2

# Como hacer que una funcion pese mas que otra o sea mas importante que otra.

# Para hacer eso podemos utilizar el operador or ya que se traduce como o ejempli si distancia > 40 y hermanos > 2 o salario familiar <= 20000 puede imprimir tienes derecho a beca
# haria que cumpliria lo del or ejemplo:

print("Programa de becas ano 2026")

distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce cuantos hermanos tienes: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario familiar: "))
print(salario_familiar)


if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000: # aqui estamos utulizando el operador or para en dado caso de no cumplir una de las 2 funciones pero cumpla
    # la tercera la de como valida porque se traduciria como o.
    print("Tienes derecho a beca")

else:
    print("No tienes derecho a beca")

# Ejemplo de operador in:

# Programa donde un alumno tiene que cursar una carrera ejempli informatica y tiene que escoger una asignatura de la cual no se puede salir si escoge una de la lista el programa
# le dice que esta contemplada en caso contrario no esta contemplada

print("Asignatura optativas ano 2026")

print("Asignatura optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

Asignatura=input("Escibre la asignatura escogida: ")

if Asignatura in ("Informatica grafica", "Pruebas de software", "Usabilidad y accesibilidad"): # como tenemos que comprar valores de tipo string tienen que ir "" entre las comillas y separados
    # por comas ,
    print("Asignatura elegida " + Asignatura) # aqui funciona el operador + porque los 2 son tipo str o cadena de texto "asignatura elegida" + asignatura, caso contrario hubiera un entero
    # habria que convertirlo porque daria un error

else:
    print("La asignatura escogida no esta contemplada")

# Nota: Python es case sensitive si no escribes igual que en el codigo no lo toma ejemplo si escribes con minuscula o mayuscula 
# hay una forma de solucionar ese problema y se hace de la siguiente manera usando la funcion lower() "lo transforma a minuscula" o upper() " transforma a mayusuclas"

# Ejemplo:

print("Asignatura optativas ano 2026")

print("Asignatura optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

Opcion=input("Escibre la asignatura escogida: ")

Asignatura=Opcion.lower()  # En este ejemplo creamos una variable donde le damos la funcion lower para que funcione esto siempre debe de empezar por .lower() o .upper()
# junto con la variable con input que hemos creado ejemplo: Asignatura=Opcion.lower()

# En pocas palabras lo que esta haciendo es todo lo que escibamos en el opcion=input lo esta convirtiendo a minusculas esa seria la logica

if Asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"): 
    print("Asignatura elegida " + Asignatura) 

else:
    print("La asignatura escogida no esta contemplada")