# ==========================================
# HERENCIA - EJEMPLO PRÁCTICO
# ==========================================
#
# En este ejercicio utilizaremos una clase padre
# llamada Vehicles y varias subclases que heredarán
# de ella.
#
# Gracias a la herencia evitamos repetir código,
# ya que las clases hijas podrán utilizar los
# atributos y métodos de Vehicles.
#
# Clases que heredan:
#
# • Van
# • Moto
# • ElectricVehicles
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


class Van(Vehicles):
    
    def load(self, loading):
        self.loaded = loading
        if(self.loaded):
            return "The van is loaded"
        else:
            return "The Van is not loaded"
        

# ==========================================
# SOBRESCRITURA DE MÉTODOS (OVERRIDE)
# ==========================================
#
# Moto heredará todos los métodos de Vehicles.
#
# Sin embargo, sobrescribiremos el método
# status() para añadir información extra
# específica de las motocicletas.
#
# Esto se conoce como Method Override.
#
# ==========================================


class Moto(Vehicles): 
    
    hwheelie = ""
    def wheelie(self):
        self.hwheelie = "Im doing a wheelie"


    def status(self):
        print("Brand: ", self.brand, "\nModel: ", self.model, "\n Running: ", self.running, "\n Accelerating: ", self.accelerates, "\n braking: ", self.brakes, "\n", self.hwheelie)



# ==========================================
# APLICANDO super() EN ESTE EJERCICIO
# ==========================================
#
# Como ElectricVehicles hereda de Vehicles,
# también necesita inicializar los atributos
# brand y model que pertenecen a la clase padre.
#
# Para conseguirlo utilizamos:
#
# super().__init__(Brand, Model)
#
# Gracias a esto no tenemos que volver a escribir:
#
# self.brand = Brand
# self.model = Model
#
# La clase padre ya realiza ese trabajo.
#
# Después añadimos únicamente los atributos
# propios de ElectricVehicles.
#
# ==========================================

class ElectricVehicles(Vehicles):
    def __init__(self, Brand, Model):

        # Llamamos al constructor de Vehicles para que
        # inicialice automáticamente los atributos brand
        # y model heredados de la clase padre.

        super().__init__(Brand, Model)

        self.autonomy = 100

    def ChargeEnergy(self):

        self.charging = True


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
# En Python una clase puede heredar de varias
# clases al mismo tiempo.
#
# En este caso ElectricBicycle hereda de:
#
# • ElectricVehicles
# • Vehicles
#
# Python seguirá un orden para buscar métodos
# y constructores. A este orden se le conoce
# como MRO (Method Resolution Order).
#
# Lo veremos con más detalle más adelante.
#
# ==========================================

class EletricBicycle(ElectricVehicles,Vehicles):
    pass


# ==========================================
# ¿QUÉ ESTÁ HACIENDO PYTHON?
# ==========================================
#
# ElectricBicycle no tiene un constructor (__init__)
# propio.
#
# Cuando creamos un objeto:
#
# MyBicycle = ElectricBicycle(...)
#
# Python busca un constructor siguiendo el orden
# de la herencia.
#
# Como ElectricBicycle no tiene uno, utiliza el
# constructor de ElectricVehicles.
#
# Dentro de ese constructor se ejecuta:
#
# super().__init__(Brand, Model)
#
# Esa línea llama automáticamente al constructor
# de Vehicles para inicializar brand y model.
#
# Gracias a esto el objeto queda completamente
# inicializado sin repetir código.
#
# ==========================================

MyBicycle = EletricBicycle("Orbea", "Ihj")