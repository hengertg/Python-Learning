import pickle

# ====================================================================================
# Hoy Veremos como serializar objetos
# ====================================================================================
#
# Primero que todo tenemos que import pickle

class Vehicles():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.starting = False
        self.running = False
        self.brake = False


    def running(self):
        self.running = True

    def starting(self):
        self.starting = True

    def brake(self):
        self.brake = True


    def status(self):
        print(f"Brand: {self.brand} Model: {self.model} Running: {self.running} Starting: {self.starting} Braking: {self.brake}")



car1= Vehicles("Nissan", "GT-R")

car2= Vehicles("Toyota", "Supra")

car3= Vehicles("Ford", "Mustang Shelby")

cars = [car1, car2, car3]

fichero = open("TheCars","wb")

pickle.dump(cars, fichero)

fichero.close()

del (fichero)

ficheroOpen = open("TheCars", "rb")

myCars = pickle.load(ficheroOpen)

ficheroOpen.close()

for c in myCars:

    print(c.status())