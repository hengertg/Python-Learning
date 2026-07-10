# ====================================================================================
# Hoy Veremos
#
# Punteros en texto
# ====================================================================================
#
# Como modificar la ubnicacion del puntero?
#
# Eso se hace con el metodo seek()
#
# Por ejemplo si le decimos seek(5) le decimos que se posicione en la posicion 5 del caracter
# ====================================================================================

from io import open

# ====================================================================================
# En python podemos hacer que un archivo sea modo lectura y escritura al mismo tiempo usando +
# ejemplo "r+"
#
# En el siguiente ejercicio se veria algo asi:
# ====================================================================================

archivo_texto = open("archivo_texto","r+")

# ====================================================================================
# Con la posicion 0 eso dira que este al final de todos los caracteres
#
# Con la posicion 0 eso dira que este al final de todos los caracteres
# ====================================================================================

# archivo_texto.seek(11)

# ====================================================================================
#
# Tambien se puede hacer esto mismo usando el method read() dentro de los parentesis() ahi colocamos nuestro parametro que seria 11 en este caso
#
#
# Esto le dice a python que lee hasta cierto punto o hasta la posicion del puntero que le hemos indicado
#
# Esto solo pasa con read() esta es la diferencia entre seek() y read()
# ==============================================================================

# print(archivo_texto.read(11))

# ==============================================================================
# Con esto archivo_texto.seek(len(archivo_texto.read())/2)
#
# Le estamos diciendo a python que en seek almacene la cantidad de texto divido entre 2 esto esta dando a entender que posicione
# el curso justamente entre la mitdad de todos los caracteres
#
# archivo_texto.seek(len(archivo_texto.read())/2)
# ==============================================================================

# Si quisieramos posicionar el cursor al final de la primera linea seria facil y sencillo que usar
#
# readline()
#
# y el codigo seria mas o menos el siguiente archivo_texto.seek(len(archivo_texto.readline()))

# archivo_texto.seek(len(archivo_texto.readline()))
# ==============================================================================

# ==============================================================================
#
# Si hacemos el siguiente comando de abajo python nos devolvera el texto en lista indicandonos cada linea de salto que existe

# print(archivo_texto.readlines())
# ====================================================================================

# ====================================================================================
# Como guardar el archivo de texto en forma de lista?
# ====================================================================================
#
# Podemos hacer esti almacenando el archivo de texto en una variable con .readlines();
#
# De la siguiente manera:

lista_texto = archivo_texto.readlines();

lista_texto[1] = " Esta linea ha sido incluido desde el exterior \n"

archivo_texto.seek(0)

# ====================================================================================
#
# el method .writelines() recibe como parametro solamente listas
#
# En esta ocasion como almacenamos en una variable una lista de nuestro archivo de texto deberiamos usar el siguiente methodo .writelines()
archivo_texto.writelines(lista_texto)

archivo_texto.close()