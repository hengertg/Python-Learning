# Aqui combinariamos un try: except de manera consecutiva, ejemplo:


def divide():

    try:

        op1=(float(input("Introduce el primer numero: ")))
        op2=(float(input("Introduce el segundo numero: ")))

        print(f"La division es", str(op1/op2))

    except ValueError:

        print("El Valor introducido es erroneo:")
    
    except ZeroDivisionError:

        print("No se puede dividir entre 0!")

    finally: # Finally: Sirve para ejecutar un bloque de codigo siempre, haya o no un error

        # Explicacion del Finally: esto es util para cerrar archivos, conexiones a bases de datos, etc. ya que si hay un error en el bloque try:
        #  except, el bloque finally: se ejecutara igualmente
        # Finally funciona de la siguiente manera: si hay un error en el bloque try: except, el bloque finally:
        #  se ejecutara igualmente, y si no hay un error, el bloque finally: se ejecutara igualmente
        print ("Calculo finalizado")


divide()


# Ejemplo en caso de hacer un try: except general de los errores
# Nota 2 esto no es recomendable


def divide2():

    try:

        op1=(float(input("Introduce el primer numero: ")))
        op2=(float(input("Introduce el segundo numero: ")))

        print(f"La division es", str(op1/op2))

    except:
        print("Ha ocurrido un error, revisa los valores introducidos")

    print ("Calculo finalizado")

divide2()


# En este ejemplo hacemos que con finally se ejecute el print("Calculo finalizado") apesar de no haber puesto el except: en el bloque de codigo
# dando el error pero siempre ejecutando el print("Calculo finalizado")


def divide3():

    try:

        op1=(float(input("Introduce el primer numero: ")))
        op2=(float(input("Introduce el segundo numero: ")))

        print(f"La division es", str(op1/op2))

    finally:
        print("Ha ocurrido un error, revisa los valores introducidos")

    print ("Calculo finalizado")

divide3()