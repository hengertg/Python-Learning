class Vehicles:
    # En Python 3 no es obligatorio escribir () al declarar una clase.
    # Python interpreta igual:
    #
    # class Cars:
    # class Cars():
    #
    # Ambos ejemplos crean la misma clase.
    #
    # Los paréntesis sí son necesarios cuando una clase hereda de otra.
    # En ese caso, dentro de los paréntesis se escribe el nombre de la
    # clase padre (superclase).
    #
    # Ejemplo:
    #
    # class Vehicle:
    #     pass
    #
    # class Car(Vehicle):
    #     pass
    #
    # Aquí Car hereda todos los atributos y métodos de Vehicle.

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

# ¿Cómo heredar una clase en Python?
#
# Para heredar una clase primero debemos tener una clase padre
# (también llamada superclase o clase base).
#
# Después creamos una nueva clase y, entre paréntesis,
# escribimos el nombre de la clase padre.
#
# Sintaxis:
#
# class ClaseHija(ClasePadre):
#     pass
#
# Ejemplo para heredar una clase en Python:
#
class Moto(Vehicles): 
# Si no heredamos la clase o en otras palabras no hubieramos colocado nada dentro () da un error.

    pass

MyMoto=Moto("Honda", "CBR")

MyMoto.status()