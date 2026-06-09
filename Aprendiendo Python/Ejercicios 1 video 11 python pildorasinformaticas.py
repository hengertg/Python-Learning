# Devolver el numero mas alto

num1=int(input("Introduce el primer numero: "))
num2=int(input("Introduce el segundo numero: "))
def DevuelveMax (n1,n2):

    if n1 < n2:
        print(n2)

    elif n2 < n1:
        print(n1)

    else:
        print("son iguales")

print("El numero mas alto es: ")

DevuelveMax(num1, num2)

# Ejercicio Lista

Nombre=input("Introduce tu nombre: ")
Direccion=input("Introduce tu direccion: ")
Telefono=input("Introduce tu telefono: ")

Lista_de_datos=[Nombre, Direccion, Telefono]

print("Los datos personales son:",Lista_de_datos[0],  Lista_de_datos[1], Lista_de_datos[2])

# Media aritmetica

numero1=int(input("Introduce tu primer numero: "))
numero2=int(input("Introduce tu segundo numero: "))
numero3=int(input("Introduce tu tercer numero: "))

media=(numero1 + numero2 + numero3)/3
print("La medida aritmetica es:")
print(media)
