import math

def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El numero no puede ser negativo") # En este ejemplo de raise estamos usando un error predefinido de python
        #en este caso estamos usando ValueError, y estamos dandole un mensaje personalizado
        #  pero podemos usar cualquier tipo de error que queramos, incluso podemos crear nuestros propios errores personalizados.
    else:
        return math.sqrt(num1)
    



op1=(int(input("Introduce un numero: ")))

try:
    print(calculaRaiz(op1))

except ValueError as ErrorDeNumeroNegativo: # En este ejemplo usando except estamos capturando el error que lanzamos con raise
    # y estamos dandole un nombre a ese error para poder usarlo dentro del bloque except

    # Para poder siempre darle el nombre despues del error debemos usar as y el nombre que queramos darle al error
    #  en este caso le dimos el nombre de ErrorDeNumeroNegativo

    print(ErrorDeNumeroNegativo)

print("Programa terminado")