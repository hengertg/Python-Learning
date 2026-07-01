# ==========================================
# POLIMORFISMO
# ==========================================
#
# • El polimorfismo en programacion quiere decir que un objeto puede cambiar de forma
#  dependiendo del contexto que se utilice
#
# Otra Deifinicion de polimorfismo
#
# Distintos objetos pueden responder al mismo método de maneras diferentes.
# 
# ==========================================

# ==========================================
#
# EJEMPLO DE POLIMORFISMO
#
# ==========================================

class Car:
    def movement(self):
        print ("My movement is with 4 wheels")

class Bike():
    def movement(self):
        print("My movement is with 2 wheels")

class Truck():
    def movement(self):
        print("My movement is with 6 wheels")





# ==========================================
#
# Para usar el polimorfismo debemos crear una funcion
# Para crear esta funcion de polimorfimos es de la siguiente manera:
# def + nombre del polimorfismo + ():
# Ejemplo: def polimorfismo():
#
# Nota: dentro de los () debe haber un parametro
#
# Luego de eso debemos hacer la funcion a la cual pertenece la clase que estariamos llamando ejemplo
# nombre del parametro que esta dentro de los () + . + el metodo + ()
# Ejemplo: parametro.metodo()
#
# Una vez teniendo todo esto ya solo quedaria hacer el objeto a la cual usuariamos el polimorfimos
# para que este polimorfismo llame a la clase del cual estamos usando ese metodo
# Ejemplo: Mi objeto = clase()
#
# Y para llamar a ese metodo usando el polimorfismo es de la siguiente manera:
#
# Como tenemos def polimorfismo(parametro): arriba como en la explicacion previa para llamarlo se hace lo siguiente
#
# polimorfismo(objeto)
#
# Esto lo que hace que en logica es que el polimorfismo esta llamando al objeto y su metodo de su clase correspondiente.
#
# ==========================================
def movementVehicle(vehicle):
    vehicle.movement()


myVehicles = Bike()

movementVehicle(myVehicles)

# ==========================================
#
# En este ejemplo que hicimos
#
# def movementVehicle(vehicle):
#  vehicle.movement()
#
#myVehicles = Bike()

# movementVehicle(myVehicles)
#
# Aqui habiamos creado el polimorfismo def movementVehicle(vehicle):
# dentro de los () dimos el parametro vehicle ya que es lo que usaremos para llamar a nuestro objeto de nuestra clase
# luego tenemos nuestro metodo del polimorfismo que es vehicle.movement()
# luego tenemos nuestro objeto de la clase correspondiente que en este caso es myVehicles = Bike()
#
# y luego tenemos nuestro llamado de nuestro polimorfismo llamando a esa clase que es movementVehicle(myVehicles)
#
# La logica detras de todo esto o lo que esta pasando con python es que movementVehicle(myVehicles) python esta llamando a movementVehicle que es el metodo de polimorfismo que hicismo
# junto con nuestro objeto myVehicles que esta dentro los () luego este dentro de este metodo def movementVehicle(vehicle): la funcion vehicle.movement() esta llamando al metodo de la clase correspondiente
# que hemos assignado en ovementVehicle(myVehicles)
#
# ==========================================