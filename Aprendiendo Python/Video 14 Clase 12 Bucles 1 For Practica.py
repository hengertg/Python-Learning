# Practica del bucle for

# Para usarlo se hace de la siguiente manera:


for i in [1,2,3]: # Para iniciar el bucle se comienza con For luego la variable(puede ser tan larga como quieras) en este caso i y el elemento que puede ser una lista
  # un tuple, un texto un rango etc, en este caso es una lista.  
    
  print("hola")

# En este caso el codigo imprimira 3 veces el mensaje hola porque en la lista hay 3 elementos 1,2,3

for i in ["primavera","verano","otono","invierno"]:
    print("Hola")

# En este caso imprimiria el print("Hola") 4 veces porque hay 4 elementos en la lista primavera, verano, otono, invierno

# En este caso la variable i lo que hace es decir que es igual al primer elemento de la lista ejemplo i="primavera" una vez que el programa sabe que i="primavera"
# Ejecuta la linea que hay en su interior y asi sucesivamente i="verano", i="otono" i="invierno" y una vez llegue al final deja de ejecutarse el bucle

# Pero que pasaria si en un ejemplo ponemos print(i)

for i in ["primavera","verano","otono","invierno"]:
    print(i) # Esto imprimiria los variables que estan almacenadas en la variable del bucle que es i