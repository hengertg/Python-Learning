# Ejercicio 1: 
# • Crea un programa que pida números infinitamente. Los números introducidos deben 
# ser cada vez mayores El programa finalizará cuando se introduce un número menor que 
# el anterior.


NumUser = int(input("Introduce un numero, por favor: "))

NumUser2 = int(input("Introduce un numero mayor que: " + str(NumUser) + ": "))

while NumUser > NumUser2:
   NumUser = NumUser2
   NumUser2 = int(input("Introduce un numero mayor que: " + str(NumUser) + ": "))

   print()
   print(NumUser2, f"No es mayor que", str(NumUser))


   # Ejercicio 2: 
# • Crea un programa que pida números positivos indefinidamente. El programa termina 
# cuando se introduce un número negativo. Finalmente el programa muestras la suma de 
# todos los números introducidos 


numero=int(input("Introduce un numero: "))
suma=0

while numero >0:
      suma = suma + numero
      numero = int(input("Introduce otro numero: "))

print("La suma de los numeros introducidos es ", str(suma) )