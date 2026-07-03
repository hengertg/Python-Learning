print("Inicia sension intrudociendo tus credenciales")

Credenciales_usuario=input()
Contrasena=input()

def login(usuario,contrasena):

    credenciales_incorrectos="credenciales incorrectos"
    Bienvenido="Bienvenido has iniciado sesion correctamente"


    if usuario =="henger" and contrasena == 1234:
        return Bienvenido
    
    return credenciales_incorrectos

resultado = login("henger", 1234) # Aqui hay un error ya que cuando se coloca cualquiera de las 2 informacion en el usuario o contrasena siempre iniciara sesion

print(resultado)

enter=input("presiona enter para cerrar...")  

# Esta primera version hace que si obligatoriamente para iniciar sesion haya que escribir "Henger" como usuario y "1234" como contrasena entonces esto hace que cuando haya
# una base de datos con varios usuarios y un nuevo usuario se registra con sus credenciales no podra iniciar sesion porque para iniciar sesion hay que poner lo que estan
# predefinido ya que en este caso seria "Henger" como usuario y "1234" como contrasena pero esto se puede solucionar de la siguiente manera ejemplo:


# Version correcta o solucionada

# En este caso el problema con el codigo anterior es que estamos llamado a la variable resultado que en el login deban colocar obligatoria mente "henger" y "1234"
# resultado = login("henger", 1234) esto hace lo mencionado previamente que los nuevos usuarios no puedan iniciar sesion con sus credenciales la forma correcta
# para evitar este problema es modificando la variable resultado de la siguiente manera resultado = login(Credenciales_usuario, int(contrasena)).
# devido a que la variable Credenciales_usuario se esta utilizando para almacenar la informacion del usuario y cuando se coloca la informacion como habiamos programado
# con el inpunt() esto permite que el codigo busque en la base de ddatos o compare ese usuario y lo de como correcto en dado caso de que tuvieramos una base de datos
# y con Contrasena pasa igual pero a la hora de print hay que colocar int() ya que lo habiamos programado como un entero ya que en el codigo hay numeros como contrasena
# en ves de textos o str

print("Inicia sension intrudociendo tus credenciales")

Credenciales_usuario=input()
Contrasena=input()

def login(usuario, contrasena):

    credenciales_incorrectos="credenciales incorrectos"
    Bienvenido="Bienvenido has iniciado sesion correctamente"


    if usuario =="henger" and contrasena == 1234:
        return Bienvenido
    
    else:
     return credenciales_incorrectos

resultado = login(Credenciales_usuario, int(Contrasena)) # La forma correcta seria esta ya que con la variable resultado estamos llamando a que Credenciales_usuario
# compare if usuario == "henger" y int(contrasena) and contrasena == 1234 asi que si colocamos la contrasena como usuario nos la dara como un error

print(resultado)

enter=input("presiona enter para cerrar...") 
