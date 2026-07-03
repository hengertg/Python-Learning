# Ejercicios bucle for & range


#Ejercicio 1

from math import e


for i in range(21):
    print(i)

# Ejercicio 2:

for i in [1,2,3,4,5]:
    print("Hola")


# Ejercicio 3:

for i in range(0, 21, 2):
    print(i)

# Ejercicio 4:

for i in range(1,13):
    print(f"5 x {i} = {5 * i}")


# Ejercicio 5:

Suma = 0

for i in range(1,101):
    Suma += i
    print(Suma)

# Ejercicio 6 email:

Email= False
EmailUser=input("Introduce tu email: ")
lower=EmailUser.lower()

for i in lower:
    if(i=="@" and (".com" in lower or ".es" in lower or ".us" in lower or ".do" in lower)):
        Email=True
    
if Email and ("outlook" in lower):
    print("Email Correcto")
else:
    print("Email Incorrecto")