def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):	
	try:	# Aqui vemos un ejemplo del try: except + error para poder resolver tipos de errores que pasan en el codigo y aun asi queremos que se siga ejecutando.
		# se hace de esta manera en este ejemplo.
		
		# Nota en espanol vendria diciendo que intente try:
		
		return num1/num2 # Nota ahora si el try no peude ejecutar este return lo que pasaria es a ejecutarse el except que es la lina de abajo
	
	except ZeroDivisionError: # Aqui que haga una exepcion Except + el error
		
		print("No se peude dividir entre 0, porque todo numero entre 0 es infinito o 0") # En este caso de la ejecucion del expcet seria esto el print que hicimos
		# dando a entender que se siga ejecutando el programa
		
		return "Operacion Erronea"
	
while True: # Aqui hicimos un bucle para solucionar un error en la cual cuando poniamos un texto en ves de un numero saltaba el ValueError
	# este bucle lo que hace es que uando coloque el texto vuelva a preguntar que coloce un numero y pasando por el try except del value Error solucionandolo
	
    try:
        op1=(int(input("Introduce el primer numero: ")))
    
        op2=(int(input("Introduce el segundo nuymero: ")))
        break;
		
    except ValueError:
	    print("Los valores introducidos no son correctos")
	
operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")