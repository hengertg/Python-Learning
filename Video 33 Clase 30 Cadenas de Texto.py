# ==========================================
# STRING CHAINS
# ==========================================
#
# • Python considera a los caracteres como objetos y esos objetos son strings
#
#  Hoy veremos algunos metodos importantes para manipular cadenas
#
# Las cadenas de texto es lo mas frecuentemente usado.
#
# ==========================================
#
# String Methods
#
# ==========================================
#
# Existen varios metodos de los string chains
#
# ==========================================
#
# upper() esto convierte en mayuscula todas las letras de un string
#
# lower() Hace lo contrario convierte en minisculas todas las letras de un string
#
# capitalize() Lo que hace en un string es convertir la primera letra en mayusculas
#
# count() Hace es contar cuantas veces aparece una letra o una cadena de caracteres dentro de un texto o una frase
#
# find() Lo que hace es representar el indice o la posicion en la cual aparece un caracter o un grupo de caracteres en un texto
#
# isdigit() lo que devuelve un booleano True o False lo que hace es decirno si el valor introducido es un digito un valor numero o no lo es
#
# isalum() Lo que hace comprobar si es un alfanumerico
#
# isalpha() Lo que hace comprobar si hay solo letras, los espacios no cuentam
#
# split() separa palabra por palabra utilizando espacios
#
# strip() Elimina los espacios sobrantes al principio y al final
#
# replace() cambia una palabra o una letra por otra dentro de un string
#
# rfind() hace lo mismo que find() representa el indice de un caracter pero lo hace contando desde atras osea contando desde el principio del string de ahi la r
# representando reverse

# Link para info y documentacino de python: https://pyspanishdoc.sourceforge.net/lib/string-methods.html (Espanol)
# Link para info y documentacion de python https://docs.python.org/3/library/index.html (English)

# ==========================================
#
# Ejemplos
#
# ==========================================

nombreUsario = input("Introduce tu nombre de usuario: ")

# ==========================================
#
# Para usar los String methods de python debemos es de la siguiente manera variable + . + stringmeethod()
# En este caso seria nombreUsuario.upper() hay que colocar el .upper() y sus parentesis ya que los string methods se consideran objetos por eso el . y sus ()
#y asi suscesivamente con los demas ejemplos

# ==========================================

print(f"El nombre es: {nombreUsario.capitalize()}")

# ==========================================
#
# Ejemplos 2
#
# ==========================================
#
# En este ejemplo estamos usamos el string method .isdigit() lo que hace es devolvernos True o False en caso de que sea un digito por ejemplo
# si en el input escribimos un texto nos devovlera False porque vendria siendo un string el texto que introducimos
# Y si sintroducimos un digito o numero nos devolvera True porque introducimos un digito
#
# ==========================================

edad = input("Introduce la edad: ")

print(edad.isdigit())


# ==========================================
#
# Ejemplos 3
#
# ==========================================

edad2 = input("Introduce your age: ")

while(edad2.isdigit()==False):
    print(f"Please introduce a digit number")

    edad2 = input("Introduce your age: ")

if (int(edad2)<18):

    print(f"You can't continue")

else:
    print(f"you can continue")