# ====================================================================================
# Hoy Veremos como guardar un archivo o fichero de manera permanente en un archivo externo
# ====================================================================================
#
# Este fichero hara que se quede de manera permanente en nuestro sistema hasta que lo borremos
# ====================================================================================

import pickle

# ====================================================================================
# Vamos a necesitar la libreria pickle obiamente
# ====================================================================================

class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        print(f"A new person has been created with the name of {self.name}")

# ==========================================
# __str__ (Magic Method / Dunder Method)
# ==========================================

# __str__ es un método especial de Python.
# Su función es decirle a Python cómo mostrar un objeto como texto.

# Python ejecuta __str__ automáticamente cuando usamos:
# print(objeto)
# o
# str(objeto)

# Sin __str__, Python muestra algo parecido a:
# <__main__.ClassName object at 0x000001F...>

# Con __str__, nosotros decidimos qué información mostrar.

# IMPORTANTE:
# __str__ SIEMPRE debe retornar (return) un string.

# ==========================================
# .format()
# ==========================================

# .format() sirve para insertar valores dentro de un string.

# Ejemplo:
# "Hello {}".format("Henger")
# Resultado:
# Hello Henger

# También puede insertar varios valores:
# "{} {}".format(valor1, valor2)

    def __str__(self):
        return "{} {} {}".format(self.name, self.gender, self.age)
    
class PeopleLists:

    people = []

    def __init__(self):
        
        # ab+ significa append binary + esto es para anadir en un archivo binaria informacion es con ab+

        listofpeople = open("FicheroExterno", "ab+") 
        listofpeople.seek(0)


        try:
            self.people = pickle.load(listofpeople)
            print("The information of {} has been loaded to the external file".format(len(self.people)))
        
        except:
            print("The file is empty")
        
        finally:
            listofpeople.close()
            del(listofpeople)


    def addPeople(self, p):
        self.people.append(p)
        self.savePersonInExternalFile()

    def showPeople(self):
        for p in self.people:
            print(p)

    def savePersonInExternalFile(self):

        listofpeople = open ("FicheroExterno", "wb")
        pickle.dump(self.people, listofpeople)
        listofpeople.close()
        del(listofpeople)

    def showInfoExternalFile(self):
        print("The information of the external file is: ")

        for p in self.people:
            print(p)

myList = PeopleLists()
people = Person("Ana", "Female", 19)
myList.addPeople(people)
myList.showInfoExternalFile()
