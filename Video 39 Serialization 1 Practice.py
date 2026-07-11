import pickle

lista_nombres = ["Pedro", "Sara", "Maria", "Isabel"]


# Para dar a entender que un archivo es de escritura binaria usamos wb esto significa write binary o eso le da a entender a python que es un archivo de escritura binaria

fichero_binario = open("lista_nombres","wb")


# para usar el metodo dump debemos primero usar la libreria pickle + .dump() dentro de los parentesis van el archivo y el nombre del archivo como parametros

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

# Para borrar el fichero de la memoria usamos del()

del (fichero_binario)


# =========================================================================================
#
# Para rescatar un archivo que ya esta dumped con .dump() y poder leerlo es sencillo

# Debemos manter el import de pickle o importarlo
#
# luego una variable + = + nombre del archivo +("Nombre del arcivo", "rb") rb vendria significando read binary
#
# Por ejemplo

fichero = open("lista_nombres", "rb")

# Luego usamos el method de pickle que es pickle.load() dentro de los parentesis que vendria siendo el metodo donde tenemos guardado el fichero

lista = pickle.load(fichero)

print(lista)
