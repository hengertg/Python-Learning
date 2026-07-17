from tkinter import *

raiz = Tk()
# ==========================================
#
# Para dar un titulo a la ventana con tkinter es tan facil como usar title() y en el parametro el nombre o titulo de la ventana
# ==========================================

raiz.title("Ventana de pruebas")


# ==========================================
# Para cambiar el size o tamano de la ventana en tkinter es tan sencillo como usar resizable()
#
# Los parametros que pondermos son 2 y son de tipo boolean el primero seria el witdh y el segundo el height
#
# Nota:
#
# Si en cualqueira de los 2 lo dejamos en 0 eso quiere decir que es false y que no nos permitira modiciar el with o height dependiendo donde lo tengamos puesto el 0
#
# Tambien podemos usar True or False en ves de usar numeros para el width & height
# ==========================================

raiz.resizable(1,1)

# ==========================================
# Como cambiar el icono
# ==========================================
#
# Para cambiar el icono debemos tener un archivo .ico
#
# Luego usaremos el metodo iconbitmap("") y entre parentesis y comilla la ruta del icono o de la imagen 
# ==========================================

raiz.iconbitmap("Graficos/yo.ico")

# ==========================================
# Como cambiar el tamano por defecto?
# ==========================================
#
# Es tan sencillo como usar el metodo geometry() dentro de los parametros obviamente dentrro de "" daremos la resolucion que queremos de la ventana
# ==========================================

raiz.geometry("650x350")


# ==========================================
# Como cambiar el background?
# ==========================================
# Para cambiar el background debemos usar el siguiente metodo que es .config() dentro de los parametros usamos bg que significa back ground y luego el color entre "" seria algo asi (bg="")

raiz.config(bg="black")

# ==========================================
# Nota improtante colcoando .pyw hara que se abra el archivo sin la consola de windows detras
# ==========================================

# ==========================================
# El mainloop() es un tipo de bucle infinito que lo que hace es mantener la ventana abierta es como un tipo bucle while
#
# Nota:
#
# Es importante que el evento mainloop() este en el ultimo lugar para que neustra ventana se quede abierta por completo hasta que decidamos cerrarla
# ==========================================

raiz.mainloop()