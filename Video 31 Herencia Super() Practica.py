# ==========================================
# HERENCIA EN PYTHON
# ==========================================
#
# Temas de esta clase:
#
# • Funcion super()
# • Funcion isinstance()
# ==========================================
#
# HERENCIA SUPER() EJEMPLOS Y PRACTICAS
#
# ==========================================


class Person:

    def __init__(self, name, age, living_place):
        
        self.name = name

        self.age = age

        self.living_place = living_place

    def description(self):

        print(f"Name: {self.name} Age: {self.age} Residence: {self.living_place}")



# Existe un concepto llamado Substitution Principle
# Traducido al espanol es siempre un/a
#
#
# En codigo esto se traduciria de la siguiente manera 
# cuando tenemos una herencia un objeto de la subclase siempre sera un objeto de la super clase o clase padre
#
# En este ejemplo un empleado es una persona o antes que empleado es una persona 
# Sin embargo al reves esto no se da osea que una persona no comienza siendo un empleado pero sin embargo un empleado es siempre una persona
# en otras palabras Employee es una sub clase de la super clase Person o de la clase padre Person


class Employee(Person):

    def __init__(self, salary, seniority, name_employee, age_employee, residence_employee):

        # ==========================================
        # ¿Qué hace super()?
        # ==========================================
        #
        # super() nos permite llamar al constructor
        # de la clase padre (Person).
        #
        # Gracias a esto no tenemos que volver a escribir:
        #
        # self.name = ...
        # self.age = ...
        # self.living_place = ...
        #
        # La clase padre se encarga de inicializar
        # esos atributos por nosotros.
        #
        # NOTA:
        # super() también puede utilizarse para llamar
        # otros métodos de la superclase.
        #
        # ==========================================

        super().__init__(name_employee, age_employee, residence_employee)
        
        self.salary = salary

        self.seniority = seniority

    # ==========================================
    # CURIOSIDAD
    # ==========================================
    #
    # En proyectos grandes es muy común utilizar
    # super() porque evita duplicar código y hace
    # que las clases sean mucho más fáciles de
    # mantener.
    #
    # Esta es una práctica muy utilizada en el
    # desarrollo profesional.
    #
    # ==========================================

    # ==========================================
    # ERROR COMÚN
    # ==========================================
    #
    # Muchos principiantes creen que super()
    # copia el código de la clase padre.
    #
    # En realidad NO lo copia.
    #
    # Lo que hace es ejecutar el método original
    # de la superclase.
    #
    # ==========================================

    def description(self):

        super().description()
        
        print(f"Salary: {self.salary} Seniority: {self.seniority}")


# ==========================================
#
# Función isinstance()
#
# ==========================================
#
# La función isinstance() nos permite comprobar si un objeto
# pertenece o es instancia de una clase determinada.
#
# Esto es muy útil cuando estamos trabajando en programas grandes
# y no tenemos claro a qué clase pertenece un objeto antes de
# realizar alguna operación con él.
#
# Sintaxis:
#
# isinstance(Objeto, Clase)
#
#
# ==========================================
# NOTA IMPORTANTE
# ==========================================
#
# isinstance() devuelve:
#
# True  -> Si el objeto pertenece a esa clase.
# False -> Si el objeto NO pertenece a esa clase.
#
# Esta función también tiene en cuenta la herencia.
# Es decir, si una clase hereda de otra, isinstance()
# reconocerá esa relación.

Manuel = Person("Manuel", 25, "New York")

# Si Manuel fuera creado como Employee:
#
# Manuel = Employee(1500, 15, "Manuel", 25, "New York")
#
# Entonces Manuel también sería considerado un objeto
# de la clase Person porque Employee hereda de Person.

Manuel.description()

# ==========================================
#
# isinstance() EJEMPLOS Y PRÁCTICAS
#
# ==========================================
#
# Para utilizar isinstance() debemos escribir:
#
# isinstance(Nombre_del_objeto, Nombre_de_la_clase)
#
# El primer argumento siempre es el objeto.
# El segundo argumento es la clase que queremos comprobar.
#
# Ejemplo con el ejercicio actual:

print(isinstance(Manuel, Person))

# Resultado:
# True
#
# Porque Manuel fue creado como un objeto de la clase Person

# Ejemplo para comprobar si es de la clase Employee y de False o sea False

print(isinstance(Manuel, Employee))

# Resultado:
# False
#
# Porque Manuel NO fue creado como un objeto Employee.


# ¿Qué pasaría si Manuel fuera creado como Employee?
#
# Manuel = Employee(1500, 15, "Manuel", 25, "New York")
#
# Resultado:
#
# isinstance(Manuel, Employee) -> True
# isinstance(Manuel, Person)   -> True
#
# ¿Por qué?
#
# Porque Employee hereda de Person.
# Todo Employee también es un Person.