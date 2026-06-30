# ==========================================
# HERENCIA EN PYTHON
# ==========================================
#
# Temas de esta clase:
#
# • Herencia simple
# • Herencia múltiple
# • Sobrescritura de métodos (Method Overriding)
#
# ==========================================




# ==========================================
# CLASE PADRE (SUPERCLASE)
# ==========================================
#
# Esta será nuestra clase padre (también llamada
# superclase o clase base).
#
# Todas las clases que hereden de ella obtendrán
# automáticamente sus atributos y métodos.
#
# En Python 3 NO es obligatorio escribir () al
# declarar una clase.
#
# Python interpreta exactamente igual:
#
# class Vehicles:
# class Vehicles():
#
# Ambos ejemplos crean la misma clase.
#
# Los paréntesis solamente son necesarios cuando
# queremos indicar que una clase hereda de otra.
#
# Ejemplo:
#
# class Vehicle:
#     pass
#
# class Car(Vehicle):
#     pass
#
# En este caso Car hereda todos los atributos y
# métodos de Vehicle.
#
# ==========================================

class Vehicles:

    def __init__(self, brand, model):
        
        self.brand = brand
        self.model = model
        self.running = False
        self.accelerates = False
        self.brakes = False

    def run(self):

        self.running = True

    def accelerate(self):
        
        self.accelerates = True

    def brake(self):

        self.brakes = True

    def status(self):
        print("Brand: ", self.brand, "\nModel: ", self.model, "\n Running: ", self.running, "\n Accelerating: ", self.accelerates, "\n braking: ", self.brakes)


# ==========================================
# HERENCIA SIMPLE
# ==========================================
#
# La clase Van hereda de Vehicles.
#
# Gracias a la herencia, Van obtiene automáticamente
# todos los atributos y métodos definidos en Vehicles.
#
# Además, podemos crear métodos exclusivos para Van.
#
# En este caso agregamos el método load(), que
# solamente pertenece a las vans.
#
# ==========================================


class Van(Vehicles):
    
    def load(self, loading):
        self.loaded = loading
        if(self.loaded):
            return "The van is loaded"
        else:
            return "The Van is not loaded"



# ==========================================
# HERENCIA SIMPLE + MÉTODO PROPIO
# ==========================================
#
# Moto también hereda de Vehicles.
#
# Al heredar, obtiene automáticamente todos los
# atributos y métodos de la clase padre.
#
# Además, podemos agregar métodos exclusivos
# pertenecientes solamente a Moto.
#
# En este ejemplo agregamos el método wheelie().
#
# ==========================================

class Moto(Vehicles): 
    
    hwheelie = ""
    def wheelie(self):
        self.hwheelie = "Im doing a wheelie"

# ==========================================
# SOBRESCRITURA DE MÉTODOS
# (Method Overriding)
# ==========================================
#
# Si una clase hija crea un método con el mismo
# nombre que uno existente en la clase padre,
# el método de la clase hija reemplaza al heredado.
#
# En este caso estamos sobrescribiendo status().
#
# Si NO escribiéramos este método, Moto utilizaría
# automáticamente el status() heredado de Vehicles.
#
# Lo sobrescribimos porque queremos mostrar también
# el estado del wheelie.
#
# ==========================================
    
    def status(self):
        print("Brand: ", self.brand, "\nModel: ", self.model, "\n Running: ", self.running, "\n Accelerating: ", self.accelerates, "\n braking: ", self.brakes, "\n", self.hwheelie)



# ==========================================
# NUEVA CLASE
# ==========================================
#
# Esta clase representa un vehículo eléctrico.
#
# Más adelante la utilizaremos para demostrar
# cómo funciona la herencia múltiple.
#
# ==========================================

class ElectricVehicles():
    def __init__(self):
        self.autonomy = 100

    def ChargeEnergy(self):

        self.charging = True


# ==========================================
# INSTANCIAS
# ==========================================
#
# Una instancia es un objeto creado a partir de
# una clase.
#
# Sintaxis:
#
# variable = Clase()
#
# Ejemplo:
#
# MyMoto = Moto("Honda", "CBR")
#
# En este caso debemos enviar brand y model porque
# el constructor (__init__) los solicita.
#
# Si el constructor no recibiera parámetros,
# simplemente crearíamos la instancia con:
#
# MiObjeto = Clase()
#
# ==========================================

MyMoto = Moto("Honda", "CBR")

MyMoto.wheelie() 

MyMoto.status()

MyVan=Van("Renault", "Kangoo")

MyVan.run()

MyVan.status()

print(MyVan.load(True))


# ==========================================
# HERENCIA MÚLTIPLE
# ==========================================
#
# Python permite heredar de varias clases al mismo
# tiempo.
#
# Para hacerlo simplemente escribimos todas las
# clases padre separadas por comas.
#
# Sintaxis:
#
# class ElectricBicycle(ElectricVehicles, Vehicles):
#
# La nueva clase heredará automáticamente todos los
# atributos y métodos de ambas clases.
#
# ==========================================



class EletricBicycle(ElectricVehicles,Vehicles):
    pass


# ==========================================
# ORDEN DE LOS CONSTRUCTORES
# ==========================================
#
# Cuando heredamos de varias clases, Python busca
# los métodos siguiendo un orden específico.
#
# En este ejemplo, Python utilizará primero el
# constructor (__init__) de la primera clase que
# aparece en la herencia.
#
# class ElectricBicycle(ElectricVehicles, Vehicles)
#
# Primero buscará:
#
# ElectricVehicles.__init__()
#
# Si cambiáramos el orden:
#
# class ElectricBicycle(Vehicles, ElectricVehicles)
#
# Entonces utilizaría primero el constructor de
# Vehicles.
#
# Este comportamiento forma parte del Method
# Resolution Order (MRO), que veremos más adelante.
#
# ==========================================

MyBicycle = EletricBicycle()


# ==========================================
# NOTA IMPORTANTE
# ==========================================
#
# Cada clase hija solamente puede utilizar los
# métodos que ha heredado o los que ella misma
# define.
#
# Por ejemplo:
#
# MyMoto.load(True)
#
# produce un error porque load() pertenece
# exclusivamente a la clase Van.
#
# ==========================================

# MyMoto.load(True)