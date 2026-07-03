print("programa de evaluacion de alumnos")

nota_alumno=input("Introduce la nota del alumno: ")

def evaluacion(nota): # Aqui estamos definiendo la variable evaluacion con def y le anadimos el parametro(nota)
    valoracion="aprobado" # Aqui creamos una variable para dar el mensaje que vendria siendo valoracion="aprobado" para cuando sea mayor 5 nos devuelva el aprobado
    if nota <5: # Aqui usamos el condicional if con el parametro nota y anadimos <5 para dar la funcion
        valoracion = "suspenso" # Aqui creamos la variable valoracion = "suspenso" esto esta debajo de if ya que hicimos que en dado caso que sea menos a 5
        # nos devuelva el mensaje de suspenso
    return valoracion # aqui el return para que nos devuelva el mensaje de suspenso

print(evaluacion(int(nota_alumno))) # y aqui para poder imprimirlo en pantalla la variable definida evaluacion (int) para poder colocar los numeros enteros con el teclado
# cuando nos lo pregunte y (nota_alumno) indicando en que parte del codigo se ejecutara cuando introduzcamos el dato