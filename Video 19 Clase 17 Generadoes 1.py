# Ejemplos practicos de generadores 

# Creacion de lista de numeros pares

def generaPares(limite):

    num=1

    miLista=[]

    while num<limite:

        miLista.append(num*2)

        num+=1

    return miLista
    
print(generaPares(10))


# Ahora Ejemplo utilizando un generador

def GeneraPares2(limite): # Aqui tenemos una funcion generadora que se llama GeneraPares2, esta funcion recibe un parametro limite que es el numero hasta el cual se generaran los numeros pares, este parametro
    # se usara para controlar el bucle while y evitar que se generen numeros pares indefinidamente
    
    num=1 # Aqui tenemos una variable num que se inicializa en 1, esta variable se usara para generar los numeros pares multiplicandola por 2, y se ira incrementando en cada iteracion del bucle while

    while num<limite: # Aqui tenemos un bucle while que se ejecuta mientras num sea menor que el limite establecido, esto hace que el generador genere los numeros pares hasta el limite establecido

        yield num*2 # Aqui usamos yield en lugar de return, esto hace que el generador devuelva un valor cada vez que se llama a la funcion y se detenga en ese punto hasta que se vuelva a llamar,
        # esto permite generar los valores de forma secuencial sin tener que almacenar todos los valores en memoria como en el caso anterior con la lista

        num+=1 # Aqui incrementamos num en 1 para generar el siguiente numero par en la siguiente iteracion del bucle while, esto hace que el generador genere los numeros pares de forma secuencial
        #hasta el limite establecido

devuelvePares=GeneraPares2(10) # Nota aqui tenemos que crear una variable para almacenar el generador y = GeneraPares2(10) esto hace que se ejecute el codigo del generador y se almacene en la variable devuelvePares

for i in devuelvePares: # Nota 2 Aqui tenemos que usar un bucle for para recorrer el generador y mostrar los valores que va generando, cada vez que se llama a devuelvePares se ejecuta el codigo del generador
    # hasta llegar al yield y devuelve el valor generado, luego vuelve a ejecutar el codigo hasta llegar al siguiente yield y asi sucesivamente hasta que se termine
    #  el codigo del generador o se alcance el limite establecido

    print(i)


# En caso de que queramos imprimir ciertos elementos por ejemplo 2 elementos o 1 elemntos se haria de la siguiente manera:

# Vamos a usar el metodo next() para obtener el siguiente valor generado por el generador, cada vez que se llama a next() se ejecuta el codigo del generador hasta llegar al siguiente yield y devuelve el valor generado

# Ejemplo:

def GeneraPares3(limite): 
    
    num=1 
    while num<limite: 

        yield num*2 

        num+=1

devuelvePares=GeneraPares3(10)

print(next(devuelvePares)) # Aqui usamos next() para obtener el siguiente valor generado por el generador, cada vez que se llama a next()
# se ejecuta el codigo del generador hasta llegar al siguiente yield y devuelve el valor generado

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))

