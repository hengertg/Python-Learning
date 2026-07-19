from tkinter import *

root = Tk()

miFrame = Frame(root, width=1000, height= 600)

miFrame.pack()

# ==========================================
# Como importar una imagen?
# ==========================================
# para importar una imagen primero debemos crear una variable y usamos el method Photoimage() y en el parametro usamos file="" y dentro de los quotes la ruta de la imagen
# ==========================================

miImagen = PhotoImage(file="Graficos/cat.png")

# ==========================================
# Como incluir un texto? 
# ==========================================
# Usaremos la clase label() y dentro de los parentesis hay que especificar el contenedor padre
# ==========================================
#
# En este ejemplo usaremos miFrame como contenedor padre
#
# Para poner el texto usamos text=""
# ==========================================
#
# Tambien se puede usar el .place() dentro de la variablee miLabel que hemos creado en otras palabres despeus de label() ejemplo:
# ==========================================
# Como cambiar el color del texto?
# ==========================================
# Con fg="color en ingles" se puede cambiar el color del texto
# ==========================================
# Como cambiar el tipo de letra y tamano de las letras?
# ==========================================
# Pues usariamos el method font=() y dentro de los parentesis iria el tamano y el nombre de la fuente de la letra ejemplo:
# font=("Comic Sans MS", 18)
# ==========================================
# para andir la imagen dentro del label o en la root se usaria image=
# ==========================================

# miLabel =   Label(miFrame, text="Hola profesor de Python Samuel, Pildoras Informaticas", fg="red", fon=("Comic Sans MS",18)).place(x=100,y=200)

miLabel =   Label(miFrame,image=miImagen).place(x=100,y=200)

# ==========================================
# Que es el method place(x= numero de posicion, y= numero de posicion)
# ==========================================
#
# Es para posicionar el label o el texto en este caso respetando la posicion o tamano del Frame
# miLabel.place(x=100, y=200)

root.mainloop()