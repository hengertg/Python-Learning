print("Verifica tu edad")

edad=input("Introduzca su edad: ")

def introducir_edad(edad):
    if edad < 18:
        Error="No eres mayor de edad"
        return Error
    elif edad > 100:
        No_Valido="Edad no valida"
        return No_Valido
    else:
        Edad_verificada="Gracias por confirmar tu edad"
        return Edad_verificada
    
print(introducir_edad(int(edad)))
    
enter=input("Presiona enter para continuar...")
