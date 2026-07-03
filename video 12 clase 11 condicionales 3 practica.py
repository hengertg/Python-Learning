
Edad=int(input("Introduce tu edad "))

def valor_edad(Edad):
    if 0<Edad<100:
        return "Edad Correcta"
        
    else:
        return"Edad no valida"
    
print(valor_edad(Edad))

enter=input("Presiona cualquier tecla para cerrar")




# En este ejemplo vamos a ver con el uso de numeros negativos en caso de introducir una edad negativa el programa nos de la edad incorrecta

# Pero usando los operadores de comparacion ejemplo:

edad=int(input("Introduce tu edad: "))

if 0<edad<100: # si usamos varias veces el oepradores de comparaciones en la misma linea nos ahorramos codigo dentro del if como en este ejemplo 
    # Nota el codigo o el flujo de ejecuccion lo leeria de izquierda a derecha como si se lee una linea de un libro
    print("La edad es correcta")
else:   
    print("la edad no es correcta")

# Segundo ejemplo de ahorro de codigo o contenacion

# Ejemplo de salarios de una empresa.

Salario_presidente=int(input("Introduce el salario del presidente "))
print("Salario_presidente: " + str(Salario_presidente)) # En Python como en otros lenguajes de programacion no se puede usar + para las cadenas de texto o str
# solo funciona con los enteros una solucion a esto es como el ejemplo presente que es anadiendo + str() y dentro del parantesis el contenido para que convierta el valor
# en string

Salario_director=int(input("Introduce el salario del director "))
print("Salario_director: " + str(Salario_director))

Salario_jefe_de_area=int(input("Introduce el salario del jefe de area "))
print("Salario_jefe_de_area: " + str(Salario_jefe_de_area))

Salario_administrativo=int(input("Introduce el salario administrativo "))
print("Salario_administrativo: " + str(Salario_administrativo))

if Salario_administrativo < Salario_jefe_de_area < Salario_director < Salario_presidente: # Como vemos aqui utilizamos el operador < varias veces para hacer el codigo
    # aqui diria si cada salario es menor que <
    # Nota se pueden utilizar distintos operadores no solo el < se puede usar > mayor que = igual que == igual que + mas - menor / division * multplicacion ** ponteciacion
    # // divion entera
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")