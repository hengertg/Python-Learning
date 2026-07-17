from tkinter import *

raiz2 = Tk()

raiz2.title("Ventana de pruebas")




raiz2.resizable(1,1)



raiz2.iconbitmap("Graficos/yo.ico")



raiz2.geometry("650x350")




raiz2.config(bg="black")

# ==========================================
# Como crear un frame?
# ==========================================
#
# Para crear un frame necesitamos una variable donde almacenar el frame
#
# Luego de la variable usamos Frame() para crear el frame

miFrame = Frame()

# ==========================================
# Como empaquetar mi frame?
# ==========================================
#
# Para eso debemos usar el method pack() para empaquetar el frame
# ==========================================
#
# Si dentro de los parametros de pack osea dentro de los () le anadimos side ="bottom" o cualquier direccion hara que el frame se mueva hacia cierto lugar de la interface

# ==========================================
# Como darle un color de fondo al frame?
# ==========================================
#
# Pues usando .config() y dentro de los parametros bg="color" se le da el color a un frame
# ==========================================
#
# Con anchor="" eso maneja puntos cardinales n = north,  s = south, e = east, w = west
#
# Tambien podemos aplicar un rellenado del frame con fill = "" x,y,both,none
#
# nota para fill  verticalmente hay que usar el method expand=True


miFrame.pack(side="bottom",anchor="n",fill="y",expand="True")

# ==========================================
# Como darle un color de fondo al frame?
# ==========================================
#
# Pues usando .config() y dentro de los parametros bg="color" se le da el color a un frame
# ==========================================
#
# Con anchor="" eso maneja puntos cardinales n = north,  s = south, e = east, w = west
#
# Tambien podemos aplicar un rellenado del frame con fill = "" x,y,both,none
#
# nota para fill  verticalmente hay que usar el method expand=True

miFrame.config(bg="red")

# ==========================================
# Como darle tramano al frame?
# ==========================================
#
# pues usamos el method .config() y dentro de los parentesis en el paramestro usamos width & height con su respectivo valor
# ==========================================

miFrame.config(width="350", height="350")

# ==========================================
# Como cambiar el grosor del borde?
# ==========================================
#
# Para eso debemos usar el method bd= para cambiar el grosor del borde del frame
# ==========================================

miFrame.config(bd=35)

# ==========================================
# Como cambiar el borde?
# ==========================================
#
# Para cambiar el borde debemos usar el method relief="" y dentro de los quotes el tipo de borde
# ==========================================

miFrame.config(relief="sunken")

# ==========================================
# Como cambiar el tipo de cursor dentro del frame?
# ==========================================
# para eso usamos el method cursor="" y dentro de los quotes el tipo del cursor
# ==========================================

miFrame.config(cursor="pirate")

raiz2.mainloop()