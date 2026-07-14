# ==========================================
# Hoy veremos f-string\
# ==========================================
#
# Ventajas de f-strings
#
# - Mas legible
# - Mas concisas
# - Soporte para expresiones complejas
# - Mas eficientes
# - Mas directas con especificaciones de formatos


import pickle

class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        print(f"A new person has been created with the name of {self.name}")


    def __str__(self):
        # return "{} {} {}".format(self.name, self.gender, self.age)
        return f"{self.name}, {self.gender},{self.age}"
    
class PeopleLists:

    people = []

    def __init__(self):
        
        

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
