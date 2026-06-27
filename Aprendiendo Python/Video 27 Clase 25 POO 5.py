# Como encapsular un metodo

class Car():

    def __init__(self): 

        self.__largeChasis=250 
        self.__widthChasis=120
        self.__wheels=4 
        self.__underway=False


    def start(self,starting):
        self.__underway = starting 

        if(self.__underway):
            check=self.__internal_check()

        if(self.__underway and check):
            return"The car is starting"
        
        elif(self.__underway and check == False):
            return "Something went wrong checking the car, it can't start"

        else: 

            return "The car is stopped" 
  
    def state(self): 
        print("The car has", self.__wheels, " wheels. a width of ", self.__widthChasis, "and a large of ",
              self.__largeChasis)
        

    def __internal_check(self): # Para encapsular un metodo es igual para encapsular las variables de uan clase es colocando __ + variable una vez encapsulada donde estemos usando esa variable hay que colocar__
        # para que el codigo o flujo de codigo entienda que nos referimos a esa variable encapsulada
        # Nota 2 al encapuslarla esto hace que no sea posible llamar a este metodo desde fuera solo sera llamado desde dentro como en esta caso, si fuera del codigo pusiera print(MyCar.__Internal_check())
        # No funcionaria porque estoy intentando llamarla desde fuera, en caso de no estar llamandola desde fuera funcionaria normal porque como en este ejemplo del codigo esta encapsulado desde dentro
        # del metodo de la propia clase
        print("Doing an internal check")

        self.gas = "Ok"
        self.oil = "Ok"
        self.doors = "Closed"

        if(self.gas=="Ok" and self.oil=="Ok" and self.doors=="Closed"):

            return True
        
        else:
            return False

      
        
MyCar=Car() 
            


print(MyCar.start(True))

print(MyCar.state()) 

print("------------------------ A continuacion creamos el segundo objeto ------------------------")

MyCar2=Car()

print(MyCar2.start(False))

print(MyCar2.state()) 
