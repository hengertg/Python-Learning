print("Introduce tus datos para iniciar sesion")

usuario=input()
contrasena=input()

def login(usuario, contrasena):
    if usuario == "Henger" and contrasena == 1234:
        Bienvenido="Haz iniciado sesion correctamente"
        return Bienvenido
    else:
        Error="Credenciales incorrectos"
        return Error
    
Resultado = login(usuario,int(contrasena))

print(Resultado)

input("Presiona enter para continuar")

 