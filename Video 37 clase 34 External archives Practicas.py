from io import open

# ====================================================================================
# Primero debemos importar la herramienta IO
#
# que se hace como en el ejemplo de arriba from io import
# En este caso estaremos usando la instruccion open que lo que hara es abrir un archivo externo
# ====================================================================================
#
# ====================================================================================
# COMO CREAR UN ARCHIVO EXTERNO?
# ====================================================================================
#
# para crear un archivo externo es bastante sencillo
#
# usaremos el nombre del archivo + = + open() dentro de los parentesis debemos darle 2 argumentos ya que nos lo pedira
# 1 de ellos es el nombre del archivo que queremos abrir y el 2do es el modo en el que lo vamos abrir.
#
# Un archivo lo podemos abrir en modo lectura en caso de que solo queramos leer la informacion
#
# Y el otro es modo escritura en caso de que queremos modificar la informacion
#
# Tambine lo podemos abrir en modo append para agregar informacion a un archivo que ya existe y tiene informacion en su interior
#
# Y esto se veria mas o menos algo asi
#
# nombre_del_archivo_texto = open("nombre_del_archivo_texto", "w") la w significa que es write para que se abra en modo escritura
#
# Para mas info en base al io: https://docs.python.org/3/library/io.html

archivo_texto = open("archivo_texto","r")

# ====================================================================================
# Como anadir informacion en nuestro archivo con python?
# ====================================================================================
#
# Para esto es facil y sencillo en este caso crearemos una variable con un contenido str
#
# variable="texto"
#
# luego debemos darle a entender a python que queremos anadir esa informacion dentro del archivo
# 
# como se anade?
#
# Pues debemos llamar el archivo que hemos creado luego usamos la nomenclatura del punto + el modo que usamos que en este caso es write() y dentro de los parentesis
# va el parametro que usaremos en este caso es la variable con el texto str
# 
# Se veria algo mas o menos asi:
#
# archivo_texto.write(variable)

frase = "Estupendo dia para estudiar python \n el miercoles"

archivo_texto.write(frase)

# ====================================================================================
# Como cerramos un archivo?
# ====================================================================================
#
# Para cerrar un archivo es facil y sencesillo debemos anadir la funcion .close()
# 
# Esto sirve para finalizar o cerrar nuestro archivo en memoria una vez terminemos de anadir la informacion
#
# y para cerrar esto es facil
#
# nombre_del_archivo.close()


archivo_texto.close()

# ====================================================================================
# Como crear un archivo modo lectura?
# ====================================================================================
#
# Para crear un archivo modo lectuar es sencillo dentro del os parametros de open("Nombre del archivo", "r") usariamos una "r" que esto siginifica que es modo read o modo lectura
#
# Luego ya lo demas es similar.

archivo_texto2 = open("archivo_texto2","r")

# ====================================================================================
# Como leer ese archivo lectura
# ====================================================================================
#
# primero debemos crear una variable y esa variable darle la instrocion del archivo con .read()
#
# Ejemplo variable = archivo_texto2.read()
#
# Esto le dice que lea lo que hay dentro de ese archivo y que lo alamacene dentro de esa variable
#
# Y ya luego quedaria cerrarla con .close()
# ====================================================================================

texto = archivo_texto2.read()


archivo_texto2.close()

# ====================================================================================
# Que pasa si queremos imprimir ese archivo para mostrarlo en consola en python?
#
# Podemos usar print() + el nombre de la variable dentro de los parantesis o usarlo como parametro
#
# Ejemplo:

print(texto)


# ====================================================================================
# Como almacenar un archivo en una lista?
# ====================================================================================
#
# para hacer eso debemos hacer una variable + = + nombre del archivo + .readlines()
#
# Esto le decimos a python que guarder la informacion dentro de una lista
#
# esto se veria mas o menos algo asi
#
# variable = nombre_del_arcihvo.readlines()
#
# y esto hace que cada linea de texto corresponde a cada lista de linea

archivo_texto3 = open("archivo_texto3","r")

lineas_texto=archivo_texto3.readlines()

archivo_texto3.close()

print(lineas_texto[0])

# ====================================================================================
# Nota: podemos decirle en el print que queremos acceder al indice de el archivo de texto como en una lista
# con [] y la posicion del indice

# ====================================================================================
# Como anadir informacion a un archivo?
# ====================================================================================
#
# para eso usaremos el metodo append
#
# Como hacerlo?
#
# Primero usaremos lo que hemos visto que en este caso es nombre del archivo = open("nombre del arcivo", "a") "a" significa append
# con esto le damos a entender a python que queremos anadir informacion al archivo
#
# Y se veria algo asi:
#
# nombre_del_archivo = open("nombre del archivo.txt", "a")
#
# segundo debemos llamar a nuestro archivo texto de la siguiente manera
#
# nombre_del_archivo.write("\n texto") es como si estuvieramos haciendo un archivo 
#
# luego lo cerramos nombre del archivo.close()
#
# Esto se veria asi:

archivo_texto = open("archivo.txt", "a")

archivo_texto.write("\n siempre es una buena icacion para estudiar Python")

archivo_texto.close()