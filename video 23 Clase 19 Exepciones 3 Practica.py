def evaluaEdad(edad):

    if edad<0:
        raise TypeError("No se permiten edades negativas") # Con raise podemos lanzar una excepcion y detener la ejecucion del programa
     # para usar raise en el bloque debemos usar raise dentro de una funcion, si lo usamos fuera de una funcion no se puede usar raise y el error que usaremos en este ejemplo es TypeError
      # pero podemos usar cualquier tipo de error que queramos, incluso podemos crear nuestros propios errores personalizados.

    if edad<20:
       return "Eres muy joven "
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate.."
    
print(evaluaEdad(-15))



def evaluaEdad2(edad):

    if edad<0:
        raise MiPropioError("No se permiten edades negativas") # En este caso hicimos un error personalizado, pero cuando ejecutamos el programa nos da un error diciendo que no se encuentra definido
        # el error MiPropioError, para solucionarlo debemos crear una clase que herede de la clase Exception y dentro de esa clase podemos definir nuestro propio mensaje de error.
    if edad<20:
         return "Eres muy joven "
    elif edad<40:
      return "eres joven"
    elif edad<65:
         return "Eres maduro"
    elif edad<100:
         return "Cuidate.."
    
print(evaluaEdad2(-15))

