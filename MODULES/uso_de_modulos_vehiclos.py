from module_vehicles import *

myCar = Vehicles("Mazda", "MX5")

myCar.status()

#=======================================================================================================================================================================================================================
# Nota
#=======================================================================================================================================================================================================================
#
# Si en dado caso movemos el modulo a una carpeta diferente y dejamos from module_vehicles import * nos daria un error
# Ya que python no lo leeria porque el archivo que esta buscando no se encuentra en la misma carpeta y pasaria python a buscarlo en syspath
#
# y Como se soluciona esto?
#
# Pues se soluciona con algo llamado paquetes o en ingles package