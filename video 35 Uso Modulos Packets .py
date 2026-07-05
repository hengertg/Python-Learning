# ====================================================================================
# COMO USAR LOS MODULES DE UN PACKETS QUE CREAMOS:
#
# Para eso usaremos from + mas nombre de la carpeta + . + nombre del modulo + import + especifacmos la funcion a la que queremos acceder
# ====================================================================================

# from Calculus.General_Calculus import *

# redondear(4.8)

# ====================================================================================
# Tambien podemos crear sub packets o mas carpetas para hacerlas como sub packets
# ====================================================================================
#
# Como se crea?
#
# Tan facil como hacer mas carpetas con nombre en donde estamos guardando los paquetes
#
# ====================================================================================
# NOTA:
# ====================================================================================
#
# Dentro de cada carpeta de paquetes o dentro de cada carpeta de sub paquetes
# debe de haber un archivo python llamadop __init__.py
# ====================================================================================
# NOTA 2:
# ====================================================================================
#
# Para poder acceder a esos paquetes es tan facil como usar la nomenclatura del punto
#
# Ejemplo:
#
# From + Nombre de la carpeta + . + nombre del modulo + import + espeficiacion de la funcion o clase, etc que queremos accedere
# ====================================================================================

# ====================================================================================
# Como usar un sub paquete?
# ====================================================================================
#
# Para usar un sub paquete es sencillo debemos siempre tener el nombre del archivo y la ruta y se haria de la siguiente manera
# 
#  from + nombre de la carpeta del paquete + . + nombre de la carpeta del sub paquete + . + nombre del modulo + import + especifacmos la funcion a la que queremos acceder

from Calculus.basics.Operaciones_Basicas import *

# ====================================================================================
# Esto importaria el otro sub paquete
# ====================================================================================

from Calculus.redondeo_potencia.RedondeoyPotencia import *

sumar(5,7)

potencia(5,7)