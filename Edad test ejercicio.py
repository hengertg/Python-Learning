print("Verificacion de edad")

edad=input("Introduce tu edad: ")

def Mayor_de_edad(edad):
    if edad>=18:
     Mayor="Eres mayor de edad bienvenido"
     return Mayor
    if edad <18:
        Menor="Eres menor de edad vuelve cuando te crezcan pelos en el culo"
        return Menor

print(Mayor_de_edad(int(edad)))


print("Verificacion de edad")

edad=input("Introduce tu edad: ")


# para mejorarlo se podria hacer con else y se simplificaba mucho mas y se escribia menos codigo 😅

def Mayor_de_edad(edad):
    if edad>=18:
     Mayor="Eres mayor de edad bienvenido"
     return Mayor
    
    else:
        Menor="Eres menor de edad vuelve cuando te crezcan pelos en el culo"
        return Menor

print(Mayor_de_edad(int(edad)))

Enter=input("Presiona enter para terminar la verificacion...")