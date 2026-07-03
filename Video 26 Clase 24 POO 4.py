class Car():


# Como crear un estado constructor en python, esto se usa para dar un estado inicial a los objetos, esto es lo que es un constructor
# para crear un estado contructor en python se hace de la siguiente manera:

    def __init__(self): # En otros lenguajes de programacion el constructor tiene el lenguaje de la clase en python es diferente siempre sera __init__


        # Luego de haber declarado el construcor debemos meter las propiedades de nuestro metodo usando self. de la siguiente manera self. + metodo como en el siguiente ejemplo:



        self.__largeChasis=250 
        self.__widthChasis=120

        # Como encapsular una variable en python
        # para encapsular una variable en python se hace de la siguiente manera es anadiendo __ por ejemplo:

        self.__wheels=4 # Aqui esta variable estaria encapsulada porque anadimos __

        self.__running=False

  

    def start(self,starting): # Aqui estariamos resumiendo un poco el codigo porque estamos anadiendo una propiedad que es el starting dentro de los ()

        # Esto lo que esta haciendo 2 tareas en 1

        self.__running=starting # Aqui aplicamos lo que haria o lo que representaria en este caso como queremos que el carro inicie tendriamos que poner el underway=starting porque es la variable que hicimos para que inicie

        if(self.__running): # aqui esta diciendo que si self.underway es igual a true nos dara el mensaje el carro esta iniciando como previamente hicimos que se.underway=starting
            return"The car is starting"

        else: 

            return "The car is stopped" 
  

    def state(self): # Aqui estamos haciendo que el carro nos diga que tiene el carro ya que le estamos dando otro valor a esta fruncion definida de la clase
        print("The car has", self.__wheels, " wheels. a width of ", self.__widthChasis, "and a large of ",
              self.__largeChasis)

        # Nota tuvimos que poner __ antes de las demas variables porque si por ejemplo habria una variable llamandose sin __ se estaria refiriendo a 2 variables diferentes porque esto __ lo esta encapsulando en ciertos casos
        # no es necesario pero en este caso como nos estamos refiriendo a una variable o estan encapuslada en toda la clase tuvimos que colocarlo
        # Ojo solo cuando queremos que no se modifique un valor que dimos dentro de una clase no se modifique fuera es que la encapsulamos con esto __ tener pendiente esto porque se puede confundir en un futuro



        
MyCar=Car() 
            


print(MyCar.start(True)) # Aqui hay que pasar el parametro porque si no lo pasamos nos dara un error

print(MyCar.state()) 

print("------------------------ A continuacion creamos el segundo objeto ------------------------")

MyCar2=Car()


print(MyCar2.start(False))

MyCar2.wheels=2 # para modificar el valor de una propiedad es de la siguiente manera nombre de la instancia + valor de la clase + = + el valor que le vamos a dar

# Como encapuslamos una variable aqui esto no serviria porque no esta siendo accesible desde fuera solo esta siendo accesible dentro de la clase por eso no cambia a 2 ruedas si no se queda en 4 ruedas

print(MyCar2.state()) 