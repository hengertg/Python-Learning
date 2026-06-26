class Car(): # Para crear una clase primero va Class + nombre de la clase en mayusucla + () y al final : y su correspendiente indentacion luego de la identacion iria el codigo de la clase
    largeChasis=250 # Receuerda que las clase tiene propiedades en este ejemplo esta la priemra propiedad de la clase que es largeChasis y su valor es 250
    widthChasis=120
    wheel=4
    starting=False

    # Recordamos que un carro tiene un comportamiento y para eso se crean metodos que son funciones dentro de la clase y para crear un metodo se hace de la misma manera que una funcion pero con la diferencia
    #  que el primer parametro es self que hace referencia a la clase y a sus propiedades

    def start(self): # Para crear un metodo usamos def + nombre del metodo o funcion + () y dentro de los parentesis van los parametros que se le pasaran a la funcion y al final :
        # y su indentacion correspondiente, tambien se coloca self, esto hace referencia al propio objeto de la clase y a sus propiedades.
        # en python es obligatorio colocar el self mientras que en otro lenguajes de programacion se usa this y no es obligatorio colocarlo.

        self.starting=True # Aqui se esta accediendo a la propiedad state de la clase Car y se le esta asignando el valor True, esto indica que el carro esta encendido.
                        # Para hacer esto es de la siguiente manera self + state + valor, en otras palabras el parametro + la propieda de la clase state + el valor.
                        # Python nos obliga especificar el self

    # Ahora quedaria comprobar si nuestro Car en nuestro codigo esta en marcha o no lo esta y esto se hace de la siguiente manera...

    # Estableceriamos otro comportamiento como en el siguiente ejemplo

    def state(self): # Aqui creariamos un metodo para el estado del Car en este ejemplo seria def + funcion o metodo + (self)
        if(self.starting): # Luego dariamos la condicion con el if, aqui no es necesario = True porque aunque no lo pusieramos ya python lo detecta automatica mente como True
            return "The car is starting" # El return o el mensaje
        
        else: # Luego la condicion else en dado caso de que no se cumpla

            return "The car is stopped" # y Aqui el mensaje o lo que trabajariamos en este caso el mensaje o lo que hara
        


# Como crear un objeto de la clase Car o perteneciente a la clase Car, para eso se hace de  la siguiente manera: nombre del objeto = nombre de la clase() y al final se coloca ()
#  para indicar que es un objeto de la clase Car

MyCar=Car() # Aqui se crea un objeto de la clase Car y se le asigna a la variable MyCar, ahora MyCar es un objeto de la clase Car y puede acceder a sus propiedades y metodos.
            # Esto tambian se conoce como instanciar un objeto de la clase Car, y MyCar es una instancia de la clase Car.
            # Aqui no se usa el operador new como en otros lenguajes de programacion, en python no es necesario usarlo para crear un objeto de una clase.
            

# Para acceder a las propiedades de la clase Car desde el objeto MyCar se usa la nomenclatura del punto. Por Ejemplo:

print("The large chasis of My Car is: ", MyCar.largeChasis)
print (" The car has: ", MyCar.wheel, " wheels")

# y si queremos acceder al comportamiento de la clase Car desde el objeto MyCar se hace de la misma manera, usando la nomenclatura del punto. Por Ejemplo:

MyCar.start()

print(MyCar.state()) # Imprimmos el codigo de esta manera
