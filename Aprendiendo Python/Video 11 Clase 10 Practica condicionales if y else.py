print("Verificacion de acceso")

edad_usuario = int(input("Introduce tu edad, por favor "))

if edad_usuario < 18:
    print("No puedes pasar") 

elif edad_usuario>100:
    print("Edad no valida") #Nota al haber 2 if en la ejecuccion se ocasion un bug ya que daria correcto las 2 instruccion y mandaria los 2 mensajes 
    # porque sigue la ejecuccion hacia abajo y saltaria al else porque el else busca el if mas cercano si queremos evaluar muchos condiciones que tiene que estar
    # acompanado de un else se utiliza otra funcion que vendria siendo la instruccion elif ejemplo:

else: # Nota para poder usar el else siempre primero debe de haber un if ya que no es posible.

    print("puedes pasar")

print("El programa ha finalizado")


print("Verificacion de nota")

nota_alumno = int(input("Introduce tu nota, por favor "))

if nota_alumno < 5:
    print("reprobado")

elif nota_alumno < 6:
    print("suficiente")

elif nota_alumno < 7:
    print("bien")

elif nota_alumno < 9:
    print("notable")
else:
    print("Excelente")