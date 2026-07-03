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
        



class Moto(Vehicles): 
    
    hwheelie = ""
    def wheelie(self):
        self.hwheelie = "Im doing a wheelie"


    def status(self):
        print("Brand: ", self.brand, "\nModel: ", self.model, "\n Running: ", self.running, "\n Accelerating: ", self.accelerates, "\n braking: ", self.brakes, "\n", self.hwheelie)



class ElectricVehicles(Vehicles):
    def __init__(self, Brand, Model):


        super().__init__(Brand, Model)

        self.autonomy = 100

    def ChargeEnergy(self):

        self.charging = True

